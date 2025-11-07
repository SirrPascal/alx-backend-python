import sqlite3
import functools


def log_queries(func):
    @functools.wraps(func)
    def
        query = args[0] if args else kwargs.get('query', None)
        if query:
            print(f"Executing SQL Query: {query}")
        else:
            print("No SQL query found to execute.")
       
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


users = fetch_all_users(query="SELECT * FROM users")
print(users)
