def list_of_details(connection_coffee):
    cursor = connection_coffee.cursor()
    cursor.execute("""insert into report(employee_name, password) values(%s, %s);""",
                   (user_data['employee_name'], user_data['password']))
    connection_coffee.commit()
    cursor.close()
