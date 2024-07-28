from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_posted = models.DateField()
    category = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_posted = models.DateField()
    category = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')


    def __str__(self):
        return self.title