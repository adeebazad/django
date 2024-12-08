import oracledb

# Set up the connection details
dsn = '(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-mumbai-1.oraclecloud.com))(connect_data=(service_name=g17250c9acce4ce_admin_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'  # SID or Service Name
connection = oracledb.connect(user='ADMIN', password='RussAdeeb@123', dsn=dsn)

# Create a cursor to interact with the database
cursor = connection.cursor()

# Example query
cursor.execute("SELECT * FROM Persons")
cursor.fetchall

# Fetch and display results
print(cursor)

# Close the cursor and connection
cursor.close()
connection.close()



