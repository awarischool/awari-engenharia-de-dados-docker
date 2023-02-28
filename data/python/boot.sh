#!/bin/bash
exec gunicorn -b :5001 --access-logfile - --error-logfile - api:app