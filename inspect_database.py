import sqlite3
import os

# Path to the database file
DB_FILE = os.path.join(os.path.dirname(__file__), "Stock-Screener", "Streamlit_Dashboard", "utils", "users.db")

def list_users():
    """Reads the users table and prints registered accounts."""
    if not os.path.exists(DB_FILE):
        print(f"Database file not found at: {DB_FILE}")
        print("Make sure you have run the Streamlit app at least once to initialize the database.")
        return

    try:
        conn = sqlite3.connect(DB_FILE)
        # Using row_factory to access columns by name
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT username, created_at FROM users ORDER BY created_at DESC")
        rows = cursor.fetchall()
        
        print("\n" + "="*50)
        print(f"{'REGISTERED USERS':^50}")
        print("="*50)
        print(f"{'Username':<25} | {'Registration Date (UTC)':<20}")
        print("-"*50)
        
        for row in rows:
            print(f"{row['username']:<25} | {row['created_at']:<20}")
            
        print("="*50)
        print(f"Total Users: {len(rows)}")
        print("="*50 + "\n")
        
        conn.close()
    except Exception as e:
        print(f"Error reading database: {e}")

if __name__ == "__main__":
    list_users()
