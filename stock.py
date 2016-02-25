import sqlite3
import os

class Stock:
	#Initialise
	def __init__(self):
		try:
			#If database has not already been created -- initialise
			if(self.Exists()==False):
				#Open the database
				self.db = sqlite3.connect('stock.db')
				#Init cursor
				self.cursor = self.db.cursor()
				#Attempt to create stocks table
				self.createTable()
				#Close db
				self.Close()
			#Else - dump
			else:
				#Open the database
				self.db = sqlite3.connect('stock.db')
				#Init cursor
				self.cursor = self.db.cursor()
				print("display")
				self.Reset()
				self.Close()
		except Exception as e:
			print("exception caught")
			print(e)
	#Return whether the database already exists
	def Exists(self):
		if(os.path.isfile("stock.db")):
			print("database already exists")
			return True
		else:
			print("database does not exist")
			return False

	#Create the stocks table
	def createTable(self):
		try:
			if(self.cursor!=None and self.db!=None):
				self.cursor.execute("CREATE TABLE stockData (name TEXT,price REAL,quantity INTEGER)")
				#Insert rows for given items
				#BAT
				self.cursor.execute("INSERT INTO stockData VALUES ('bat',0.0,0)")
				#EGGS
				self.cursor.execute("INSERT INTO stockData VALUES ('egg',0.0,0)")
				#Commit database changes
				self.db.commit()
				print("created stocks table")
			else:
				print("Unable to create table, cursor, or database is invalid")
		except Exception as e:

			print("exception caught")
			print(e)
	#Template function for appending a row depending on the item name
	def addItem(self,name,amount):
		try:
			if(self.cursor!=None and self.db!=None and name!=None and amount!=None):
				self.cursor.execute("UPDATE stockData SET quantity = quantity + " + str(amount) + " WHERE name = " + "'" + str(name) + "'")
				self.db.commit()
			else:
				print("null cursor, or db")
		except Exception as e:
			print("exception caught")
			print(e)
	#Template function for setting item price depending on item name
	def setItemPrice(self,name,price):
		try:
			if(self.cursor!=None and self.db!=None and name!=None and price!=None):
				self.cursor.execute("UPDATE stockData SET price = " + str(price) + " WHERE name = " + "'" + str(name) + "'")
				self.db.commit()
			else:
				print("null cursor, or db, or data")
		except Exception as e:
			print("exception caught")
			print(e)
	#Template function to set item quantity depending on item name
	def setItemQuantity(self,name,quantity):
		try:
			if(self.cursor!=None and self.db!=None and name!=None and quantity!=None):
				self.cursor.execute("UPDATE stockData SET quantity = " + str(quantity) + " WHERE name = " + "'" + str(name) + "'")
				self.db.commit()
			else:
				print("null cursor, or db, or data")
		except Exception as e:
			print("exception caught")
			print(e)
	#Template function for getting item quantity depending on given item name
	def getItemQuantity(self,name):
		try:
			if(self.cursor!=None and self.db!=None and name!=None):
				self.cursor.execute("SELECT quantity FROM stockData WHERE name = " + "'" + str(name) + "'")
				return self.cursor.fetchone()
			else:
				print("null cursor, or db, or data")
		except Exception as e:
			print("exception caught")
			print(e)
	
	#Template function for getting item price depending on given item name
	def getItemPrice(self,name):
		try:
			if(self.cursor!=None and self.db!=None and name!=None):
				self.cursor.execute("SELECT price FROM stockData WHERE name = " + "'" + str(name) + "'")
				return self.cursor.fetchone()
			else:
				print("null cursor,or db, or data")
		except Exception as e:
			print("exception caught")
			print(e) 
	#Set price of bat
	def setBatPrice(self,price):
		self.setItemPrice('bat',price)
	#Set price of egg
	def setEggPrice(self,price):
		self.setItemPrice('egg',price)
	#Set bat quantity
	def setBatQuantity(self,quantity):
		self.setItemQuantity('bat',quantity)
	#Set egg quantity
	def setEggQuantity(self,quantity):
		self.setItemQuantity('egg',quantity)
	#Add to bat quantity
	def addBat(self,amount):
		self.addItem('bat',amount)
	#Add to egg quantity
	def addEgg(self,amount):
		self.addItem('egg',amount)
	#Reset item data
	def Reset(self):
		self.setBatPrice(0.0) #Bat price
		self.setBatQuantity(0) #Bat quantity
		self.setEggPrice(0.0) #Egg price
		self.setEggQuantity(0) #Egg quantity
	#Close the stocks database
	def Close(self):
		try:
			if(self.db!=None):
				self.db.close()
		except Exception as e:
			print("exception caught")
			print(e)

if __name__ == "__main__":
	stock = Stock()
