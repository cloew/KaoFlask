from flask import jsonify, request

class JSONController:
    """ Represents a controller for a JSON Page """
    
    def perform(self, *args, **kwargs):
        """ Perform the JSON action """
        response = self.performWithJSON(*args, json=request.json, **kwargs)
        
        code = 200
        if len(response) == 2:
            data, code = response
        else:
            data = response
        return jsonify(data), code
        
    def performWithJSON(self, json=None):
        """ Perform the JSON action """