from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Define the GraffitiEntry model
class GraffitiEntry(db.Model):
    __tablename__ = 'graffiti_entries'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each entry
    title = db.Column(db.String(100), nullable=False)  # Title of the graffiti
    description = db.Column(db.Text, nullable=True)  # Optional description
    latitude = db.Column(db.Float, nullable=False)  # Latitude of graffiti location
    longitude = db.Column(db.Float, nullable=False)  # Longitude of graffiti location
    image_url = db.Column(db.String(255), nullable=False)  # Path or URL of the uploaded image
    created_at = db.Column(db.DateTime, default=datetime.now)  # Entry creation timestamp
    created_by = db.Column(db.String(50), nullable=False)  # Contributor's name or username

    def __repr__(self):
        return f"<GraffitiEntry {self.id} - {self.title}>"
