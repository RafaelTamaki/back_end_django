from django.test import TestCase
from django.urls import reverse
import pytest

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

class URLsTest(TestCase):
    def test_ok(self):
        assert 1 == 1
    
