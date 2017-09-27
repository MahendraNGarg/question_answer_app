# -*- coding: utf-8 -*-

from rest_framework import generics
from django_filters import rest_framework
from django.views.generic import ListView
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from .authentication import *
from .filters import *


class QuestionListViews(generics.ListAPIView):
    """
    View to list of questions
    """
    authentication_classes = (TenantAuthentication,)
    serializer_class = QuestionListSerializer
    model_class = serializer_class.Meta.model
    queryset = model_class.objects.all().exclude(private=True)
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = QuestionFilter


class QuestionRetriveView(generics.RetrieveAPIView):
    """
    View to get specific question's detail
    """
    authentication_classes = (TenantAuthentication,)
    serializer_class = QuestionDetailSerializer
    model_class = serializer_class.Meta.model
    queryset = model_class.objects.all().exclude(private=True)
    filter_backends = (rest_framework.DjangoFilterBackend,)


class DashboardView(ListView):
    model = Tenant
    template_name = 'api/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['questions'] = models.Question.objects.count()
        context['answers'] = models.Answer.objects.count()
        context['users'] = User.objects.count()
        return context
