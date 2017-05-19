#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from posts.views import ExtendUserViewSet

router = routers.DefaultRouter()
router.register(r'extuser', ExtendUserViewSet)

urlpatterns = [
        url(r'', include(router.urls)),
]
