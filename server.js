// Shipyard test app: Node.js + Express, database through DATABASE_URL.
const express = require("express");
const mysql = require("mysql2/promise");

const app = express();
const pool = mysql.createPool(process.env.DATABASE_URL);

app.get("/", (req, res) => res.send("Hello from Node.js on Shipyard"));

app.get("/db", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT VERSION() AS version");
    res.json({ ok: true, version: rows[0].version });
  } catch (error) {
    res.status(500).json({ ok: false, error: error.message });
  }
});

app.listen(Number(process.env.PORT) || 3000, "0.0.0.0");
