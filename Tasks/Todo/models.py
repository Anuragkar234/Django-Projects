from django.db import models

# Create your models here.

class TODO(models.Model):
    title = models.CharField(max_length=20)
    complete = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title