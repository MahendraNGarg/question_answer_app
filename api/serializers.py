# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import *


class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title')


class AnswerListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Answer
        fields = ('id', 'body', 'user')


class QuestionDetailSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'answer')

    def get_answer(self, obj):
        answer = AnswerListSerializer(
            Answer.objects.filter(
                question=self.instance.id
            ),
            many=True
        )
        return answer.data
