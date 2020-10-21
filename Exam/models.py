from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    shortName = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName


class Question(models.Model):
    question = models.CharField(max_length = 250)
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option4 = models.CharField(max_length = 100)
    option5 = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question




