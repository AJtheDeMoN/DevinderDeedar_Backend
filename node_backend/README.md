# Node.js Backend for DevinderDeedar

This is a Node.js implementation of the backend, replicating the functionality of the Django backend.
It uses the same SQLite database (`../backend/db.sqlite3`).

## Setup

1.  Navigate to this directory:
    ```bash
    cd node_backend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

## Running the Server

To start the server:

```bash
npm start
```

The server runs on port 8000 by default.
Ensure the Django server is not running on the same port, or change the port in `index.js`.

## Endpoints

*   `GET /api/article/` - List all articles
*   `GET /api/article/:id/` - Get article details
*   `GET /api/story/` - List all stories
*   `GET /api/story/:id/` - Get story details
*   `GET /api/prose/` - List all prose
*   `GET /api/activator/` - Health check
