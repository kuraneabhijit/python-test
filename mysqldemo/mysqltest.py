import mysql.connector 
try:
    # db connection
    mydb=mysql.connector.connect(host='localhost', user='root', password='root1234',database='python_demo')
    cur=mydb.cursor()

    #create table
    cur.execute('CREATE TABLE IF NOT EXISTS STUDENT (student_id integer(4), name varchar(20))')

    #insert row
    student_info=(1,'Abhijit Kurane')
    cur.execute('INSERT INTO STUDENT (student_id,name) VALUES (%s,%s)',student_info)

    #insert mutliple rows
    multiple_student_info=[(2,'Abhijit Kurane 2'), (3,'Abhijit Kurane 3'), (4,'Abhijit Kurane 4')]
    cur.executemany('INSERT INTO STUDENT (student_id,name) VALUES (%s,%s)',multiple_student_info)


    #get rows(tuples) in table
    cur.execute("SELECT * FROM STUDENT")
    result=cur.fetchall()
    for rec in result:
        print(rec[1])



    mydb.commit()
    cur.close()
except Exception as e:
    print("exception caught::",e)
