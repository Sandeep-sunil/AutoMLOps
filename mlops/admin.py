from django.contrib import admin
from .models import MLModel, PipelineRun
# Register your models here.

@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "version",
        "framework",
        "status",
        "created_at",
    )

    list_filter = ("status", "framework")
    search_fields = ("name", "version", "framework")
    ordering = ("-created_at",)


@admin.register(PipelineRun)
class PipelineRunAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "status",
        "started_at",
        "completed_at",
        "created_at",
    )

    list_filter = ("status",)
    search_fields = ("model__name", "logs")
    ordering = ("-created_at",)