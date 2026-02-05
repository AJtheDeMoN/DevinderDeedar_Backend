const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const path = require('path');

const app = express();
const port = 8000; // Django usually runs on 8000, but might conflict if both run. I'll stick to 8000 as requested "same exact backend", but user might want to run them simultaneously. I'll use 8000 but warn if it fails. Actually, I'll use 8001 to be safe or 8000 if they stop django. Let's use 8000 to match "exact backend".

app.use(cors({
    origin: [
        "https://devinder-deedar.vercel.app"
    ],
    methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    credentials: true
}));
app.use(express.json());

// Path to the existing Django SQLite database
const dbPath = path.resolve(__dirname, './db.sqlite3');
const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        console.error('Error opening database ' + dbPath + ': ' + err.message);
    } else {
        console.log('Connected to the SQLite database at ' + dbPath);
    }
});

// Helper to format content
const formatContent = (content) => {
    if (!content) return "";
    return content.replace(/`/g, "<p>");
};

// Routes

// Article List
app.get('/api/article/', (req, res) => {
    const sql = 'SELECT id, title_punjabi, title_english, book_punjabi, book_english, year FROM blog_article';
    db.all(sql, [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ articles: rows });
    });
});

// Article Detail
app.get('/api/article/:pk/', (req, res) => {
    const sql = 'SELECT * FROM blog_article WHERE id = ?';
    const params = [req.params.pk];
    db.get(sql, params, (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        if (!row) {
            res.status(404).json({ error: 'Article not found' });
            return;
        }
        const data = {
            id: row.id,
            title: row.title_punjabi,
            content: formatContent(row.content),
            author: row.author,
            year: row.year
        };
        res.json(data);
    });
});

// Story List
app.get('/api/story/', (req, res) => {
    const sql = 'SELECT id, title_punjabi, title_english, year FROM blog_story';
    db.all(sql, [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ stories: rows });
    });
});

// Story Detail
app.get('/api/story/:pk/', (req, res) => {
    const sql = 'SELECT * FROM blog_story WHERE id = ?';
    const params = [req.params.pk];
    db.get(sql, params, (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        if (!row) {
            res.status(404).json({ error: 'Story not found' });
            return;
        }
        const data = {
            id: row.id,
            title: row.title_punjabi,
            content: formatContent(row.content),
            author: row.author,
            year: row.year
        };
        res.json(data);
    });
});

// Prose List
app.get('/api/prose/', (req, res) => {
    const sql = 'SELECT id, content FROM blog_prose';
    db.all(sql, [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ proses: rows });
    });
});

// Activator
app.get('/api/activator/', (req, res) => {
    res.json({ ok: 'ok' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

// Keep alive
setInterval(() => {}, 1000);

