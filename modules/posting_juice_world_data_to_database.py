def juice_world_data(connection_juice, user_data):
    cursor = connection_juice.cursor()
    cursor.execute("""insert into report(employee_name, password) values(%s, %s);""",
                   (user_data['employee_name'], user_data['password']))
    connection_juice.commit()
    cursor.close()
