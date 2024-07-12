from django.test import TestCase
from django.urls import reverse


from . models import Book

# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title='Can not hurt me',
                                       subtitle="Master your mind and defy the odds",
                                       author="David Goggins",
                                       isbn="9781544512273",)
        
    def test_book_content(self):
        self.assertEqual(self.book.title,"Can not hurt me")
        self.assertEqual(self.book.subtitle,"Master your mind and defy the odds")
        self.assertEqual(self.book.author,"David Goggins")
        self.assertEqual(self.book.isbn,"9781544512273")
        
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"Master your mind and defy the odds")
        self.assertTemplateUsed(response,"book.html")
            
        


