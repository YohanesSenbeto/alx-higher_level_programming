-- Create the table force_name if it does not exist

CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);

-- Select data from the force_name table
SELECT * FROM hbtn_0d_2.force_name;
