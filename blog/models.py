from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    date =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "images/", default="django.jpg")
    
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title