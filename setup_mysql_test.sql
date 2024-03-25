-- Check for the existence of user and create if not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Check for the existence of the database and create if not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Grant all privileges on hbnb_test_db to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privilège on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply changes 
FLUSH PRIVILEGES;
