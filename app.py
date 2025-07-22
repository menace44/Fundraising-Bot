from flask import Flask, request, render_template

app = Flask(__name__)

class AdvancedFundraisingBot:
    def __init__(self, goal_amount):
        """Initialize the fundraising bot with a donation goal."""
        self.goal_amount = goal_amount
        self.donations = {}  # To track user donations
        self.total_donations = 0  # Sum of all donations
        self.description = "Support our cause by donating today! Your contribution helps us reach our fundraising goal and make a difference."

    def donate(self, user_name, amount):
        """Accept a donation from a user."""
        if user_name in self.donations:
            self.donations[user_name] += amount
        else:
            self.donations[user_name] = amount
        self.total_donations += amount

    def get_progress(self):
        """Return the progress towards the fundraising goal."""
        return self.total_donations, self.goal_amount

bot = AdvancedFundraisingBot(goal_amount=1000)

@app.route("/")
def index():
    total, goal = bot.get_progress()
    description = bot.description
    return render_template('index.html', total=total, goal=goal, description=description)

@app.route("/donate", methods=["POST"])
def donate():
    user_name = request.form["name"]
    amount = float(request.form["amount"])
    bot.donate(user_name, amount)
    total, goal = bot.get_progress()
    description = bot.description
    return render_template('index.html', total=total, goal=goal, message=f"Thank you {user_name} for donating ${amount:.2f}!", description=description)

if __name__ == "__main__":
    app.run(debug=True)
