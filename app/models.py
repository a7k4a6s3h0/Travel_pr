from django.db import models

# Create your models here.


class Travel_places(models.Model):
    book_name = models.CharField(max_length=100)
    book_photo = models.ImageField(upload_to='images')
    book_description = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.book_name