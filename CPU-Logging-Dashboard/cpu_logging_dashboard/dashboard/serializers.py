from rest_framework import serializers
from .models import Host, Metric

class MetricSerializer(serializers.ModelSerializer):
    host = serializers.SlugRelatedField(slug_field='name', queryset=Host.objects.all())

    class Meta:
        model = Metric
        fields = ['host', 'timestamp', 'cpu_percent', 'ram_percent', 'rdp_active']

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'ip_address', 'created_at']