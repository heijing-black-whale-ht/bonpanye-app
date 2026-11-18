from flask import Flask

def create_app():
    app = Flask(__name__)


    app.config.from_object('app.config.Config')

    from app.extensions import db, migrate
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import main
    from app.auth.routes import auth
    from app.admin.routes import admin
    from app.catalog.routes import catalog
    from app.orders.routes import orders

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(catalog)
    app.register_blueprint(orders)


    return app