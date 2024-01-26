from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name     = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = ((0, 'Draft'), (1, 'Published'),)
    title       = models.CharField(max_length=200, unique=True)
    slug        = models.SlugField(max_length=200, unique=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on  = models.DateTimeField(auto_now=True)
    content     = models.TextField()
    content     = RichTextField()
    image       = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Add this line for the image field
    created_on  = models.DateTimeField(auto_now_add=True)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)
    status      = models.IntegerField(choices=STATUS_CHOICES, default=0)
    likes       = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    resized_image = ImageSpecField(source='image',processors=[ResizeToFit(300, 300)],format='JPEG',options={'quality': 90})
    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"


class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.post.title}"


