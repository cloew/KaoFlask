
REGISTER_METHOD = 'register'

def route_like(route):
    """ Return if the route has the Route interface """
    return hasattr(route, REGISTER_METHOD)