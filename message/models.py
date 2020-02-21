from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField( max_length=500)
    pub_date=models.DateField("date_published")

class Comment(models.Model):
    commenter=models.CharField( max_length=50)
    body=models.CharField(max_length=500)
    comment_date=models.DateTimeField("date_commented")
    article=models.ForeignKey(Article, on_delete=models.CASCADE)

# Create your models here.
