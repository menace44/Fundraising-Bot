import random

class FundraisingBot:
    def __init__(self, goal_amount, min_donation=10, max_donation=5000, deadline=None):
        """Initialize the bot with goal, donation limits, and optional deadline."""
        self.goal_amount = goal_amount
        self.donations = {}
        self.total_donations = 0
        self.milestone_notifications = [0.5, 1.0]  # Notify at 50%, 100% of the goal
        self.reached_milestones = []
        self.min_donation = min_donation
        self.max_donation = max_donation
        self.deadline = deadline
        self.raffle_tickets = {}
        self.prizes = []

    def donate(self, user_name, amount):
        """Accept donation and allocate raffle tickets."""
        if amount < self.min_donation or amount > self.max_donation:
            return f"Donation must be between ${self.min_donation} and ${self.max_donation}."
        if user_name in self.donations:
            self.donations[user_name] += amount
        else:
            self.donations[user_name] = amount
        self.total_donations += amount
        tickets = self.assign_raffle_tickets(user_name, amount)
        return f"Thank you {user_name}, for donating ${amount:.2f} and earning {tickets} raffle tickets!"

    def assign_raffle_tickets(self, user_name, amount):
        """Assign 1 raffle ticket per $100 donated."""
        tickets = int(amount // 100)
        if user_name not in self.raffle_tickets:
            self.raffle_tickets[user_name] = []
        for i in range(tickets):
            self.raffle_tickets[user_name].append(f"Ticket #{len(self.raffle_tickets[user_name]) + 1}")
        return tickets

    def check_progress(self):
        """Check fundraising progress."""
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

    def get_summary(self):
        """Return a summary of donations and progress."""
        summary = f"Goal: ${self.goal_amount:.2f}\nTotal Donations: ${self.total_donations:.2f}\n"
        summary += "\n".join([f"{user}: ${amount:.2f}" for user, amount in self.donations.items()])
        return summary