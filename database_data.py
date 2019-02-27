def list_of_details(connection):
    cursor = connection.cursor()
    cursor.execute("select * from ")
    connection.commit()
    cursor.close()
