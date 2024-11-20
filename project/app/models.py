from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.TextField()
    instructions = models.TextField()
    cook_time = models.PositiveIntegerField(help_text="Cook time in minutes", default=0)

class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog/')
    caption = models.CharField(max_length=250)

    def __str__(self):
        return self.caption

class RecommendRecipe(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.TextField()
    instructions = models.TextField()
    cook_time = models.PositiveIntegerField(help_text="Cook time in minutes", default=0)

    def __str__(self):
        return self.name
