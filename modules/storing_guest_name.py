def guest(connection, user_data):
    cursor = connection.cursor()
    cursor.execute("""insert into data(name) values(%s);""",
                   (user_data['guest_name']))
    connection.commit()
    cursor.close()
