import mysql.connector
from getpass import getpass

#This functions starts the connection to mysql server
def start_connection(pswd):
    return mysql.connector.connect(user='root',host='127.0.0.1',password=pswd,database='employees')
    #print(cnx)
    
#This function verifies if a given id corresponds to an employee.
def check_employee(employee_id):
   sql = 'select * from employee where id=%s'

def main():
    
    print('Welcome')
    password = getpass()
    
    #cnx is the connection object.
    cnx=start_connection(password)
    
    sql = 'select * from employee where id=%s'
    c = cnx.cursor(buffered=True)
    
    for i in range (0,7):
        data = (i,)
        c.execute(sql,data)
        r = c.rowcount

        if r == 1:
            flag = True

        else:
            flag = False

        print(f"Flag: {flag}")

    print(cnx)
    cnx.close()

if __name__ == '__main__':
    main()
