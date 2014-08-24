
class Endpoint:
    """ Represents a URL endpoint """
    
    def __init__(self, url, **kwargs):
        """ Initialize the Endpoint """
        self.url = url
        
        self.methodToController = {}
        for key in kwargs:
            self.methodToController[key.upper()] = kwargs[key]
        
    def addToServer(self, app):
        """ Add the Endpoint to the server """
        for method in self.methodToController:
            controller = self.methodToController[method]
            app.add_url_rule(self.url, 'stuff', controller.perform, methods=[method])