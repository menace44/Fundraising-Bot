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

    def test_donate_below_minimum(self):
        response = self.app.post('/donate', data=dict(name='Alice', amount='5'))
        self.assertIn('Donation must be between $10 and $5000.', response.data.decode())

    def test_donate_above_maximum(self):
        response = self.app.post('/donate', data=dict(name='Bob', amount='6000'))
        self.assertIn('Donation must be between $10 and $5000.', response.data.decode())

    def test_raffle_ticket_assignment(self):
        self.app.post('/donate', data=dict(name='Alice', amount='250'))
        self.assertEqual(bot.raffle_tickets['Alice'], ['Ticket #1', 'Ticket #2', 'Ticket #3'])

    def test_check_progress(self):
        bot.total_donations = 1000
        bot.goal_amount = 2000
        total, milestones = bot.check_progress()
        self.assertIn(b'Total donations: $1000.00 (50.00%)', total.encode())
        self.assertIn('Milestone: 50%', milestones)

    def test_set_goal(self):
        bot.set_goal(3000)
        self.assertEqual(bot.goal_amount, 3000)

    def test_add_prizes_and_draw_winners(self):
        bot.add_prizes(['Prize 1', 'Prize 2'])
        self.app.post('/donate', data=dict(name='Alice', amount='250'))
        self.app.post('/donate', data=dict(name='Bob', amount='150'))
        winners = bot.draw_winners()
        self.assertIn('Prize 1', winners)
        self.assertIn('Prize 2', winners)

if __name__ == '__main__':
    unittest.main()
