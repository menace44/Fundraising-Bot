Full Finalization of the FundraisingBot Project
# Fundraising-Bot
🐣 Simple Steps to Build the Fundraising Bot

We’ll break down everything into easy parts, with explanations and code along the way.

Part 1: What We’re Doing

We are building a Fundraising Bot that lets people donate money to help reach a goal (like $1000). The bot will live on the internet so that anyone can use it from their phone or computer. It will track how much money has been donated and let people see the progress.

Part 2: Files We Need

Here’s a list of all the important files you will create:

	1.	app.py – This file will contain the bot’s brain and how it runs on the web.
	2.	templates/index.html – This is the web page where users will see the progress and donate.
	3.	requirements.txt – This file lists what your bot needs to work.
	4.	LICENSE – This file sets rules about who can use and share the bot.
	5.	README.md – This file explains what the bot does and how to use it.

Part 3: Let’s Create the Code and Files

1. 🧠 The Brain – app.py

This file runs the bot and allows people to donate. It shows how much has been donated so far and updates the page when new donations are made.

from flask import Flask, request, render_template

app = Flask(__name__)

class AdvancedFundraisingBot:
    def __init__(self, goal_amount):
        """Initialize the fundraising bot with a donation goal."""
        self.goal_amount = goal_amount
        self.donations = {}  # To track user donations
        self.total_donations = 0  # Sum of all donations

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
    return render_template('index.html', total=total, goal=goal)

@app.route("/donate", methods=["POST"])
def donate():
    user_name = request.form["name"]
    amount = float(request.form["amount"])
    bot.donate(user_name, amount)
    total, goal = bot.get_progress()
    return render_template('index.html', total=total, goal=goal, message=f"Thank you {user_name} for donating ${amount:.2f}!")

if __name__ == "__main__":
    app.run(debug=True)

What does this do?

	•	When someone visits your web page, it shows how much money has been donated so far.
	•	People can type their name and how much they want to donate.
	•	After they click “Donate,” the page updates to show the new total!

2. 🖥️ The Web Page – templates/index.html

This file shows the web page where users can see the donation progress and fill out a form to donate.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fundraising Bot</title>
</head>
<body>
    <h1>Fundraising Goal: ${{ goal }}</h1>
    <h2>Total Raised: ${{ total }}</h2>
    
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}

    <form action="/donate" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="amount">Donation Amount:</label>
        <input type="number" id="amount" name="amount" required><br><br>
        
        <input type="submit" value="Donate">
    </form>
</body>
</html>

What does this do?

	•	It shows how much has been raised so far and asks people to fill out their name and donation amount.
	•	When they click “Donate,” the page reloads and shows the new total.

3. 📋 The List of Things You Need – requirements.txt

This file tells the system what programs are needed to run the bot.

Flask==2.0.1

What does this do?

	•	It tells the computer to install Flask, which makes the web app work.

4. 📄 The License – LICENSE

This file sets the rules for who can use and share the bot.

## Contributor and Donor-Only License

**Version 1.0, 2024**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, modify, and contribute to the Software for personal use and development purposes, under the terms described below.

### Definitions:
1. **Contributor**: An individual or entity who has made a substantial contribution to the project by providing code, documentation, bug reports, feature suggestions, or other valuable feedback and improvements.
2. **Substantial Contribution**: A non-trivial contribution that has been merged into the main project repository by the project maintainers.
3. **Donor**: An individual or entity who has contributed a cumulative total of $1,000 USD or more to the project through verified financial donations.
4. **Donation**: A financial contribution made to the project, verified by project maintainers or through official donation channels associated with the project.

### Terms and Conditions:
- Contributors can use and modify the Software for personal or development purposes.
- Only Donors who have donated $1,000 or more are allowed to distribute the Software.
- All users must provide proper attribution to the original authors of the Software.

What does this do?

	•	It says that only people who contribute to the project or donate $1,000 or more can share it.

5. 📖 The Instructions – README.md

This file explains what the project is and how to install and use it.

# Fundraising Bot Web App

This is a simple web app that helps track donations and shows how close we are to reaching the goal.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fundraising_bot_web.git
cd fundraising_bot_web

2. Install the dependencies

pip install -r requirements.txt

3. Run the web app locally

python app.py

4. Access the app

Go to http://127.0.0.1:5000/ in your browser to see the app running!

**What does this do?**
- It tells people how to download, set up, and run your project on their own computer.

### Part 4: Put Everything on GitHub

1. **Initialize a Git repository**:
   - Open your terminal or command prompt in the project folder and type:

   ```bash
   git init

	2.	Add all your files:
	•	Now, tell Git to track the files you just created:

git add .


	3.	Commit your changes:
	•	This is like saving a version of your work:

git commit -m "Initial commit of fundraising bot"


	4.	Create a repository on GitHub:
	•	Go to GitHub and click on New Repository. Name it fundraising_bot_web.
	•	Don’t forget to copy the repository URL!
	5.	Push your code to GitHub:
	•	In your terminal, type:

git remote add origin https://github.com/yourusername/fundraising_bot_web.git
git branch -M main
git push -u origin main



Part 5: Make the App Work on the Internet

	1.	Install Heroku CLI and log in to deploy the app on the web.
	2.	Deploy the app to Heroku:
	•	In your terminal, type:

heroku create my-fundraising-bot
git push heroku main


	3.	Open the app on the web:
	•	After deploying, open your app by typing:

heroku open



Now, anyone with a phone or computer can go to the web address and donate to your fundraiser! 🎉

