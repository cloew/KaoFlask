from .route_like import route_like

from kao_decorators import proxy_for

@proxy_for('routes', ['__iter__'])
class Routes:
    """ Represents a container of Routes that implements the Route Interface """
    
    def __init__(self, *routes):
        """ Initialize with any number of routes """
        self.routes = []
        self.add(routes)
            
    def add(self, *routes):
        """ Add the given routes """
        for route in routes:
            if route_like(route):
                self.routes.append(route)
            else:
                self.routes.extend(route)
            
    def register(self, app):
        """ Register the routes with the given app """
        for route in self.routes:
            route.register(app)