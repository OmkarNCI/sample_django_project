from django.test import TestCase
from .models import Sample

class SampleTest(TestCase):
    def test_create_sample(self):
        s = Sample.objects.create(name='SonarCloud')
        self.assertEqual(s.name, 'SonarCloud')