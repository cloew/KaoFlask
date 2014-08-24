from flask import jsonify, request

class JSONController:
    """ Represents a controller for a JSON Page """
    
    def perform(self, *args, **kwargs):
        """ Perform the JSON action """
        return jsonify(self.performWithJSON(*args, json=request.json, **kwargs))
        
    def performWithJSON(self, json=None):
        """ Perform the JSON action """