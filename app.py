from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'studentdb')
DB_USER = os.environ.get('DB_USER', 'misbah')
DB_PASS = os.environ.get('DB_PASS', 'Misbah123!')

def get_db():
    return psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name VARCHAR(100), score INTEGER)")
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, score FROM students ORDER BY id DESC")
    students = cur.fetchall()
    cur.close()
    conn.close()
    html = "<html><head><title>Student Records</title><style>body{font-family:sans-serif;max-width:600px;margin:40px auto;padding:0 20px}input{padding:8px;margin:4px;border:1px solid #ddd;border-radius:6px}button{padding:8px 16px;background:#185FA5;color:white;border:none;border-radius:6px;cursor:pointer}table{width:100%;border-collapse:collapse;margin-top:20px}th,td{padding:10px;border:1px solid #ddd;text-align:left}th{background:#f5f5f5}.del{background:#e53e3e;padding:4px 10px;font-size:12px}</style></head><body><h2>Student Records (EKS)</h2><form method='POST' action='/add'><input name='name' placeholder='Student name' required><input name='score' type='number' placeholder='Score' required><button type='submit'>Add Student</button></form><table><tr><th>ID</th><th>Name</th><th>Score</th><th>Action</th></tr>"
    for s in students:
        html += f"<tr><td>{s[0]}</td><td>{s[1]}</td><td>{s[2]}</td><td><form method='POST' action='/delete/{s[0]}'><button class='del'>Delete</button></form></td></tr>"
    html += "</table></body></html>"
    return html

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    score = request.form['score']
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, score) VALUES (%s, %s)", (name, score))
    conn.commit()
    cur.close()
    conn.close()
    return index()

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return index()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
