import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):       
        self.conn = sqlite3.connect(self.db_name)
        print("[INFO] Database connection opened.")
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):    
        if exc_type:
            print(f"[ERROR] An exception occurred: {exc_value}")            
        if self.conn:
            self.conn.close()
            print("[INFO] Database connection closed.")        
        return False



with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
