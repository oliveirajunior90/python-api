class HealthCheckView(object):
    def __init__(self, app, prefix):

        @app.get(prefix)
        def health_check():
            return {"message": "OK"}