from flask import Flask, jsonify, request
from mlxtend.frequent_patterns import apriori
import pandas as pd
import logging

app = Flask(__name__)

# Dummy influencer data
influencers = [
    {"id": 1, "name": "Influencer A", "audience": 10000, "engagement_rate": 3.5},
    {"id": 2, "name": "Influencer B", "audience": 5000, "engagement_rate": 4.0},
    {"id": 3, "name": "Influencer C", "audience": 20000, "engagement_rate": 2.0},
]

logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    logging.info('Headers: %s', request.headers)
    logging.info('Body: %s', request.get_data())

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
    if not request.json or not all(key in request.json for key in ('id', 'name', 'audience', 'engagement_rate')):
        return jsonify({"error": "Missing or invalid data"}), 400

    new_influencer = request.json
    if any(i['id'] == new_influencer['id'] for i in influencers):
        return jsonify({"error": "Influencer with this ID already exists"}), 400

    influencers.append(new_influencer)
    return jsonify({"message": "Influencer added successfully", "data": new_influencer}), 201

@app.route('/update_influencer/<int:id>', methods=['PUT'])
def update_influencer(id):
    influencer = next((i for i in influencers if i['id'] == id), None)
    if influencer is None:
        return jsonify({"error": "Influencer not found"}), 404

    data = request.json
    if 'name' in data:
        influencer['name'] = data['name']
    if 'audience' in data:
        influencer['audience'] = data['audience']
    if 'engagement_rate' in data:
        influencer['engagement_rate'] = data['engagement_rate']

    return jsonify({"message": "Influencer updated successfully", "data": influencer})

@app.route('/delete_influencer/<int:id>', methods=['DELETE'])
def delete_influencer(id):
    global influencers
    influencers = [i for i in influencers if i['id'] != id]
    return jsonify({"message": "Influencer deleted successfully"})

@app.route('/brand_match', methods=['GET'])
def brand_match():
    min_audience = int(request.args.get('audience', 0))
    matched = [i for i in influencers if i['audience'] >= min_audience]
    return jsonify({"matched_influencers": matched})

@app.route('/apriori', methods=['GET'])
def run_apriori():
    try:
        # Convert influencer data to a DataFrame
        df = pd.DataFrame(influencers)

        # Binary conversion: check if audience and engagement_rate are above their respective means
        df_binary = pd.DataFrame({
            'audience_high': (df['audience'] > df['audience'].mean()).astype(int),
            'engagement_high': (df['engagement_rate'] > df['engagement_rate'].mean()).astype(int)
        })

        logging.info(f"Binary DataFrame for Apriori:\n{df_binary}")

        # Run Apriori algorithm
        frequent_itemsets = apriori(df_binary, min_support=0.1, use_colnames=True)

        # Convert the frozenset to a list for JSON serialization
        frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: list(x))

        # Check if any frequent itemsets were found
        if frequent_itemsets.empty:
            return jsonify({"message": "No frequent itemsets found"}), 200

        return jsonify(frequent_itemsets.to_dict(orient='records'))
    except Exception as e:
        logging.error(f"Apriori algorithm error: {e}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Exception: {e}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
