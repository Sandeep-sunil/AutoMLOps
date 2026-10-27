from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard_home(request):
    context = {
        "total_models": 4,
        "healthy_models": 3,
        "active_incidents": 2,
        "drift_alerts": 1,
        "remediations_today": 5,
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )