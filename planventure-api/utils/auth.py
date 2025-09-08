from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta

def generate_token(user_id: int) -> str:
    """Generate a JWT token for the given user ID."""
    expires_delta = timedelta(days=1)  # Token expires in 1 day
    return create_access_token(
        identity=user_id,
        expires_delta=expires_delta
    )

def get_current_user_id() -> int:
    """Get the current user ID from the JWT token."""
    return get_jwt_identity()
