#!/bin/bash

# Downgrade to Django 4 compatible to vercel
pip install Django==4.0

# Update dependencies list
pip freeze > requirements.txt