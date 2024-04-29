from flask import Flask, request, jsonify
from recommendation import get_recommendations
from login import validate_credentials
from flask_cors import CORS , cross_origin
import requests
import base64

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/recommend', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def recommend():
     # Get JSON data from the request body
    data = request.json
    
    # Extract category, user_id, and n_recommendations from the JSON data
    category = data.get('category')
    user_id = data.get('user_id')
    n_recommendations = data.get('n_recommendations')

    # Validate that all required fields are present
    if not all([category, user_id, n_recommendations]):
        return jsonify({'error': 'Category, user_id, and n_recommendations are required.'}), 400

    # Call the get_recommendations function with the extracted arguments
    recommended_items = get_recommendations(category, user_id, n_recommendations)
    
    # Fetch metadata for recommended items
    items_with_metadata = []
    for item in recommended_items:
        metadata = fetch_metadata(item['item_id'])
        item_with_metadata = {
            'item_id': item['item_id'],
            'similarity': item['similarity_percentage'],
            'metadata': metadata
        }
        items_with_metadata.append(item_with_metadata)


    
    response = jsonify({'user_id': user_id, 'recommended_items': items_with_metadata})
    return response, 200
   
    


# Login route
@app.route('/login', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# @cross_origin(origins='*')
def login():
    # Get user credentials from the POST request
    user_email = request.json.get('email')
    password = request.json.get('password')
    print(user_email,password)

    # Call the validation function from auth.py
    user_id = validate_credentials(user_email, password)

    if user_id is not None:
    #    response.headers.add("Access-Control-Allow-Origin", "*")
        response = jsonify({'user_id': user_id})
        #response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/metadata', methods=['POST'])
def recommend_items():
    # Assume you receive product IDs from the frontend
    products = request.json['product_ids']  # Adjust this to match your JSON structure
    print(products)
    # Fetch metadata for each product ID
    item_metadata = []
    for product in products:
        print(product)
        metadata = fetch_metadata(product['item_id'])
        item_metadata.append({
            'metadata': metadata
        })

    # Return the recommended products with metadata
    return jsonify(item_metadata)

def fetch_metadata(product_id):
    username = 'Siddik'
    password = 'Siddik_1234MM'
    url = f'https://realtime.oxylabs.io/v1/queries'

    body = {
        'source': 'amazon_product',
        'domain': 'com',
        'query': product_id,
        'parse': True,
        'context': [
            {'key': 'autoselect_variant', 'value': False},
        ],
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON data
        else:
            return None
    except Exception as e:
        print('Error fetching metadata:', e)
        return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000 ,debug=True)
