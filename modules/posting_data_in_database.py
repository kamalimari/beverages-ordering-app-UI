def posting_data(connection, user_data):
    cursor = connection.cursor()
    cursor.execute("""insert into report(employee_name, password) values(%s, %s);""",
                   (user_data['employee_name'], user_data['password']))
    connection.commit()
    cursor.close()
