import psycopg2
from config import DB_CONFIG

def insert_candidate(name, skills, education):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO candidates (name, skills, education)
        VALUES (%s, %s, %s)
    """, (name, ', '.join(skills), ', '.join(education)))
    conn.commit()
    cur.close()
    conn.close()