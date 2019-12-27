CREATE TABLE weather(
	id INT NOT NULL,
	timeId INT NOT NULL,
	latitude VARCHAR(100) NOT NULL,
	longitude VARCHAR(100) NOT NULL,
	location VARCHAR(100) NOT NULL,
	summaryForcast VARCHAR(100) NOT NULL,
	curTemp INT NOT NULL,
	PRIMARY KEY(id)
);



-- CREATE TABLE report(
-- 	id INT NOT NULL,
-- 	lat VARCHAR(20) NOT NULL,
-- 	lon VARCHAR(20) NOT NULL,
-- 	t INT NOT NULL,
-- 	sum VARCHAR(20) NOT NULL,
-- 	PRIMARY KEY(id)
-- );


-- CREATE TABLE users(
--   username VARCHAR(20) NOT NULL,
--   fullname VARCHAR(40) NOT NULL,
--   age INT NOT NULL,
--   PRIMARY KEY(username)
-- );
