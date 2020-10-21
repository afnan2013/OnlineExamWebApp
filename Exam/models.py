from django.db import models

# Create your models here.
class Question(models.Model):
    CAT_CHOICES = (
    ('set1','Set1'),
    ('set2','Set2'),
    ('set3','Set3'),
    ('set4','Set4')
    )
    question = models.CharField(max_length = 250)
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option4 = models.CharField(max_length = 100)
    option5 = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question
