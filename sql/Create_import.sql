LOAD DATA LOCAL INFILE '/home/jasonhao/recengine.org/public/media/data/CustomerProfiles2.csv'
INTO TABLE customer1
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'   
LINES TERMINATED BY '\n'
IGNORE 1 LINES

CREATE TABLE customer1(
   ID INT NOT NULL AUTO_INCREMENT,
   sumOfProfile VARCHAR(100) NOT NULL,
   month VARCHAR(100) NOT NULL,
   entity VARCHAR(40) NOT NULL,
   utilitydunsnumber VARCHAR(40) NOT NULL,
   utilityaccountnumber VARCHAR(40) NOT NULL,
   commodityid DOUBLE(16,10)  NOT NULL,
   meternumber DOUBLE(16,10) NOT NULL,
   jan DOUBLE(16,10)  NOT NULL,
   feb DOUBLE(16,10)  NOT NULL,
   mar DOUBLE(16,10)  NOT NULL,
   apr DOUBLE(16,10)  NOT NULL,
   may DOUBLE(16,10)  NOT NULL,
   jun DOUBLE(16,10)  NOT NULL,
   jul DOUBLE(16,10)  NOT NULL,
   aug DOUBLE(16,10)  NOT NULL,
   sem DOUBLE(16,10)  NOT NULL,
   oct DOUBLE(16,10)  NOT NULL,
   nov DOUBLE(16,10)  NOT NULL,
   december DOUBLE(16,10)  NOT NULL,
   valuesPerDay       VARCHAR(40),
   PRIMARY KEY ( ID )
);

LOAD DATA LOCAL INFILE '/home/jasonhao/recengine.org/public/media/data/CustomerList2.csv'
INTO TABLE customer2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r'
IGNORE 1 LINES

CREATE TABLE customer2(
   ID INT NOT NULL AUTO_INCREMENT,
   entity VARCHAR(100) NOT NULL,
   utility VARCHAR(100) NOT NULL,
   utilityduns VARCHAR(40) NOT NULL,
   utilityaccountnumber VARCHAR(40) NOT NULL,
   commodityid VARCHAR(40) NOT NULL,
   meternumberfixed VARCHAR(40) NOT NULL,
   servicestart DATE NOT NULL,
   contractexpiration DATE  NOT NULL,
   accounttype VARCHAR(40) NOT NULL,
   rateclasscode VARCHAR(40) NOT NULL,
   profiletype VARCHAR(40) NOT NULL,
   producttype VARCHAR(40) NOT NULL,
   iso VARCHAR(40) NOT NULL,
   loadzone VARCHAR(40) NOT NULL,
   plc DOUBLE(16,10)  NOT NULL,
   nits DOUBLE(16,10)  NOT NULL,
   currentrate DOUBLE(16,10)  NOT NULL,
   annualvolume DOUBLE(16,10)  NOT NULL,
   Column1 DOUBLE(16,10)  NOT NULL,
   PRIMARY KEY ( ID )
);


