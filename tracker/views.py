from django.shortcuts import render
from .models import AuditTrail

def audit_log(request):
    logs = AuditTrail.objects.all().order_by('-timestamp')
    return render(request, 'audit_log.html', {'logs': logs})
