from flask import jsonify, request
from functools import wraps

def with_json(fn):
    """ Decorator to extract the request's Json and pass it to the function as a `json` parameter, then jsonify the result from the fn """
    @wraps(fn)
    def fn_with_json(*args, **kwargs):
        json = request.get_json()
        response = fn(*args, json=json, **kwargs)
        
        if type(response) is tuple and len(response) == 2:
            data, code = response
        else:
            data, code = response, 200
        return jsonify(data), code
    return fn_with_json
