import pymysql

# Database credentials
host_name='localhost'
port_id=3306
user_name='root'
user_password=''
database_name='learn_sql'

# Connect to database
conn = pymysql.connect(host=host_name, port=port_id, user=user_name, passwd=user_password, db=database_name)

# Establish connection
cur = conn.cursor()

# Execute queries
cur.execute("SELECT * FROM user_accounts")

# Print reuslt
#print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()