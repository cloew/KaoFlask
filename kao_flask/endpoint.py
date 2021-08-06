
class Endpoint:
    """ Represents a URL endpoint """
    
    def __init__(self, url, **kwargs):
        """ Initialize the Endpoint """
        if hasattr(url, 'url'):
            url = url.url
        self.url = url
        
        self.methodToHandler = {}
        for key in kwargs:
            self.methodToHandler[key.upper()] = kwargs[key]
        
    def register(self, app):
        """ Register the Endpoint with the server """
        for method in self.methodToHandler:
            handler = self.methodToHandler[method]
            app.add_url_rule(self.url, str(handler), handler, methods=[method])