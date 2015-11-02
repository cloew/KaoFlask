
REGISTER_METHOD = 'register'

def endpoint_like(endpoint):
    """ Return if the endpoint has the Endpoint interface """
    return hasattr(endpoint, REGISTER_METHOD)