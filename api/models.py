from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=500)
    description=modes.CharFeild(max_length=5000)
    isMCQ=models.BooleanField(deafult=False)
    difficulty=models.FloatField()
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class Answers(models.Model):
    questionId=models.ForeignKey(Question)
    answer=models.CharField(max_length=5000)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class McqChioces(models.Model):
    questionId=models.ForeignKey(Question)
    choice=models.CharField(max_length=500)
    isCorrect=models.BooleanField(daflult=False)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class Categories(models.Model):
    parentCategoryId=models.ForeignKey(Categories)
    category=models.CharField(max_length=100)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class QuestionCategory(models.Model):
    questionId=models.ForeignKey(Question)
    categoryId=models.ForeignKey(Categories)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)
