import sys

from approver.models import *
from approver.signals.bridge.model_signals import model_push

import django
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import fields, signals
from django.test import TestCase, Client
from approver.tests.tests_models.test_utils import check_fields

class ProjectTestCase(TestCase):
    def setUp(self):
        signals.post_save.disconnect(model_push, Project)
        pass

    def test_project_model(self):
        self.assertTrue(check_fields(Project,"title","Char",300))
        self.assertTrue(check_fields(Project,"description","Text"))
