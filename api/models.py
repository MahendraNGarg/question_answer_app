# -*- coding: utf-8 -*-


import random
from django.db import models
from django.contrib.auth.models import User

RANDOM_STRING = str(random.randint(10000, 99999))


class Question(models.Model):
    title = models.CharField(max_length=300)
    private = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Answer(models.Model):
    body = models.TextField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100, default=RANDOM_STRING)
    api_count = models.IntegerField(default=0)

    def update_api_count(self):
        self.api_count = self.api_count + 1
        self.save()
