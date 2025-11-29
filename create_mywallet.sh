#!/bin/bash

# Project name
PROJECT_NAME="MyWallet"

# Create project root
mkdir $PROJECT_NAME
cd $PROJECT_NAME || exit

# ---------------------
# Backend structure
# ---------------------
mkdir -p backend/app/routers
mkdir -p backend/app/core
mkdir -p backend/app/utils
mkdir -p backend/tests

# Create backend files
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/app/models.py
touch backend/app/schemas.py
touch backend/app/crud.py
touch backend/app/database.py
touch backend/app/routers/__init__.py
touch backend/app/routers/users.py
touch backend/app/core/__init__.py
touch backend/app/core/config.py
touch backend/app/utils/__init__.py
touch backend/app/utils/security.py
touch backend/tests/test_users.py
touch backend/requirements.txt
touch backend/.env

# ---------------------
# Frontend structure
# ---------------------
mkdir -p frontend/public
mkdir -p frontend/src/components
mkdir -p frontend/src/pages

# Create frontend files
touch frontend/src/App.js
touch frontend/src/index.js
touch frontend/package.json
touch frontend/.env

# ---------------------
# Root files
# ---------------------
touch README.md
touch docker-compose.yml
touch Dockerfile.backend

echo "Project $PROJECT_NAME structure created successfully!"
