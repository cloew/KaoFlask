from .nested_app import NestedApp

class NestedRoutes:
    """ Represents a collection of nested routes """
    
    def __init__(self, prefix, routes):
        """ Initialize with the prefix and the routes """
        self.prefix = prefix
        self.routes = routes
        
    def register(self, app):
        """ Regsiter with the given app """
        nestedApp = NestedApp(self.prefix, app)
        self.routes.register(nestedApp)