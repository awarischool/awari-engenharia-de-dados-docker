#!/bin/bash

# Usage: Initial script put in `docker-entrypoint-initdb.d` directory
# Use bash for least error prones caused by shell syntax.

# Immediately exits if any error occurs during the script
# execution. If not set, an error could occur and the
# script would continue its execution.
set -o errexit
set -ex

# Creating an array that defines the environment variables
# that must be set. This can be consumed later via arrray
# variable expansion ${REQUIRED_ENV_VARS[@]}.
readonly REQUIRED_ENV_VARS=(
  "POSTGRES_USER")

# Main execution:
# - verifies if all environment variables are set
# - runs the SQL code to create user and database
main() {
  check_env_vars_set
#   init_user_and_db
}

# Checks if all of the required environment variables are set.
# If one of them isn't, echoes a text explaining which one isn't
# and the name of the ones that need to be.
check_env_vars_set() {
  for required_env_var in "${REQUIRED_ENV_VARS[@]}"; do
    if [[ -z "${!required_env_var}" ]]; then
      echo "Error:
    Environment variable '$required_env_var' not set.
    Make sure you have the following environment variables set:"
      "${REQUIRED_ENV_VARS[@]}"
"Aborting."
      exit 1
    fi
  done
}

# Performs the initialization in the already-started PostgreSQL
# using the preconfigured POSTGRE_USER user.
# init_user_and_db() {
#   psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
#      CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
#      CREATE DATABASE $DB_DATABASE;
#      GRANT ALL PRIVILEGES ON DATABASE $DB_DATABASE TO $DB_USER;
# EOSQL
# }

function create_user_and_database() {
    local DB_DATABASE=$1
    echo "  Creating user and database '$DB_DATABASE'"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
        CREATE DATABASE $DB_DATABASE;
        CREATE USER $DB_DATABASE WITH PASSWORD '${POSTGRES_PASSWORD}';
        ALTER DATABASE $DB_DATABASE OWNER TO $DB_DATABASE;
        GRANT ALL PRIVILEGES ON DATABASE $DB_DATABASE TO $POSTGRES_USER;
        GRANT ALL ON schema public TO $DB_DATABASE;
        GRANT USAGE ON schema public TO $DB_DATABASE;
EOSQL
}

if [ -n "$POSTGRES_MULTIPLE_DATABASES" ]; then
    echo "Multiple database creation requested: $POSTGRES_MULTIPLE_DATABASES"
    for db in $(echo "$POSTGRES_MULTIPLE_DATABASES" | tr ',' ' '); do
        create_user_and_database "$db"
    done
    echo "Multiple databases created"
fi

# Executes the main routine with environment variables
# passed through the command line. We don't use them in
# this script but now you know
main "$@"