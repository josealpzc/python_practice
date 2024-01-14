import mysql.connector

def start_connection(pswd):
    
    cnx = mysql.connector.connect(user='root',host='127.0.0.1',password=pswd,database='employees')
    print(cnx)
    cnx.close()

def main():
    print('Welcome')
    pswd = input('Please enter your password for sql: ')
    start_connection(pswd)

if __name__ == '__main__':
    main()
