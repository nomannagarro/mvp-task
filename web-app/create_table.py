import pymysql

def create_table():
    rds_host = get_rds_endpoint()
    db_name = "mydatabase"
    username = "admin"
    password = "password"
        
    try:
        conn = pymysql.connect(host=rds_host, user=username, passwd=password, db=db_name)
        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Check if the table exists
        query = "SHOW TABLES LIKE 'file_record'"
        cursor.execute(query)

        if cursor.fetchone() is None:
            # Table doesn't exist, create it
            create_query = """
            CREATE TABLE file_record (
                File_Name VARCHAR(255),
                No_Of_Letters INT
            )
            """
            cursor.execute(create_query)
            print("Table 'file_record' created successfully.")
        else:
            print("Table 'file_record' already exists.")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


create_table()