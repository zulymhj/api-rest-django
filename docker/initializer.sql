-- ########
--
-- ########
DROP DATABASE IF EXISTS  ecommerce_db;
CREATE USER eco_user WITH ENCRYPTED PASSWORD 'eco_pass';
CREATE DATABASE ecommerce_db owner eco_user;
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO eco_user;