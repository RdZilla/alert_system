#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres --dbname postgres <<-EOSQL
    CREATE DATABASE alert_system;
    GRANT ALL PRIVILEGES ON DATABASE alert_system TO postgres;
EOSQL