from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import encrypt, home, enigma


# Create your tests here.
class SmokeTest(TestCase):

    def test_root_resolves_to_home(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_slash_enigma_resolves_to_enigma(self):
        found = resolve('/enigma')
        self.assertEqual(found.func, enigma)

    def test_slash_encrypt_resolves_to_encrypt(self):
        found = resolve('/encrypt')
        self.assertEqual(found.func, encrypt)
