# config.py
# MedVitals AI — Production Environment Configuration
# Security remediation: secrets loaded from environment variables

import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.environ.get("APP_ENV", "production")
APP_NAME = os.environ.get("APP_NAME", "medvitals-ai")
APP_PORT = int(os.environ.get("APP_PORT", "8080"))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
AWS_ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

LLM_ENDPOINT = os.environ.get(
    "LLM_ENDPOINT",
    "https://api.openai.com/v1/chat/completions"
)
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o")
LLM_TIMEOUT = int(os.environ.get("LLM_TIMEOUT", "30"))

SESSION_SECRET = os.environ.get("SESSION_SECRET")