#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/2/9'
__author__ = 'zhaohongyang'
"""

from rest_framework import serializers

from . import models as labtask_model


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = labtask_model.Project
        fields = ('id', 'project_name', 'owner', 'project_status', 'project_info', 'start_time', 'end_time')

