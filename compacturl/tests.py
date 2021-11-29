from django.test import TestCase
from .models import Shortener

# Create your tests here.
class ShortenerModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Shortener.objects.create(long_url="https://github.com/ahmadsb/CompactURL#activate-the-virtual-environment")


    def test_string_method(self):
        shortener = Shortener.objects.get(id=1)
      
        expected_string = f"compact: {shortener.long_url} to {shortener.short_url}"
        self.assertEqual(str(shortener), expected_string)

