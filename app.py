import random
import math
from flask import Flask, request, render_template

app = Flask(__name__)

class FundraisingBot:
    def __init__(self, goal_amount, min_donation=10, max_donation=5000):
        """Initialize the fundraising bot with a donation goal."""
        self.goal_amount = goal_amount
        self.donations = {}  # To track user donations
        self.total_donations = 0  # Sum of all donations
        self.description = "Support our cause by donating today! Your contribution helps us reach our fundraising goal and make a difference."
        self.min_donation = min_donation
        self.max_donation = max_donation
        self.raffle_tickets = {}
        self.milestone_notifications = [0.5, 1.0]  # Notify at 50%, 100% of the goal
        self.reached_milestones = []

    def donate(self, user_name, amount):
        """Accept a donation from a user."""
        if amount < self.min_donation or amount > self.max_donation:
            return f"Donation must be between ${self.min_donation} and ${self.max_donation}."
        
        if user_name in self.donations:
            self.donations[user_name] += amount
        else:
            self.donations[user_name] = amount
        self.total_donations += amount
        self.assign_raffle_tickets(user_name, amount)
        return f"Thank you {user_name} for donating ${amount:.2f}!"

    def assign_raffle_tickets(self, user_name, amount):
        """Assign raffle tickets based on donation amount."""
        # Calculate tickets: one ticket per $100, rounded up
        tickets = math.ceil(amount / 100)  # Use regular division and round up
        if user_name not in self.raffle_tickets:
            self.raffle_tickets[user_name] = []
        # Assign exactly the calculated number of tickets
        self.raffle_tickets[user_name] = [f"Ticket #{i + 1}" for i in range(tickets)]

    def get_progress(self):
        """Return the progress towards the fundraising goal."""
        return self.total_donations, self.goal_amount

    def check_progress(self):
        """Check fundraising progress and milestones."""
        progress = self.total_donations / self.goal_amount
        milestones = []
        for milestone in self.milestone_notifications:
            if progress >= milestone and milestone not in self.reached_milestones:
                self.reached_milestones.append(milestone)
                milestones.append(f"Milestone: {int(milestone * 100)}%")
        return f"Total donations: ${self.total_donations:.2f} ({progress*100:.2f}%)", milestones

    def set_goal(self, new_goal_amount):
        """Set a new goal for the fundraising campaign."""
        self.goal_amount = new_goal_amount
        return f"New fundraising goal set to ${new_goal_amount:.2f}"

    def add_prizes(self, prize_list):
        """Add prizes for the raffle."""
        self.prizes = prize_list

    def draw_winners(self):
        """Select winners based on raffle tickets."""
        winners = {}
        all_tickets = [(user, ticket) for user, tickets in self.raffle_tickets.items() for ticket in tickets]
        random.shuffle(all_tickets)
        for prize in self.prizes:
            if all_tickets:
                winner = random.choice(all_tickets)
                winners[prize] = winner[0]
                all_tickets.remove(winner)
        return winners

bot = FundraisingBot(goal_amount=1000)

@app.route("/")
def index():
    total, goal = bot.get_progress()
    description = bot.description
    return render_template('index.html', 
                         total=total, 
                         goal=goal, 
                         description=description,
                         min_donation=bot.min_donation,
                         max_donation=bot.max_donation)

@app.route("/donate", methods=["POST"])
def donate():
    user_name = request.form["name"]
    amount = float(request.form["amount"])
    message = bot.donate(user_name, amount)  # Capture the message
    total, goal = bot.get_progress()
    description = bot.description
    
    # Get progress milestones
    _, milestones = bot.check_progress()
    
    # Get user's tickets if donation was successful
    tickets = bot.raffle_tickets.get(user_name, []) if 'Thank you' in message else []
    
    return render_template('index.html', 
                         total=total, 
                         goal=goal, 
                         message=message, 
                         description=description,
                         min_donation=bot.min_donation,
                         max_donation=bot.max_donation,
                         tickets=tickets,
                         milestones=milestones)

if __name__ == "__main__":
    app.run(debug=True)
