from django.core.management.base import BaseCommand
from dashboard.models import Metric
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = "Delete metrics older than 7 days"

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=7)
        deleted, _ = Metric.objects.filter(timestamp__lt=cutoff).delete()
        self.stdout.write(f"Deleted {deleted} old metrics")
