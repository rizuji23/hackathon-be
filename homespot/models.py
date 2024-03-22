from django.db import models

# Create your models here.
class Testimoni(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_testimoni = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    image = models.ImageField(upload_to="testimoni/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.id_testimoni