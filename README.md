# HNG Stage 0 Backend Task

This is a simple Flask API developed as part of the HNG Stage 0 Backend Task. The API returns basic information in JSON format, including:
- The registered email address.
- The current datetime in ISO 8601 format (UTC).
- The GitHub URL of the project's codebase.

## API Documentation

### Endpoint
- **URL**: `https://task0-api.onrender.com`
- **Method**: `GET`

### Response Format
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/mumiaktech/Task0-API"
}
```

### Example Usage
You can test the API using `curl` or a web browser:
```bash
curl https://task0-api.onrender.com
```

### Setup Instructions
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mumiaktech/Task0-API.git
   cd Task0-API
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **Test the API**:
   Open your browser or use `curl` to visit:
   ```
   http://127.0.0.1:5000/
   ```

## Backlink
- [Hire Python Developers](https://hng.tech/hire/python-developers)
