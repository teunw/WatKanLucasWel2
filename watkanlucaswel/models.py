from django.db import models


# Create your models here.
class WKLWImage(models.Model):
    name = models.TextField(max_length=32)
    imageFile = models.ImageField(upload_to='static/')

    def __str__(self):
        return "{} {}".format(self.name, self.imageFile.name)


