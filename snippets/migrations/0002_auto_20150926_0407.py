# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=5000)),
                ('added', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parentCategoryId', models.ForeignKey(to='snippets.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='McqChoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=500)),
                ('isCorrect', models.BooleanField(default=False)),
                ('added', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=5000)),
                ('isMCQ', models.BooleanField(default=False)),
                ('difficulty', models.FloatField()),
                ('added', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now=True)),
                ('categoryId', models.ForeignKey(to='snippets.Categories')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('questionId', models.ForeignKey(to='snippets.Question')),
            ],
        ),
        migrations.AddField(
            model_name='mcqchoices',
            name='questionId',
            field=models.ForeignKey(to='snippets.Question'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questionId',
            field=models.ForeignKey(to='snippets.Question'),
        ),
    ]
