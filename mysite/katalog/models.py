from django.db import models

# Create your models here.

class Buku(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField()
    book_cover = models.ImageField(upload_to='cover/')
    pdf_file = models.FileField(upload_to='pdf/')
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return "{}{}".format(self.id,self.title)