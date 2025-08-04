from flask import Flask, request, jsonify
from models import donors, campaigns

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Fundraising Bot API is running"})


@app.route("/donors", methods=["GET", "POST"])
def manage_donors():
    if request.method == "GET":
        return jsonify(donors)
    if request.method == "POST":
        new_donor = request.json
        donors.append(new_donor)
        return jsonify({"message": "Donor added successfully"}), 201


@app.route("/campaigns", methods=["GET", "POST"])
def manage_campaigns():
    if request.method == "GET":
        return jsonify(campaigns)
    if request.method == "POST":
        new_campaign = request.json
        campaigns.append(new_campaign)
        return jsonify({"message": "Campaign created successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
