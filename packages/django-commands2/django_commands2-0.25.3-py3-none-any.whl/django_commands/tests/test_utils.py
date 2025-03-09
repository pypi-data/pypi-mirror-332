#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase

from django_commands.models import CommandLog
from django_commands.utils import iter_large_queryset


LOGGER = logging.getLogger("django_commands")
# LOGGER.setLevel(logging.DEBUG)


class Test(TestCase):

    def test_same_field(self):
        CommandLog.objects.create(name="a")
        CommandLog.objects.create(name="a")
        CommandLog.objects.create(name="a")
        CommandLog.objects.create(name="a")
        CommandLog.objects.create(name="b")
        CommandLog.objects.create(name="b")
        CommandLog.objects.create(name="b")
        for i in range(7):
            results = set()
            for sub_queryset in iter_large_queryset(
                    CommandLog.objects.all(), ordering_field="name",
                    batch_size=i,
                    ):
                for user in sub_queryset:
                    self.assertNotIn(user.id, results)
                    results.add(user.id)
            self.assertEqual(
                    len(results), 7
            )
