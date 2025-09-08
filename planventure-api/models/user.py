from datetime import datetime, timezone
from app import db
from utils.password import hash_password, verify_password
from utils.auth import generate_token

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, 
                          default=lambda: datetime.now(timezone.utc),
                          onupdate=lambda: datetime.now(timezone.utc))
    
    # Relationship with trips
    trips = db.relationship('Trip', back_populates='user', cascade='all, delete-orphan')

    # Relationship with Trip is handled by backref in Trip model
    
    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password: str) -> None:
        """Set the user's password hash."""
        self.password_hash = hash_password(password)

    def check_password(self, password: str) -> bool:
        """Check if the provided password matches the hash."""
        return verify_password(password, self.password_hash)

    def get_token(self) -> str:
        """Generate an access token for the user."""
        return generate_token(self.id)
