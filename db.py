import sqlite3

def init_db():
    conn = sqlite3.connect('vulnscanner.db')
    cursor = conn.cursor()

    # Create table for reports
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_type TEXT,
            target TEXT,
            raw_output TEXT,
            ai_summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def save_report(scan_type, target, raw_output, ai_summary):
    conn = sqlite3.connect('vulnscanner.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO reports (scan_type, target, raw_output, ai_summary)
        VALUES (?, ?, ?, ?)
    ''', (scan_type, target, raw_output, ai_summary))

    conn.commit()
    conn.close()

def get_reports():
    conn = sqlite3.connect('vulnscanner.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, scan_type, target, created_at FROM reports ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows
