# this is the basic backend file to run flask portion for making a connection between backend and frontend and testing for sample datasets(list).

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy influencer data
influencers = [
    {"id": 1, "name": "Influencer A", "audience": 10000, "engagement_rate": 3.5},
    {"id": 2, "name": "Influencer B", "audience": 5000, "engagement_rate": 4.0},
    {"id": 3, "name": "Influencer C", "audience": 20000, "engagement_rate": 2.0},
]

@app.route('/')
def home():
    return "Welcome to InfluencerConnect API"

@app.route('/influencers', methods=['GET'])
def get_influencers():
    return jsonify(influencers)

@app.route('/match', methods=['GET'])
def match_influencers():
    min_engagement = float(request.args.get('engagement', 0))
    matched = [i for i in influencers if i['engagement_rate'] >= min_engagement]
    return jsonify(matched)

@app.route('/add_influencer', methods=['POST'])
def add_influencer():
    new_influencer = request.json
    influencers.append(new_influencer)
    return jsonify({"message": "Influencer added successfully", "data": new_influencer}), 201

@app.route('/brand_match', methods=['GET'])
def brand_match():
    min_audience = int(request.args.get('audience', 0))
    matched = [i for i in influencers if i['audience'] >= min_audience]
    return jsonify({"matched_influencers": matched})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
