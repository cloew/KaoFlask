from .route_like import route_like
from flask import Flask

class Server:
    """ Represents the Flask Server """
    
    def __init__(self, name, config=None, routes=[], extensions=[]):
        """ Initialize the Server """
        self.app = Flask(name)
        if config is not None:
            self.app.config.from_object(config)
            
        for extension in extensions:
            extension.initialize(self)
        
        self.routes = routes
        self.applyRoutes()
        
    def run(self, **kwargs):
        """ Run the server """
        self.app.run(**kwargs)
        
    def applyRoutes(self):
        """ Apply the routes to the server """
        if route_like(self.routes):
            self.routes.register(self.app)
        else:
            for route in self.routes:
                route.register(self.app)