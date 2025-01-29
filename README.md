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

---

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

## License

This project is licensed under the **MIT License**.
