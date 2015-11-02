from kao_decorators import proxy_for

@proxy_for('endpoints', ['__iter__'])
class Routes:
    """ Represents a container of Route Endpoints that can add nested Route Endpoints """
    
    def __init__(*endpoints):
        """ Initialize with any number of Endpoints """
        self.endpoints = []
        for endpoint in endpoints:
            self.add(endpoint)
            
    def add(self, endpoint):
        """ Add the given endpoint """
        self.endpoints.append(endpoint)