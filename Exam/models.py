from django.db import models

# Create your models here.
class Questions(models.Model):
    CAT_CHOICES = (
    ('set1','Set1'),
    ('set2','Set2'),
    ('set3','Set3'),
    ('set4','Set4')
    )
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question
