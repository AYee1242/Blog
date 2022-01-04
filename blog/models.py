from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    twitter = models.CharField(max_length=50, null=True)
    linked_in = models.CharField(max_length=50, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    bootstrap_colour = models.CharField(max_length=20, default="badge-primary")

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=250)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField()
    image = models.ImageField(upload_to='uploads', null=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    author = models.ForeignKey(
        Author, null=True, on_delete=SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=1024)
    date = models.DateField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
