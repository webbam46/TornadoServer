import tornado.httpserver
import tornado.ioloop
import tornado.web
import socket
from stock import Stock


s = None

class Database(tornado.web.RequestHandler):
	def get(self):
		s = Stock()
		self.write("OK")
		s.Close()

class Bat(tornado.web.RequestHandler):
	def get(self):
		try:
			s = Stock()
			#Check for price/quantity
			reply = ""
			price = self.get_argument('price','')
			quantity = self.get_argument('quantity','')
			value = self.get_argument('value','')
			if(price=='true'):
				reply += "Bat unit price: "
			elif(price!=''):
				reply += "Setting price"
			if(quantity=='true'):
				reply += "Bat quantity: "
			elif(quantity!=''):
				reply += "Setting quantity"
			if(reply==""):
				reply = "OK"
			self.write(reply)
			s.Close()
		except Exception as e:
			print(e)
class Egg(tornado.web.RequestHandler):
	def get(self):
		try:
			s = Stock()
			reply = ""
			#Check for price/quantity
			price = self.get_argument('price','')
			quantity = self.get_argument('quantity','')
			value = self.get_argument('value','')
			if(price=='true'):
				reply += "Egg unit price: "
			elif(price!=''):
				reply += "setting price"
			if(quantity=='true'):
				reply += "Egg quantity: "
			elif(quantity!=''):
				reply += "setting quantity"
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
	
