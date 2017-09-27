# -*- coding: utf-8 -*-

from rest_framework import authentication
from rest_framework import exceptions
from .models import Tenant


class TenantAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        tenant = Tenant.objects.filter(
            api_key=request.GET.get('api_key')
        ).last()

        if not tenant:
            raise exceptions.AuthenticationFailed('Invalid API key')

        tenant.update_api_count()
