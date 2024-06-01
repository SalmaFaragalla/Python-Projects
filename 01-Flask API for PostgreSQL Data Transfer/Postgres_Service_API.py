from flask import Flask, request, jsonify
import psycopg2
import json

############################################# PostgreSQL Python Main #################################################
class Database:
    def __init__(self, db_name, db_user, db_password, db_host="localhost", db_port="5432"):
        """
        Initializes the database connection details.

        Args:
            db_name (str): Name of the database to connect to.
            db_user (str): Username for database access.
            db_password (str): Password for database access.
            db_host (str, optional): Hostname of the database server. Defaults to "localhost".
            db_port (str, optional): Port number of the database server. Defaults to "5432".
        """
        self.name = db_name
        self.user = db_user
        self.password = db_password
        self.host = db_host
        self.port = db_port
        self.conn = None
        self.cursor = None
        self.records = []
        self.__ConnectToServer()

    def __ConnectToServer(self):
        """
        Connect to the PostgreSQL database server.

        Raises:
            Exception: If there is an error connecting to the database.
        """
        try:
            self.conn = psycopg2.connect(database=self.name, user=self.user, password=self.password, host=self.host, port=self.port)
            self.cursor = self.conn.cursor()
            print("Connected to PostgreSQL database.")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def __ExecuteQuery(self, query, params = None, fetch = False):
        """
        Execute a SQL query on the connected PostgreSQL database.

        Args:
            query (str): The SQL query to be executed.
            params (tuple, optional): The parameters to be used with the SQL query.
            fetch (bool, optional): Whether to fetch and print the results of the query. Defaults to False.

        Returns:
            list: The fetched data from the executed query if fetch is True.

        Raises:
            Exception: If not connected to the database or if there is an error executing the SQL query.
        """
        if not self.conn:
            raise Exception("Not connected to database!")
        try:
            self.cursor.execute(query, params or [])
            self.conn.commit()
            if (fetch):
                self.records = self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print(f"Error executing SQL: {e}")
    
    def Select(self):
        """
        Executes a SELECT query on the database.

        Args:
            query (str): The SELECT query to be executed.

        Returns:
            list: The fetched records.
        """
        self.__ExecuteQuery("SELECT * FROM actor LIMIT 10;",fetch= True)
        return self.records
    
    def Insert(self,records):
        """
        Executes an INSERT query on the database.

        Args:
            records (list): List of records to be inserted.
    """
        for record in records:
            self.__ExecuteQuery("INSERT INTO actor (actor_id, first_name, last_name) VALUES (%s, %s, %s);" , record)
    

    def RecordsToJSON(self):
        column_names = ("actor_id", "first_name", "last_name", "last_update")
        records_list = [dict(zip(column_names, row)) for row in self.records]
        output = {
        "message": "Records Inserted.",
        "status": "success",
        "data": records_list
        }
        return json.dumps(output, indent=4)
    
    def Close(self):
        """
        Close the cursor and the connection to the PostgreSQL database.

        Raises:
            Exception: If there is an error closing the database connection.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print("Database connection closed.")
        except Exception as e:
            print(f"Error closing the database connection: {e}")   
    
def PostgreSQL_Python_Service_Main():
    db1 = Database(db_name = "dvdrental", db_user = "postgres" ,db_password = "salma" )
    db2 = Database(db_name = "dvdrentalinsert", db_user = "postgres" ,db_password = "salma" )

    db1_records = db1.Select()
    db2.Insert(db1_records)
    
    db1.Close()
    db2.Close()

    return db1.RecordsToJSON()

############################################# PostgreSQL Python API #################################################
# Create a Flask application instance
app = Flask(__name__)

# Define a route for POST requests at the root URL "/"
@app.route("/transfer-records", methods=["POST"])
def PostgreSQL_Python_Service():
    # Call the function to handle PostgreSQL service and get records in JSON format
    recordsJSON = PostgreSQL_Python_Service_Main()
    #Return the records JSON along with HTTP status code 201 (Created)
    return  recordsJSON , 201

if __name__ == "__main__":
    # Enable debugging mode for development
    app.run(debug = True)

