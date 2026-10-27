from django.db import models

# Create your models here.
class MLModel(models.Model):

    STATUS_CHOICES = [
        ("registered", "Registered"),
        ("training", "Training"),
        ("healthy", "Healthy"),
        ("degraded", "Degraded"),
        ("failed", "Failed"),
    ]

    name = models.CharField(max_length=150)
    version = models.CharField(max_length=50)
    framework = models.CharField(max_length=100, default="scikit-learn")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="registered",
    )

    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "version"],
                name="unique_ml_model_version",
            )
        ]

    def __str__(self):
        return f"{self.name} (v{self.version})"


class PipelineRun(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("running", "Running"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    ]

    model = models.ForeignKey(
        MLModel,
        on_delete=models.CASCADE,
        related_name="pipeline_runs",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    logs = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.model.name} - {self.status}"