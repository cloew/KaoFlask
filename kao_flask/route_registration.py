from collections.abc import Iterable

def isiterable(obj):
    """ Return if the object is iterable """
    return isinstance(obj, Iterable)

def register_routes(app, routes):
    """ Register the given routes """
    for routeOrSubRoutes in routes:
        if isiterable(routeOrSubRoutes):
            register_routes(app, routeOrSubRoutes)
        else:
            routeOrSubRoutes.register(app)
