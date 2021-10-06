import unittest

from translator.py import englishToFrench, frenchToEnglish

class TestLanguage(unittest.TestCase):
    def Test1(self):
            self.assertEqual(englishToFrench('women'), 'femmes') #To test if the english word is women the frech translation must be femmes
            self.assertEqual(englishToFrench('men'), 'hommes') #to test if the english word is men the french translation must be hommes

    def Test2(self):
            self.assertEqual(frenchToEnglish('femmes'), 'women') #To test if the french word is femmes the english translation must be women
            self.assertEqual(frenchToEnglish('hommes'), 'men') #To test if the french word is hommes the english translation must be men

    def Test3(self):
            self.assertEqual(englishToFrench('Hello'), 'Bonjour') #To test if the english word is Hello the french translation must be Bonjour
            self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') #To test if the french word is Bonjour the english translation must be Hello
