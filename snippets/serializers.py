from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Question
from snippets.models import Answers
from snippets.models import McqChoices
from snippets.models import Categories
from snippets.models import QuestionCategory


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(queryset=Snippet.objects.all(), view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title','description','difficulty',)
        read_only_fields = ('id','isMCQ','owner','added')

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('answer')
        read_only_fields = ('id','questionId','owner','added')

class McqChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = McqChoices
        fields = ('choice','isCorrect')
        read_only_fields = ('id','questionId','owner','added')

class McqChiocesSerializer(serializers.ModelSerializer):
    class Meta:
        model = McqChoices
        fields = ('choice','isCorrect')
        read_only_fields = ('id','questionId','owner','added')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('parentCategoryId','category')
        read_only_fields = ('id','owner','added')

class QuestionCategory(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = ('questionId','categoryId')
        read_only_fields = ('id','owner','added')
