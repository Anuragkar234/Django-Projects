from django.db import models

""" 
# defining a tuple
PRIORITY = [
    ("H", "High"),
    ("M", "Medium"),
    ("L", "Low"),
]

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 60) # If you define char field, then you need to define max length
    question = models.TextField(max_length = 400)
    priority = models.CharField(max_length = 1, choices = PRIORITY)

    # what default method to show
    # check the two string method in JS or android
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "The Question"
        verbose_name_plural = "People's Questions"
 """

