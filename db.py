import sqlite3

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_query(conn, query, params=()):  # Added params for parameterized queries
    """Execute a SQL query."""
    try:
        c = conn.cursor()
        c.execute(query, params)  # Use params for parameterized queries
        conn.commit()
        return c.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def list_tables(conn):
    """List all tables in the database."""
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    result = execute_query(conn, query)
    if result:
        for table in result:
            print(f"- {table[0]}")
    else:
        print("No tables found.")

def show_table_data(conn, table_name):
    """Show data from a table."""
    query = f"SELECT * FROM {table_name};"
    result = execute_query(conn, query)
    if result:
        cursor = conn.cursor()
        cursor.execute(query)
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for row in result:
            print(row)
    else:
        print(f"Table '{table_name}' is empty or doesn't exist.")

def add_record(conn, table_name, data):  # data is a dictionary
    """Add a record to a table."""

    try:
      placeholders = ", ".join(["?"] * len(data))
      columns = ", ".join(data.keys())
      query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
      execute_query(conn, query, tuple(data.values()))
      print("Record added successfully.")
    except Exception as e:
      print(f"Error adding record: {e}")


def remove_record(conn, table_name, condition):
    """Remove a record from a table based on a condition."""
    query = f"DELETE FROM {table_name} WHERE {condition};"
    execute_query(conn, query)
    print("Record(s) removed successfully.")

def clear_table(conn, table_name):
    """Clear all data from a table."""
    query = f"DELETE FROM {table_name};"
    execute_query(conn, query)
    print("Table cleared successfully.")


def main():
    database = "db.sqlite3"
    conn = create_connection(database)

    if conn:
        while True:
            print("\nDatabase Operations Menu:")
            print("1. List tables")
            print("2. Show table data")
            print("3. Add record")
            print("4. Remove record")
            print("5. Clear table")
            print("6. Exit")

            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    list_tables(conn)
                elif choice == '2':
                    table_name = input("Enter table name: ")
                    show_table_data(conn, table_name)
                elif choice == '3':
                    table_name = input("Enter table name: ")
                    # Get column names (improve this if you have a lot of columns)
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT * FROM {table_name} LIMIT 0;") #Select 0 rows to get column names
                    column_names = [description[0] for description in cursor.description]

                    data = {}
                    print("Enter data (type 'exit' to finish):")
                    for col in column_names:
                        value = input(f"{col}: ")
                        if value.lower() == 'exit':
                            break
                        data[col] = value
                    if data: #If the user entered data
                        add_record(conn, table_name, data)
                elif choice == '4':
                    table_name = input("Enter table name: ")
                    condition = input("Enter condition for removal (e.g., id=5): ")
                    remove_record(conn, table_name, condition)
                elif choice == '5':
                    table_name = input("Enter table name: ")
                    clear_table(conn, table_name)
                elif choice == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                conn.commit() #Commit after each operation to make sure data is saved

        conn.close()


if __name__ == "__main__":
    main()