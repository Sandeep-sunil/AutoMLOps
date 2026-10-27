from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import MLModel, PipelineRun
# Create your views here.
def model_list(request):
    models = MLModel.objects.annotate(
        pipeline_count=Count("pipeline_runs", distinct=True)
    )

    context = {
        "models": models,
        "total_models": MLModel.objects.count(),
        "healthy_models": MLModel.objects.filter(
            status="healthy"
        ).count(),
        "active_pipelines": PipelineRun.objects.filter(
            status__in=["pending", "running"]
        ).count(),
    }

    return render(request, "mlops/model_list.html", context)