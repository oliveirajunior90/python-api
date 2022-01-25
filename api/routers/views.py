from api.services.users.views import UsersView
from api.services.health_check import HealthCheckView

class RouterViews(object):
    
    api_version = 'v1'

    def __init__(self, app):
        UsersView(app, prefix="/users")
        HealthCheckView(app, prefix="/health-check")

        

        
