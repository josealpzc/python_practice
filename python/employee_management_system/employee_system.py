import mysql.connector
from getpass import getpass

connection = None 

#This functions starts the connection to mysql server
def start_connection(pswd):

    #The connect() constructor creates a connection to the MySQL server and return a MySQLConnection object.
    return mysql.connector.connect(user='root',host='127.0.0.1',password=pswd,database='employees')
    #print(cnx)
    
#This function verifies if a given id corresponds to an employee.
def check_employee(employee_id):
    #cursor method returns a MySQLCursor() object.
    cursor=connection.cursor()
    query = 'select * from employee where id=%s'
    data=(employee_id,)
    cursor.execute(query,data)
    print(cursor)

    for name in cursor:
        print(name)

def main():
    
    print('Welcome')
    password = getpass() 
    #starting connection to MySQL server
    global connection
    connection=start_connection(password)
    print(connection)
   
    check_employee(1)

    connection.close()

if __name__ == '__main__':
    main()
