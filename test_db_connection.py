from src.database.connection import get_connection

try:
    connection = get_connection()

    print("✅ Connected to PostgreSQL successfully!")

    connection.close()

except Exception as e:
    print("❌ Connection failed!")
    print(e)