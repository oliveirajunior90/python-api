class UsersView(object):

    def __init__(self, app, prefix):

        @app.get(prefix)
        def get_all_users():
            return []