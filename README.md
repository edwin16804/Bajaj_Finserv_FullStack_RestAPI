# Bajaj Finserv FullStack REST API

A FastAPI-based REST API that processes input data arrays and categorizes elements while performing various transformations.

## Features

- **Data Processing**: Categorizes input elements into odd numbers, even numbers, alphabets, and special characters
- **Mathematical Operations**: Calculates sum of all numeric elements
- **String Transformations**: Applies alternating case transformation to concatenated alphabetic strings
- **RESTful API**: Clean POST endpoint for data processing

## API Endpoint

### POST `/bfhl`

Processes an array of data and returns categorized results.

**Request Body:**
```json
{
    "data": ["string1", "string2", "123", "456", "abc", "def", "!@#"]
}
```

**Response:**
```json
{
    "is_success": true,
    "user_id": "john_doe_17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123",
    "odd_numbers": ["123"],
    "even_numbers": ["456"],
    "alphabets": ["ABC", "DEF"],
    "special_characters": ["!@#"],
    "sum": "579",
    "concat_string": "cBa"
}
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Bajaj_Finserv_FullStack_RestAPI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Server

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application:**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - ReDoc documentation: http://localhost:8000/redoc

### Production Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Testing

### Using curl
```bash
curl -X POST "http://localhost:8000/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["123", "456", "abc", "def", "!@#"]}'
```

### Using Python requests
```python
import requests

url = "http://localhost:8000/bfhl"
data = {"data": ["123", "456", "abc", "def", "!@#"]}
response = requests.post(url, json=data)
print(response.json())
```

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running FastAPI applications
- **typing-extensions**: Extended typing support

## Project Structure

```
Bajaj_Finserv_FullStack_RestAPI/
├── main.py              # FastAPI application and API endpoints
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Data Processing Logic

1. **Numeric Elements**: Separated into odd and even numbers, summed together
2. **Alphabetic Elements**: Converted to uppercase and concatenated
3. **Special Characters**: Identified and collected separately
4. **String Transformation**: Concatenated alphabetic string is reversed and converted to alternating case


