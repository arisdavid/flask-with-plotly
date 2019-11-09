from flask import Flask
from main_app.blueprints.pages.views import page
from main_app.blueprints.charts.views import charts


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    app.register_blueprint(charts)
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

