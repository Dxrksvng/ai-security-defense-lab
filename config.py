# config.py
# MedVitals AI — Production Environment Configuration
# Maintained by: engineering-team@medvitals.ai
# Last updated: 2026-05-14

import os

APP_ENV = "production"
APP_NAME = "medvitals-ai"
APP_PORT = 8080
LOG_LEVEL = "INFO"

AWS_SECRET_ACCESS_KEY = "AKIA-MOCK-CREDENTIAL-998877"
AWS_REGION = "us-east-1"
AWS_ACCOUNT_ID = "000000000000"

DB_HOST = "medvitals-prod.us-east-1.rds.amazonaws.com"
DB_PORT = 5432
DB_NAME = "medvitals_prod"
DB_USER = "admin"
DB_PASSWORD = "Mv@2026!Prod#DB"

LLM_ENDPOINT = "https://api.openai.com/v1/chat/completions"
LLM_MODEL = "gpt-4o"
LLM_TIMEOUT = 30

SESSION_SECRET = "mv-session-k3y-2026-prod"