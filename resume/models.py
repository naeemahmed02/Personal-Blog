from django.db import models

class Resume(models.Model):
    job_title = models.CharField(max_length=200)
    resume_file = models.FileField(upload_to='files/resume', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return self.job_title