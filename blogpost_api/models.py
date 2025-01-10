from django.contrib.auth.models import User
from tags_api.models import TagSchema
from django.db import models

# Create your models here.
class BlogPostSchema(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=100)
    body_text = models.TextField()
    img_data = models.ImageField(upload_to='blogpost_images/', blank=True, null=True)
    tags = models.ManyToManyField(TagSchema, related_name="blog_posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.title}, {self.author.username}, {self.created_at}, {self.likes}'