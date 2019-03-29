def madras_coffee_data(connection_coffee, user_data):
    cursor = connection_coffee.cursor()
    cursor.execute("""insert into final_report(employee_name, password) values(%s, %s);""",
                   (user_data['employee_name'], user_data['password']))
    connection_coffee.commit()
    cursor.close()