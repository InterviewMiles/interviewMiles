from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

        # limit the number of instances retained
        snippets = Snippet.objects.all()
        if len(snippets) > 100:
            snippets[0].delete()

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=5000)
    isMCQ=models.BooleanField(default=False)
    difficulty=models.FloatField()
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class Answers(models.Model):
    questionId=models.ForeignKey(Question)
    answer=models.CharField(max_length=5000)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class McqChoices(models.Model):
    questionId=models.ForeignKey(Question)
    choice=models.CharField(max_length=500)
    isCorrect=models.BooleanField(default=False)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class Categories(models.Model):
    parentCategoryId=models.ForeignKey("Categories")
    category=models.CharField(max_length=100)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)

class QuestionCategory(models.Model):
    questionId=models.ForeignKey(Question)
    categoryId=models.ForeignKey(Categories)
    owner=models.ForeignKey(User)
    added=models.DateTimeField(auto_now=True)
