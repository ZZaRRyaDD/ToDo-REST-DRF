import os
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

if cors_origins := os.getenv('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS = [
        origin.strip() for origin in cors_origins.split(',')
    ]
else:
    CORS_ALLOWED_ORIGINS = []

CORS_ALLOWED_ORIGIN_REGEXES = [
    r'^http://localhost(:[0-9]+)?',
]

SPECTACULAR_SETTINGS = {
    "TITLE": "todo_rest API",
    "DESCRIPTION": "Documentation of API endpoints of todo_rest",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny",],
    "SERVERS": [
        {
            "url": "http://localhost:8000",
            "description": "Local Development server",
        },
    ],
}

SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('JWT',),
}

DJOSER = {
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "SET_USERNAME_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "reset/password/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "reset/username/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "SERIALIZERS": {
        "user_create": "apps.account.serializers.UserSerializer",
        "user": "apps.account.serializers.UserSerializer",
        "current_user": "apps.account.serializers.UserSerializer",
        "user_delete": "apps.account.serializers.UserSerializer",
    },
}
