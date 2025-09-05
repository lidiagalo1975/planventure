from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Basic configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///planventure.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import models here to avoid circular imports
from models import User

CORS(app, origins=os.getenv('CORS_ORIGINS', '*'))

@app.route('/')
def home():
    return jsonify({"message": "Welcome to PlanVenture API"})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)
