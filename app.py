import os
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the API endpoint
@app.route('/', methods=['GET'])
def get_info():
    email = "akoth0mitch@gmail.com"
    current_datetime = datetime.utcnow().isoformat() + "Z"
    github_url = "https://github.com/mumiaktech/Task0-API"

    return jsonify({
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    })

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
