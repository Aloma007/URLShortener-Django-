# URL Shortener API 🔗

A RESTful API built with Python, Django, and Django REST Framework that allows users to shorten long URLs, manage their links, and track how many times a short URL has been accessed. 

This project was built as part of the [roadmap.sh backend developer track](https://roadmap.sh/projects/url-shortening-service).

## Features

*   **Create:** Submit a long URL and receive a randomly generated 6-character short code.
*   **Retrieve (Redirect):** Look up a short code to retrieve the original URL.
*   **Update:** Change the destination of an existing short code.
*   **Delete:** Remove a short code from the database.
*   **Analytics:** Track and view how many times a specific short URL has been accessed.

## 🛠️ Tech Stack

*   **Language:** Python
*   **Framework:** Django, Django REST Framework (DRF)
*   **Database:** SQLite (Default)
*   **Testing:** Thunder Client / Postman

## 💻 Local Setup and Installation

Follow these steps to get the project running on your local machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aloma007/URLShortener-Django-.git
   cd URLShortener-Django-
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The API will now be available at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Create a Short URL
*   **URL:** `/shorten`
*   **Method:** `POST`
*   **Body (JSON):**
    ```json
    {
      "url": "https://www.example.com/some/long/url"
    }
    ```
*   **Success Response:** `201 Created`

### 2. Retrieve Original URL
*   **URL:** `/shorten/<shortCode>`
*   **Method:** `GET`
*   **Description:** Returns the original URL and increments the access count by 1.
*   **Success Response:** `200 OK`

### 3. Update a Short URL
*   **URL:** `/shorten/<shortCode>`
*   **Method:** `PUT`
*   **Body (JSON):**
    ```json
    {
      "url": "https://www.example.com/some/updated/url"
    }
    ```
*   **Success Response:** `200 OK`

### 4. Delete a Short URL
*   **URL:** `/shorten/<shortCode>`
*   **Method:** `DELETE`
*   **Success Response:** `204 No Content`

### 5. Get URL Statistics
*   **URL:** `/shorten/<shortCode>/stats`
*   **Method:** `GET`
*   **Description:** Returns the URL data including the total `accessCount` without incrementing the tracker.
*   **Success Response:** `200 OK`

## Check out Live Web App below 👇🏽😇
https://urlshortener-django-frontend.vercel.app/

## 🤝 Contributing
Contributions, issues, and feature requests are kindly welcome! 

## License
Distributed under GPL-3.0 license | See LICENSE for more information.
