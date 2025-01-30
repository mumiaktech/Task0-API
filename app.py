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
    # Your registered email address
    email = "akoth0mitch@gmail.com"

    # Current datetime in ISO 8601 format (UTC)
    current_datetime = datetime.utcnow().isoformat() + "Z"

    # GitHub URL of the project's codebase
    github_url = "https://github.com/yourusername/your-repo"

    # Return the response as JSON
    return jsonify({
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)