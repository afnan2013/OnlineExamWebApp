from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Question, Category, Exam, ExamPaper, Student

# Register your models here.
admin.site.unregister(Group)


class QuestionAdmin(admin.ModelAdmin):
    search_fields=['question']

class ExamPaperAdmin(admin.ModelAdmin):
    search_fields = ['id', 'paperName']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Exam)
admin.site.register(ExamPaper, ExamPaperAdmin)
admin.site.register(Student)