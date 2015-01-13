from flask import jsonify, request

class JSONController:
    """ Represents a controller for a JSON Page """
    
    def __init__(self, decorators=[]):
        """ Initialize the JSON Controller with its required decorators """
        self.decorators = decorators
        
    @property
    def perform(self):
        """ Return the perform function """
        method = self.performMethod
        for decorator in self.decorators:
            method = decorator(method)
        return method
    
    def performMethod(self, *args, **kwargs):
        """ Perform the JSON action """
        response = self.performWithJSON(*args, **kwargs)
        
        code = 200
        if len(response) == 2 and type(response) is tuple:
            data, code = response
        else:
            data = response
        return jsonify(data), code
        
    def performWithJSON(self, json=None):
        """ Perform the JSON action """
       
    @property
    def json(self):
        """ Return the current JSON """
        return request.json