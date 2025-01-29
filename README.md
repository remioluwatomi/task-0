# Information Retrieval API

A public API that returns some of my information and current ISO 8601 timestamp in JSON format.

---

## Features

- Public API(GET) endpoint for retrieving information and current ISO 8601 timestamp.
- Information Retrieval in JSON format.
- CORS Handling - API handles Cross Origin Resources Sharing (CORS) Appropriately.

---

## Technologies Used

- **Python** proramming language.
- **FLASK framework** for building the API.
- **flask-cors** for handling CORS.
- **Swagger** for api documentation

---

## Screenshots

![Screenshot of the Swagger API docs](/app/static/Screenshot%202025-01-29%20025432.png)

![Screenshot of the Swagger API docs](/app/static/Screenshot%202025-01-29%20025549.png)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/remioluwatomi/task-0

   cd task-0

   ```

2. Create and Activate a Virtual Environment

   ```bash
    python -m venv venv

    # Activate virtual environment

    # Windows
    venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install requirements
   ```

4. Create a .env file in the project root and add the following environment variables:

   ```.env
    MY_EMAIL=the-email-to-be-retrieved
    GITHUB_REPO_URL=url-for-the-repo-being-retrieved
   ```

5. Start the development server::

   ```bash
   python run.py
   ```

   The API will be available at:

   ```bash
   http://127.0.0.1:5000
   ```

   ```bash
   #docs
   http://127.0.0.1:5000/docs
   ```

## Endpoints

### `GET /`

Accepts GET request and returns the required JSON response.

### Response:

- Success:

```json
{
  "email": "hng@gmail.com",
  "current_datetime": "2025-01-29T14:30:45Z",
  "github_url": "https://github.com/username/repo"
}
```

## Disclaimer:

This project is my submssion to HNG task-0.

## Back Links

[![Python Developers](https://img.shields.io/badge/Hire_Python_Developers-3030e6?style=for-the-badge)](https://hng.tech/hire/python-developers)  
[![C# Developers](https://img.shields.io/badge/Hire_C%23_Developers-2390c5?style=for-the-badge)](https://hng.tech/hire/csharp-developers)  
[![PHP Developers](https://img.shields.io/badge/Hire_PHP_Developers-6e7c00?style=for-the-badge)](https://hng.tech/hire/php-developers)  
[![GoLang Developers](https://img.shields.io/badge/Hire_GoLang_Developers-00a9ff?style=for-the-badge)](https://hng.tech/hire/golang-developers)  
[![Java Developers](https://img.shields.io/badge/Hire_Java_Developers-f4a261?style=for-the-badge)](https://hng.tech/hire/java-developers)  
[![Node.js Developers](https://img.shields.io/badge/Hire_Node.js_Developers-42b883?style=for-the-badge)](https://hng.tech/hire/nodejs-developers)

## License

This project is licensed under the **MIT License**.
