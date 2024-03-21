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

    data = event.get('data')

    # Connecting to MySQL database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Inserting data into the inventory table
        insert_query = "INSERT INTO inventory (store, item, quantity) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (data['store'], data['item'], data['quantity']))
        conn.commit()

        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully into the inventory table')
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

# Example event format:
# {
#     "data": {
#         "store": "Boston"   
#         "item": "Amazon Dot",
#         "quantity": 10
#     }
# }

