from django.urls import path
from . import views
from .views import MetricCreateView, MetricLatestView, MetricHistoryView, MetricRangeView, dashboard_view

urlpatterns = [
    path('api/metrics/', MetricCreateView.as_view(), name='metric-create'),
    path('api/metrics/latest/<str:host_name>/', MetricLatestView.as_view(), name='metric-latest'),
    path('api/metrics/history/<str:host_name>/', MetricHistoryView.as_view(), name='metric-history'),
    path('api/metrics/range/<str:host_name>/<str:range_key>/', MetricRangeView.as_view(), name='metric-range'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
