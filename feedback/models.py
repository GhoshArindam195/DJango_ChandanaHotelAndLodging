from django.db import models


# Create your models here.
class Feedback(models.Model):
    f_from = models.CharField(max_length=50)
    f_type = models.CharField(max_length=50)
    f_subject = models.CharField(max_length=500)
    f_content = models.CharField(max_length=500)
    is_actioned = models.BooleanField(default=False)

    def __str__(self):
        return self.f_subject
