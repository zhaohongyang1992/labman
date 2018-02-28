#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/2/9'
__author__ = 'zhaohongyang'
"""

from rest_framework.routers import DefaultRouter

from . import views as labtask_view

labtask_router = DefaultRouter()
labtask_router.register(r'project', labtask_view.ProjectInfoView)

# 自定义url
urlpatterns = [

]

# viewset urls
urlpatterns += labtask_router.urls
