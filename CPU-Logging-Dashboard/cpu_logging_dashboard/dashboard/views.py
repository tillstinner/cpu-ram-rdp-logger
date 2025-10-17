from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.shortcuts import render
from datetime import timedelta

from .models import Host, Metric
from .serializers import MetricSerializer, HostSerializer


# Post endpoint for metrics
class MetricCreateView(APIView):
    """POST endpoint for metrics from hosts/services."""
    def post(self, request, *args, **kwargs):
        host_name = request.data.get('host')
        if not host_name:
            return Response({"error": "host is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        host, _ = Host.objects.get_or_create(name=host_name)

        timestamp = parse_datetime(request.data.get('timestamp'))
        if not timestamp:
            timestamp = timezone.now()  # ensures a timezone-aware datetime

        metric = Metric.objects.create(
            host=host,
            timestamp=timestamp,
            cpu_percent=request.data.get('cpu', 0),  # matches service payload
            ram_percent=request.data.get('ram', 0),
            rdp_active=request.data.get('rdp_active', False)
        )

        serializer = MetricSerializer(metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MetricLatestView(APIView):
    """GET the latest metric for a given host."""
    def get(self, request, host_name):
        try:
            host = Host.objects.get(name=host_name)
        except Host.DoesNotExist:
            return Response({"error": "Host not found"}, status=status.HTTP_404_NOT_FOUND)
        
        metric = host.metrics.order_by('-timestamp').first()
        if not metric:
            return Response({"error": "No metrics found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MetricSerializer(metric)
        return Response(serializer.data)


class MetricHistoryView(APIView):
    """
    GET /api/metrics/history/<host_name>/?since=<ISO>&until=<ISO>
    Returns metrixs in a given time range
    """
    def get(self, request, host_name):
        try:
            host = Host.objects.get(name=host_name)
        except Host.DoesNotExist:
            return Response({"error": "Host not found"}, status=status.HTTP_404_NOT_FOUND)
        
        since = parse_datetime(request.GET.get('since')) if request.GET.get('since') else None
        until = parse_datetime(request.GET.get('until')) if request.GET.get('until') else None

        metrics = host.metrics.all()
        if since:
            metrics = metrics.filter(timestamp__gte=since)
        if until:
            metrics = metrics.filter(timestamp__lte=until)
        
        serializer = MetricSerializer(metrics, many=True)
        return Response(serializer.data)


class MetricRangeView(APIView):
    """
    Returns metrics for a host within a given range: '1h', '24h', '7d'
    """
    def get(self, request, host_name, range_key):
        try:
            host = Host.objects.get(name=host_name)
        except Host.DoesNotExist:
            return Response({"error": "Host not found"}, status=404)
        
        now = timezone.now()
        if range_key == '1h':
            start_time = now - timedelta(hours=1)
        elif range_key == '24h':
            start_time = now - timedelta(hours=24)
        elif range_key == '7d':
            start_time = now - timedelta(days=7)
        else:
            return Response({"error": "Invalid range"}, status=400)
        
        metrics = host.metrics.filter(timestamp__gte=start_time).order_by('timestamp')
        serializer = MetricSerializer(metrics, many=True)
        return Response(serializer.data)
    
class HostListView(APIView):
    def get(self, request):
        hosts = Host.objects.values_list('name', flat=True)
        return Response(list(hosts))


def dashboard_view(request):
    return render(request, 'dashboard.html')