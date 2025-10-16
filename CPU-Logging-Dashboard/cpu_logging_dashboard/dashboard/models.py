from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Metric(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='metrics')
    timestamp = models.DateTimeField()
    cpu_percent = models.FloatField()
    ram_percent = models.FloatField()
    rdp_active = models.BooleanField()

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.host.name} @ {self.timestamp}"