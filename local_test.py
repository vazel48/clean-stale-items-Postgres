import psycopg2
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

db_config = {
    "dbname": "ubf1",
    "user": "postgres",
    "password": "mysecretpassword",
    "host": "localhost",
    "port": "5432"
}

try:
    with psycopg2.connect(**db_config) as connection:
        with connection.cursor() as cursor:
            # Removing records older than 30 days from "user_item" table
            cursor.execute("""
            DELETE FROM user_item
            WHERE "createdAt" < now() - INTERVAL '30 days';
            """)
            connection.commit()  # Make sure the changes are committed before proceeding

            # Removing unused records from "Item" table
            cursor.execute("""
            DELETE FROM "Item"
            WHERE NOT EXISTS (
                SELECT 1
                FROM user_item
                WHERE user_item."itemID" = "Item"."itemID"
            );
            """)
            connection.commit()

    print(f"{current_time} - Delete requests completed successfully.")

except psycopg2.Error as e:
    print(f"{current_time} - Error when working with PostgreSQL: {e}")


