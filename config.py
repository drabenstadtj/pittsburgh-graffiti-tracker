import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")  # use env var or fallback
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable modification tracking
    UPLOAD_FOLDER = "static/images"  # default upload folder for images

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///graffiti.db"  # SQLite database for development

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///graffiti.db")  # Use env var or fallback

# Choose the configuration based on environment variable
config = DevelopmentConfig if os.getenv("FLASK_ENV") == "production" else DevelopmentConfig

# Example env file:
#  FLASK_ENV=production or empty for development
#  SECRET_KEY=your_secure_secret_key
#  DATABASE_URL=sqlite:///prod_database.db may be changed to mysql or otherwise later
