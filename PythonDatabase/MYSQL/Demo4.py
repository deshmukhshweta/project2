import SathyaConnector as sathya
conn = sathya.my_db_connector()
if conn.is_connected():
    print("Connected")
    curs = conn.cursor()
    curs.execute("insert into employee values(101,'Naveen',1000,905249)")
    print("Data Inserted")
    conn.commit()
    conn.close()
else:
    print("Not Connected")
