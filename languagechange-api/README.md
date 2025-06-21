# Language Change API

## Overview
The Language Change API is a simple web service that allows users to translate text between various languages. It supports multiple languages and provides an easy-to-use interface for language translation.

## Features
- Translate text from one language to another.
- Supports a wide range of languages.
- Easy integration with other applications.

## Technologies Used
- Python
- Flask (or FastAPI)
- googletrans

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd languagechange-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the API server:
   ```
   python src/main.py
   ```

2. Make a request to the translation endpoint. For example, using `curl`:
   ```
   curl -X POST http://localhost:8000/translate -H "Content-Type: application/json" -d '{"from": "English", "to": "French", "text": "Hello, world!"}'
   ```

3. The API will respond with the translated text.

## API Endpoints

### POST /translate
- **Description**: Translates text from one language to another.
- **Request Body**:
  ```json
  {
    "from": "source_language",
    "to": "target_language",
    "text": "text_to_translate"
  }
  ```
- **Response**:
  ```json
  {
    "translated_text": "translated_text_here"
  }
  ```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.