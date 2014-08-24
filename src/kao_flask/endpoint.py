
class Endpoint:
    """ Represents a URL endpoint """
    
    def __init__(self, url, get=None):
        """ Initialize the Endpoint """
        self.url = url
        self.getController = get
        
    def addToServer(self, app):
        """ Add the Endpoint to the server """
        if self.getController is not None:
            app.add_url_rule(self.url, 'stuff', self.getController.perform, methods=['GET'])