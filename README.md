# 🔗 URL Shortener

A lightweight, production-conscious URL shortener built with **pure Python** and **PostgreSQL** — no web frameworks, no unnecessary dependencies. Just Python's standard library, `psycopg2`, and a clean architecture.

---

## 🧠 Philosophy

Most URL shorteners are built on top of heavy frameworks. This one is different — it uses Python's built-in `http.server` module to handle HTTP from scratch, giving you full visibility into how the web actually works under the hood.

---

## ✨ Features

- 🔐 **SQL Injection Protection** — Parameterized queries throughout
- ♻️ **Collision Handling** — Short code uniqueness is guaranteed before saving
- 🌍 **Environment-Based Configuration** — No hardcoded values anywhere
- 🧱 **Zero Framework Dependencies** — Pure Python standard library for HTTP
- 🐘 **PostgreSQL** — Production-grade relational database
- 🔁 **301 Redirects** — Industry-standard permanent redirects

---

## 🗂️ Project Structure

```
url_shortener/
│
├── main.py          # Entry point — starts the HTTP server
├── handler.py       # Request handler — routing, requests, responses
├── db.py            # Database layer — connection, queries
├── shortener.py     # Short code generation and collision checking
├── .env             # Environment variables (never commit this)
├── .gitignore       # Ignores .env and venv
└── README.md        # You are here
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| HTTP Server | `http.server` (Standard Library) |
| Database | PostgreSQL 18 |
| DB Driver | `psycopg2-binary` |
| Configuration | `python-dotenv` |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL (via [Postgres.app](https://postgresapp.com) or any installation)

---

### 1. Clone the Repository

```bash
git clone https://github.com/shanAweb/URL-Shortenere-with-Python-Postgress.git
cd URL-Shortenere-with-Python-Postgress
```

---

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install psycopg2-binary python-dotenv
```

---

### 4. Set Up PostgreSQL

Start your PostgreSQL server and run the following:

```bash
psql -p 5433 -U your_username -d postgres
```

```sql
CREATE DATABASE url_shortener;
\c url_shortener

CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 5. Configure Environment Variables

Create a `.env` file in the root of the project:

```env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=url_shortener
DB_USER=your_username
DB_PASSWORD=

HOST=localhost
PORT=8080
BASE_URL=http://localhost:8080
```

---

### 6. Run the Server

```bash
python main.py
```

You should see:
```
Server running on http://localhost:8080
```

---

## 🧪 Testing the API

### Shorten a URL

```bash
curl -X POST http://localhost:8080/shorten \
-H "Content-Type: application/json" \
-d '{"original_url": "https://www.google.com"}'
```

**Response:**
```json
{
    "short_url": "http://localhost:8080/aB3kP9"
}
```

---

### Redirect to Original URL

```bash
curl -L http://localhost:8080/aB3kP9
```

Or simply paste `http://localhost:8080/aB3kP9` into your browser — it will redirect you automatically.

---

### API Reference

| Method | Endpoint | Body | Description |
|---|---|---|---|
| `POST` | `/shorten` | `{"original_url": "..."}` | Shortens a long URL |
| `GET` | `/<short_code>` | None | Redirects to original URL |

---

### HTTP Status Codes

| Code | Meaning |
|---|---|
| `200` | URL shortened successfully |
| `301` | Redirect to original URL |
| `400` | Bad request — missing or invalid URL |
| `404` | Short code not found |
| `500` | Internal server error |

---

## 🏗️ Architecture

```
Client Request
      │
      ▼
  main.py  ──────────────────── Starts HTTPServer on configured host/port
      │
      ▼
 handler.py ─────────────────── Receives all HTTP requests
      │
      ├── do_POST()  ─────────── Handles POST /shorten
      │       │
      │       ├── shortener.py ── Generates unique short code
      │       └── db.py ───────── Saves original_url + short_code
      │
      └── do_GET()  ──────────── Handles GET /<short_code>
              │
              └── db.py ───────── Looks up short_code → redirects
```

---

## 🔒 Security Considerations

- All SQL queries use **parameterized placeholders** (`%s`) to prevent SQL injection
- Credentials are stored in `.env` and never hardcoded
- `.env` is listed in `.gitignore` and never committed to version control

---

## 🛣️ Roadmap

- [ ] Click counter — track visits per short URL
- [ ] URL expiry — short URLs that expire after a set time
- [ ] Custom short codes — let users define their own alias
- [ ] Duplicate detection — return existing short code for duplicate URLs
- [ ] HTML frontend — browser-based form for submitting URLs

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Author

Built with 💻 and curiosity by **Shan**