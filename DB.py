import sqlite3
import OCR
obj = OCR.chooseImg()
#conn = sqlite3.connect("DB.db")
#c = conn.cursor()


#create new table
"""c.execute('''create table medcine
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             name text not null,
             price int not null,
             quantaty int );''')
 """
 
#insert Panadol to table
#c.execute('insert into medcine (name, price, quantaty) values ("Panadol", 15, 20)')

#insert catafast to table
#c.execute('insert into medcine (name, price, quantaty) values ("Catafast", 20, 30)')

#Add new medcine
def addNewMedcine(name, price, quantaty):
	conn = sqlite3.connect("DB.db")
	c = conn.cursor()
	
	c.execute('insert into medcine (name, price, quantaty) values (:name, :price, :quan)',{
	
																	'name':name,
																	'price':price,
																	'quan':quantaty	})
	
	
	# commit changes
	conn.commit()

	# close connection
	conn.close()
	print("the {} of {} is added with {} $ ".format(quantaty, name, price))

	
#view all data
def showData():
	conn = sqlite3.connect("DB.db")
	c = conn.cursor()
	c.execute('select * from medcine')
	records = c.fetchall()
	print_records = ''
	for record in records:
		print_records += str(record[0]) + "\t " + str(record[1]) + "\t" + str(record[2]) + "\t"+str(record[3]) + " \n"
	print("ID\t Name\t\tPrice\tQuantaty")
	print(print_records)
	 # commit changes
	conn.commit()

	# close connection
	conn.close()
'''
re = obj.cheack()
def despatchingProcess(re):
	conn = sqlite3.connct("DB.db")
	c = conn.cursor()
	if re == 1:
		c.execute("UPDATE medcine SET quantaty = quantaty - 1 WHERE ID = :medcine",{
																			'medcine':re})	
	 # commit changes
	conn.commit()

	# close connection
	conn.close()
'''
