--== Task Description ==--

Cleaning user_item Table: The script deletes records from the user_item table that are older than 30 days, based on the createdAt timestamp.

Cleaning Item Table: After cleaning the user_item table, the script proceeds to delete records from the Item table that are no longer associated with any user_item records. This step ensures that the Item table only contains items that are in use or have been used within the last 30 days.

--== Execution Flow ==--

The script first establishes a connection to the PostgreSQL database using the credentials provided in the db_config dictionary.

Within a try block, the script executes two SQL DELETE operations inside a context manager that handles the database connection and cursor creation automatically, ensuring that resources are properly managed.
Successful execution of delete operations is followed by a commit to the database to ensure changes are saved.
If the script encounters any errors during execution, particularly when working with PostgreSQL, it catches these exceptions and prints an error message along with the current timestamp.

--== Error Handling ==--

The script includes basic error handling to catch and report any issues that occur during the database operations, specifically targeting exceptions thrown by the psycopg2 library. This approach ensures that any problems encountered are logged with a timestamp for easier debugging and maintenance.


Notice for CRON
> crontab -e
0 8 * * 0 /usr/bin/python3 /home/ubuntu/py_scripts/clean-stale-items-postgres.py > /home/ubuntu/py_scripts/cron.log 2>&1
