import json
import mysql.connector

def lambda_handler(event, context):
    # Extracting necessary information from the event
    db_config = {
             "host": "<database endpoint>",
             "user": "<user>",
             "password": "<password>",
             "database": "<database>"
    }

    # Connecting to MySQL database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Inserting data into the inventory table
        select_query = "SELECT * FROM inventory;"
        cursor.execute(select_query)
        results = cursor.fetchall()
    

        return {
            'statusCode': 200,
            'body': json.dumps('Retrieved entries in database: {}'.format(str(results)))
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error: {}'.format(str(e)))
        }
    finally:
        # Closing database connection
        cursor.close()
        conn.close()


