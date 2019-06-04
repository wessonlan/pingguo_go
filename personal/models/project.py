from django.db import models

# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=50, null=False)
    describe = models.TextField(max_length=255, default='')
    status = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name