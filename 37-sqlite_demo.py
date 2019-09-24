import sqlite3

import employee

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')  #in memory db it for testing not throw any error

c = conn.cursor()

c.execute("""CREATE TABLE employees(first text,last text,pay integer)""")

c.execute("INSERT INTO employees VALUES ('ut','bhar',4000)")


emp1 = employee.Employee('sad', 'asdsa', 88900)
emp2 = employee.Employee('saddc', 'asacddsa', 88943500)

c.execute("INSERT INTO employees VALUES ('{}','{}',{})".format(emp1.first, emp1.last, emp1.pay))
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp1.first, emp1.last, emp1.pay))
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp1.first,'last':emp1.last,'pay':emp1.pay})
# print(c.fetchone())
# c.fetchmany(5) # number of row
# c.fetchall()
print(c.fetchone())

conn.commit()

c.execute("SELECT *  from employees")

print(c.fetchall())

conn.close()
#function context object it will not need to close conn
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES ('{}','{}',{})".format(emp1.first, emp1.last, emp1.pay))
