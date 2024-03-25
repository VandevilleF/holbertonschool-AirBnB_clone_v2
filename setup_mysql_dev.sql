-- Check for the existence of user and create if not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Check for the existence of the database and create if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Grant all privilèges on hbnb_dev_db to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant select privilège on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
