from django.db import models


class Service(models.Model):
    service = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service
