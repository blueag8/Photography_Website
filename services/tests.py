from django.test import TestCase
from .models import Services
# Create your tests here.
class ServicesTest(TestCase):
   """"""

   def test_str(self):
       test_name = Services(name = 'A service')
       self.assertEqual(str(test_name), 'A service')
