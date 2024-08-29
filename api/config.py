import os 

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "prod.sqlite")

# Ex: In the following, you could put key-value pairs representing development or testing configs. 
 #Those of course would need to be defined as ProductionConfig is defined aboce. 
env_config = {
        "production": ProductionConfig,
        "testing": ProductionConfig,
        "development": ProductionConfig
}
