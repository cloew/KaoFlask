from .endpoint_like import endpoint_like
from .nested import NestedRoutes

from kao_decorators import proxy_for

@proxy_for('endpoints', ['__iter__'])
class Routes:
    """ Represents a container of Route Endpoints that can add nested Route Endpoints """
    
    def __init__(*endpoints):
        """ Initialize with any number of Endpoints """
        self.endpoints = []
        self.nestedRoutes = {}
        self.add(endpoints)
            
    def add(self, *endpoints):
        """ Add the given endpoints """
        for endpoint in endpoints:
            if endpoint_like(endpoint):
                self.endpoints.append(endpoint)
            else:
                self.endpoints.extend(endpoint)
            
    def nest(self, prefix, *endpoints):
        """ Nest the given endpoints at the prefix given """
        if prefix in self.nestedRoutes:
            self.nestedRoutes[prefix].add(*endpoints)
        else
            routes = Routes(*endpoints)
            self.nestedRoutes[prefix] = routes
            self.endpoints.append(NestedRoutes(prefix, routes))
            
    def register(self, app):
        """ Register the routes with the given app """
        for endpoint in self.endpoints:
            endpoint.register(app)