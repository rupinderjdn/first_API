from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name
class Car(models.Model):
    slug=models.SlugField(null=False,blank=False)
    name=models.CharField(max_length=256)
    image=models.ImageField(upload_to="project images",blank=True,null=True)
    about=models.TextField()
    tags=models.ManyToManyField("Tag",blank=True)
    CreatedAt=models.DateTimeField(auto_now_add=True)
    UpdatedAt=models.DateTimeField(auto_now_add=True)
    favourited=models.BooleanField()
    def __str__(self):
        return self.name