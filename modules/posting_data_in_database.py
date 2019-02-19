def posting_data(connection, user_data):
    cursor = connection.cursor
    cursor.execute("""insert into employee_details(nam, employee_id) values(%s, %s);""",
                   (user_data['nam'], user_data['employee_id']))
    connection.commit()
    cursor.close()
