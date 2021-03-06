# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/questions/$',
        views.QuestionListViews.as_view(), name='question-list'),
    url(
        r'^api/questions/(?P<pk>[0-9]+)/$',
        views.QuestionRetriveView.as_view(), name='question-individual'),
    url(r'^$', views.DashboardView.as_view(), name='default-view')
]
