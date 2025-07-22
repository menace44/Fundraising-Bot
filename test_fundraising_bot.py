import unittest
from app import app, bot

class FundraisingBotTestCase(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True
        # Reset bot donations and total for clean test
        bot.donations = {}
        bot.total_donations = 0

    def test_index_page_shows_description(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(bot.description.encode(), response.data)
        self.assertIn(b'Fundraising Goal', response.data)

    def test_donate_updates_total_and_shows_message(self):
        response = self.app.post('/donate', data=dict(name='Alice', amount='50'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you Alice for donating $50.00!', response.data)
        self.assertIn(bot.description.encode(), response.data)
        self.assertIn(b'Total Raised: $50', response.data)

    def test_multiple_donations_accumulate(self):
        self.app.post('/donate', data=dict(name='Alice', amount='50'))
        self.app.post('/donate', data=dict(name='Bob', amount='30'))
        response = self.app.get('/')
        self.assertIn(b'Total Raised: $80', response.data)

if __name__ == '__main__':
    unittest.main()
