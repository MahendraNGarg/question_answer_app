# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'private', 'user']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['body', 'question', 'user']


class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_key', 'api_count']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Tenant, TenantAdmin)
