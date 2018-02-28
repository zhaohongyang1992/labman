#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2017/11/20'
__author__ = 'zhaohongyang'
"""

from rest_framework.viewsets import ModelViewSet

from . import models as labtask_model
from . import serializers as labtask_serializer


class ProjectInfoView(ModelViewSet):
    queryset = labtask_model.Project.objects.all()
    serializer_class = labtask_serializer.ProjectSerializer
