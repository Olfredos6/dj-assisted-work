from django.test import TestCase

from . import models


class PublisherTestCase(TestCase):
    def test_can_create_publisher(self):
        publisher = models.Publisher.objects.create(name="Publisher 1")
        self.assertQuerySetEqual(models.Publisher.objects.all(), [publisher])
