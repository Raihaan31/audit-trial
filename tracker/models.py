from django.db import models

class AuditTrail(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    model_name = models.CharField(max_length=100)
    action = models.CharField(max_length=6, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} - {self.action} at {self.timestamp}"
