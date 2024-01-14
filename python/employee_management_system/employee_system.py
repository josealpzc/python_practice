import mysql.connector

def start_connection(pswd):
    return mysql.connector.connect(user='root',host='127.0.0.1',password=pswd,database='employees')
    #print(cnx)
    
#This function verifies if a given id corresponds to an employee.
def check_employee(employee_id):
    sql = 'select * from employee where id=%s'
    #c=cnx.cursor
    

def main():
    print('Welcome')
    pswd = input('Please enter your password for sql: ')
    cnx=start_connection(pswd)
    #check_employee(cnx)
    print(cnx)
    cnx.close()

if __name__ == '__main__':
    main()
