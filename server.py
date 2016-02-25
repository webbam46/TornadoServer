import tornado.httpserver
import tornado.ioloop
import tornado.web
import socket
from stock import Stock


s = None

class Database(tornado.web.RequestHandler):
	def delete(self):
		s = Stock()
		self.write("OK")
		s.Close()
	def get(self):
		s = Stock()
		self.write("OK")
		s.Close()

class Bat(tornado.web.RequestHandler):
	def put(self):
		try:
			s = Stock()
			price = self.get_argument('price','')
			quantity = self.get_argument('quantity','')
			if(price!=''):
				s.setBatPrice(float(price))
				
			if(quantity!=''):
				s.setBatQuantity(int(quantity))
			self.write("OK")
		except Exception as e:
			print(e)

	def get(self):
		try:
			s = Stock()
			#Check for price/quantity
			reply = ""
			price = self.get_argument('price','')
			quantity = self.get_argument('quantity','')
			value = self.get_argument('value','')
			if(price=='true'):
				#Get the bat unit price
				price = s.getItemPrice('bat')
				reply += "bat unit price: " + str(price)
			if(quantity=='true'):
				#Get the bat quantity
				quantity = s.getItemQuantity('bat')
				reply += "bat stock level: " + str(quantity)
			if(value=='true'):
				#Get item total value
				total = s.getItemTotal('bat')
				reply += "bat total stock value: " + str(total)
			if(reply==""):
				reply = "OK"
			self.write(reply)
			s.Close()
		except Exception as e:
			print(e)
class Egg(tornado.web.RequestHandler):
	def put(self):
		try:
			s = Stock()
			price = self.get_argument('price','')
			quantity = self.get_argument('quantity','')
			if(price!=''):
				s.setEggPrice(float(price))
			if(quantity!=''):
				s.setEggQuantity(int(quantity))
			self.write("OK")
		except Exception as e:
			print(e)	
	
	def get(self):
		try:
			s = Stock()
			reply = ""
			#Check for price/quantity
			price = self.get_argument('price','')
			quantity = self.get_argument('quantity','')
			value = self.get_argument('value','')
			if(price=='true'):
				#Get the egg unit price
				price = s.getItemPrice('egg')
				reply += "egg unit price: " + str(price)
			if(quantity=='true'):
				quantity = s.getItemQuantity('egg')
				reply += "egg stock level: " + str(quantity)
			if(value=='true'):
				#Get item total value
				total = s.getItemTotal('egg')
				reply += "egg total stock value: " + str(total)
			if(reply==""):
				reply = "OK"
			self.write(reply)
			s.Close()
		except Exception as e:
			print(e)


application = tornado.web.Application([
	(r"/database",Database),
	(r"/item/bat",Bat),
	(r"/item/egg",Egg)
])

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(43210) #Server port
	print("Starting server")
	print("PORT: 43210")
	tornado.ioloop.IOLoop.instance().start()
	
