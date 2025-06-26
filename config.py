"""
Configuration file for Yoga Pose Detection System
"""

import os
from typing import Dict, Any

# Server Configuration
HOST = "0.0.0.0"
PORT = 8000
DEBUG = True

# CORS Configuration
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
    "*"  # Allow all origins in development
]

# MediaPipe Configuration
MEDIAPIPE_CONFIG = {
    "static_image_mode": True,
    "model_complexity": 2,
    "enable_segmentation": True,
    "min_detection_confidence": 0.5
}

# Pose Analysis Configuration
ANGLE_THRESHOLDS = {
    "elbow": {"min": 80, "max": 160},
    "knee": {"min": 90, "max": 170},
    "hip": {"min": 60, "max": 180},
    "shoulder": {"min": 70, "max": 180}
}

# File Upload Configuration
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

# Image Processing Configuration
IMAGE_QUALITY = 0.8
MAX_IMAGE_DIMENSION = 1024

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# --- New Security Configuration ---
# You should generate a strong, random secret key for production
# Command: openssl rand -hex 32
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
# --- End of Security Configuration ---

# Development Configuration
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
IS_PRODUCTION = ENVIRONMENT.lower() == "production"

# API Configuration
API_TITLE = "Yoga Pose Detection API"
API_VERSION = "1.0.0"
API_DESCRIPTION = """
A comprehensive pose detection system for yoga pose analysis.

## Features
- Upload and analyze yoga pose images
- Real-time camera pose detection
- Joint angle calculations and safety alerts
- Visual feedback with pose landmarks

## Endpoints
- `POST /analyze-image` - Analyze pose from uploaded image
- `POST /analyze-frame` - Analyze pose from base64 encoded frame
- `GET /health` - Health check endpoint
"""

# Error Messages
ERROR_MESSAGES = {
    "no_pose_detected": "No pose detected in the image. Please ensure the person is clearly visible.",
    "file_too_large": "File size exceeds maximum limit of 10MB.",
    "invalid_file_type": "Invalid file type. Please upload an image file.",
    "camera_error": "Unable to access camera. Please check permissions.",
    "processing_error": "Error processing image. Please try again.",
    "backend_error": "Backend service error. Please try again later."
}

# Success Messages
SUCCESS_MESSAGES = {
    "pose_analyzed": "Pose analyzed successfully!",
    "camera_started": "Camera started successfully!",
    "camera_stopped": "Camera stopped successfully!"
}

def get_config() -> Dict[str, Any]:
    """Get the complete configuration dictionary."""
    return {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG,
        "cors_origins": CORS_ORIGINS,
        "mediapipe_config": MEDIAPIPE_CONFIG,
        "angle_thresholds": ANGLE_THRESHOLDS,
        "max_file_size": MAX_FILE_SIZE,
        "allowed_extensions": ALLOWED_EXTENSIONS,
        "image_quality": IMAGE_QUALITY,
        "max_image_dimension": MAX_IMAGE_DIMENSION,
        "log_level": LOG_LEVEL,
        "log_format": LOG_FORMAT,
        "jwt_secret_key": JWT_SECRET_KEY,
        "jwt_algorithm": JWT_ALGORITHM,
        "access_token_expire_minutes": ACCESS_TOKEN_EXPIRE_MINUTES,
        "environment": ENVIRONMENT,
        "is_production": IS_PRODUCTION,
        "api_title": API_TITLE,
        "api_version": API_VERSION,
        "api_description": API_DESCRIPTION,
        "error_messages": ERROR_MESSAGES,
        "success_messages": SUCCESS_MESSAGES
    } 