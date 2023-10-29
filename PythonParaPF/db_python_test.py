import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root", #O seu nome de usuario certamente eh root
  password="1234" #Aqui voce devera digitar a senha que voce criou ao baixar o MySQL
)

crs = mydb.cursor()
execsqlcmd = lambda cmd, crs: crs.execute (cmd)
execcreatetable = lambda table, attrs, crs : execsqlcmd ("CREATE TABLE " + table + " (" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname, crs : execsqlcmd ("CREATE DATABASE " + dbname + ";\n", crs)
execdropdatabase = lambda dbname, crs : execsqlcmd ("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda dbname, crs : execsqlcmd ("DROP TABLE " + dbname + ";\n", crs)
execusedatabase = lambda dbname, crs : execsqlcmd ("USE " + dbname + ";\n", crs)
execselectfromwhere = lambda attrs, table, wherecond, crs : execsqlcmd ("SELECT " + attrs + " FROM " + table + " WHERE " + wherecond + ";", crs)
execinsertinto = lambda table, attrs, values, crs : execsqlcmd ("INSERT INTO " + table + " (" + attrs + ")" + " VALUES (" + values + ");", crs)

#"CREATE DATABASE mydatabase"
execcreatedatabase ("mydatabase", crs)

#"USE DATABASE mydatabase"
execusedatabase ("mydatabase", crs)

#"CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
execcreatetable ("customers", "name VARCHAR (255) , address VARCHAR (255)", crs)

#"INSERT INTO ... VALUES ..."
execinsertinto ("customers", "name , address", "'Ascleps', 'Rua Bledorns do Bacchi 444'", crs)

#"SELECT * FROM customers"
execselectfromwhere ("*", "customers", "true", crs)

res = crs.fetchall ()
print_result = lambda res : [print (x) for x in res]

print_result (res)

execdroptable ("customers", crs)
execdropdatabase ("mydatabase", crs)
