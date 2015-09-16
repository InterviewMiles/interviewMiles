from rest_framework import serializers
from api.models import *

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
        model = McqChioces
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

