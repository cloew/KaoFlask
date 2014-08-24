from flask import Flask

class Server:
    """ Represents the Flask Server """
    
    def __init__(self, name, routes=[]):
        """ Initialize the Server """
        self.app = Flask(name)
        self.routes = routes
        self.applyRoutes()
        
    def run(self, debug=False):
        """ Run the server """
        self.app.run(debug=debug)
        
    def applyRoutes(self):
        """ Apply the routes to the server """
        for route in self.routes:
            route.addToServer(self.app)