import unittest
import sys
import os
import re
from app import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_news(self):
        response = self.app.get('/news')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.json[0])

    def test_get_events(self):
        response = self.app.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.json[0])

  
    def test_news_date_format(self):
        response = self.app.get('/news')
        news = response.json
        date_pattern = r"\d{4}-\d{2}-\d{2}"
        for item in news:
            self.assertRegex(item['date_posted'], date_pattern, "El formato de la fecha es incorrecto")

    def test_events_date_format(self):
        response = self.app.get('/events')
        events = response.json
        date_pattern = r"\d{4}-\d{2}-\d{2}"
        for event in events:
            self.assertRegex(event['event_date'], date_pattern, "El formato de la fecha es incorrecto")

    def test_news_post_not_allowed(self):
        response = self.app.post('/news')
        self.assertEqual(response.status_code, 405)

    def test_events_delete_not_allowed(self):
        response = self.app.delete('/events')
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
