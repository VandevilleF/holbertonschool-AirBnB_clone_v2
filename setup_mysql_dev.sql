-- Check if the database 'hbnb_test_db' already exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbnb_test_db';

-- If the database doesn't exist, create it
IF @@rowcount = 0 THEN
  CREATE DATABASE hbnb_test_db;
END IF;

-- Check if the user 'hbnb_test' already exists
SELECT User FROM mysql.user WHERE User = 'hbnb_test' AND Host = 'localhost';

-- If the user doesn't exist, create it
IF @@rowcount = 0 THEN
  CREATE USER hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
END IF;

-- Grant all privileges on 'hbnb_test_db' to 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;

-- Grant SELECT privilege on 'performance_schema' to 'hbnb_test'
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;

-- Flush privileges to apply changes immediately
FLUSH PRIVILEGES;
