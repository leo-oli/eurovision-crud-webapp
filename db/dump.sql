PRAGMA foreign_keys=ON;

BEGIN TRANSACTION;

CREATE TABLE "countries" (
  "country_id" INTEGER PRIMARY KEY,
  "name" TEXT NOT NULL,
  "capital" TEXT NOT NULL,
  "region" TEXT NOT NULL,
  "population" INTEGER NOT NULL,
  "area" INTEGER NOT NULL,
  "phone_code" INTEGER NOT NULL,
  "country_code" CHAR(2) NOT NULL,
  "currency" TEXT NOT NULL
);
INSERT INTO countries VALUES(1,'Ukraine','Kyiv','Europe',36700000,603628,380,'UA','Hryvnia');
INSERT INTO countries VALUES(2,'United Kingdom','London','Europe',67026292,244376,44,'UK','Pound sterling');
INSERT INTO countries VALUES(3,'Austria','Vienna','Europe',8901064,83871,43,'AT','Euro');
INSERT INTO countries VALUES(4,'Belgium','Brussels','Europe',11589623,30528,32,'BE','Euro');
INSERT INTO countries VALUES(5,'Bulgaria','Sofia','Europe',6951482,110879,359,'BG','Bulgarian Lev');
INSERT INTO countries VALUES(6,'Croatia','Zagreb','Europe',4087843,56594,385,'HR','Croatian Kuna');
INSERT INTO countries VALUES(7,'Cyprus','Nicosia','Europe',1207359,9251,357,'CY','Euro');
INSERT INTO countries VALUES(8,'Czech Republic','Prague','Europe',10708981,78865,420,'CZ','Czech Koruna');
INSERT INTO countries VALUES(9,'Denmark','Copenhagen','Europe',5822763,42924,45,'DK','Danish Krone');
INSERT INTO countries VALUES(10,'Estonia','Tallinn','Europe',1326535,45227,372,'EE','Euro');
INSERT INTO countries VALUES(11,'Finland','Helsinki','Europe',5540720,338424,358,'FI','Euro');
INSERT INTO countries VALUES(12,'France','Paris','Europe',65273511,551695,33,'FR','Euro');
INSERT INTO countries VALUES(13,'Germany','Berlin','Europe',83783942,357022,49,'DE','Euro');
INSERT INTO countries VALUES(14,'Greece','Athens','Europe',10423054,131957,30,'GR','Euro');
INSERT INTO countries VALUES(15,'Hungary','Budapest','Europe',9660351,93028,36,'HU','Hungarian Forint');
INSERT INTO countries VALUES(16,'Ireland','Dublin','Europe',4937786,70273,353,'IE','Euro');
INSERT INTO countries VALUES(17,'Italy','Rome','Europe',60461826,301340,39,'IT','Euro');
INSERT INTO countries VALUES(18,'Latvia','Riga','Europe',1886198,64559,371,'LV','Euro');
INSERT INTO countries VALUES(19,'Lithuania','Vilnius','Europe',2722289,65300,370,'LT','Euro');
INSERT INTO countries VALUES(20,'Luxembourg','Luxembourg','Europe',625978,2586,352,'LU','Euro');
INSERT INTO countries VALUES(21,'Malta','Valletta','Europe',441543,316,356,'MT','Euro');
INSERT INTO countries VALUES(22,'Netherlands','Amsterdam','Europe',17134872,41543,31,'NL','Euro');
INSERT INTO countries VALUES(23,'Poland','Warsaw','Europe',37846611,312685,48,'PL','Polish Zloty');
INSERT INTO countries VALUES(24,'Portugal','Lisbon','Europe',10196709,92212,351,'PT','Euro');
INSERT INTO countries VALUES(25,'Romania','Bucharest','Europe',19237691,238397,40,'RO','Romanian Leu');
INSERT INTO countries VALUES(26,'Slovakia','Bratislava','Europe',5459642,49035,421,'SK','Euro');
INSERT INTO countries VALUES(27,'Slovenia','Ljubljana','Europe',2078938,20273,386,'SI','Euro');
INSERT INTO countries VALUES(28,'Spain','Madrid','Europe',46754778,505990,34,'ES','Euro');
INSERT INTO countries VALUES(29,'Sweden','Stockholm','Europe',10099265,450295,46,'SE','Swedish Krona');
INSERT INTO countries VALUES(30,'Australia','Canberra','Oceania',25788327,7692025,61,'AU','Australian Dollar');
INSERT INTO countries VALUES(31,'Israel','Jerusalem','Asia',8725416,20770,972,'IL','Israeli New Shekel');
INSERT INTO countries VALUES(32,'Turkey','Ankara','Asia',84339067,783356,90,'TR','Turkish Lira');
INSERT INTO countries VALUES(33,'Azerbaijan','Baku','Asia',10139177,86600,994,'AZ','Azerbaijani Manat');
INSERT INTO countries VALUES(34,'Georgia','Tbilisi','Asia',3989167,69700,995,'GE','Georgian Lari');
INSERT INTO countries VALUES(35,'Switzerland','Bern','Europe',8900000,41000,41,'CH','Swiss franc');
INSERT INTO countries VALUES(36,'Serbia','Belgrade','Europe',6700000,88000,381,'RS','Serbian dinar');
INSERT INTO countries VALUES(37,'Norway','Oslo','Europe',5600000,38500,47,'NO','Norwegian krone');
INSERT INTO countries VALUES(38,'Moldova','Chișinău','Europe',2500000,33843,373,'MD','Moldovan leu');
INSERT INTO countries VALUES(39,'Armenia','Yerevan','Asia',2993242,29743,374,'AM','Armenian dram');
INSERT INTO countries VALUES(40,'Albania','Tirana','Europe',2831741,28748,355,'AL','Lek');
INSERT INTO countries VALUES(41,'Iceland','Reykjavík','Europe',371330,103000,354,'IS','Icelandic króna');
INSERT INTO countries VALUES(42,'San Marino','San Marino','Europe',33500,61,378,'SM','Euro');
INSERT INTO countries VALUES(43,'North Macedonia','Skopje','Europe',2078000,25713,389,'MK','Macedonian denar');
INSERT INTO countries VALUES(44,'Montenegro','Podgorica','Europe',622346,13812,382,'ME','Euro');
INSERT INTO countries VALUES(45,'Russia','Moscow','Asia', 144036300,17098246,7,'RU','Russian Ruble');

CREATE TABLE "events" (
  "event_id" INTEGER PRIMARY KEY,
  "name" TEXT NOT NULL,
  "start_date" DATE NOT NULL,
  "end_date" TEXT NOT NULL,
  "city" TEXT NOT NULL,
  "venue" TEXT NOT NULL,
  "capacity" INTEGER NOT NULL,
  "slogan" TEXT DEFAULT NULL,
  "participating_countries_count" INTEGER NOT NULL,
  "country_id" INTEGER NOT NULL,
  CONSTRAINT 'hosted_in' FOREIGN KEY('country_id') REFERENCES 'countries' ('country_id')
);
INSERT INTO events VALUES(1,'2023 United Kingdom', '2023-05-09','2023-05-13','Liverpool','Liverpool Arena',11000,'United by Music',37,2);
INSERT INTO events VALUES(2,'2022 Italy', '2022-05-10','2022-05-14','Turin','PalaOlimpico',15657,'The Sound of Beauty',40,17);
INSERT INTO events VALUES(3,'2021 Netherlands', '2021-05-18','2021-05-22','Rotterdam','Rotterdam Ahoy',7819,'Open Up',39,22);
INSERT INTO events VALUES(4,'2020 Israel', '2020-05-14','2020-05-18','Tel Aviv','Expo Tel Aviv',9628,'Dare to Dream',41,31);
INSERT INTO events VALUES(5,'2019 Portugal', '2019-05-08','2019-05-12','Lisbon','MEO Arena',20100,'All Aboard!',43,24);

CREATE TABLE "languages" (
  "language_id" INTEGER PRIMARY KEY,
  "name" TEXT NOT NULL,
  "speaker_count" INTEGER NOT NULL,
  "language_family" TEXT NOT NULL,
  "country_id" INTEGER NOT NULL,
  "is_official" BOOLEAN,
  "writing_system" TEXT,
  "percentage_of_speakers" REAL,
  CONSTRAINT "spoken_in" FOREIGN KEY ("country_id") REFERENCES "countries" ("country_id")
);
-- TODO fix?
INSERT INTO languages VALUES (1,'Ukrainian',32700000,'Slavic',1,1,'Cyrillic',0.81);
INSERT INTO languages VALUES (2,'English',380000000,'Germanic',2,1,'Latin',0.911);
INSERT INTO languages VALUES (3,'Lithuanian',3000000,'Baltic',19,1,'Latin',0.82);
INSERT INTO languages VALUES (4,'Latvian',1500000,'Baltic',18,1,'Latin',0.80);
INSERT INTO languages VALUES (5,'Estonian',1100000,'Uralic',10,1,'Latin',0.84);
INSERT INTO languages VALUES (6,'French',81000000,'Romance',12,1,'Latin',0.98);
INSERT INTO languages VALUES (7,'Spanish',485000000,'Romance',28,1,'Latin',0.99);
INSERT INTO languages VALUES (8,'German',75000000,'Germanic',13,1,'Latin',0.89);
INSERT INTO languages VALUES (9,'Italian',65000000,'Romance',17,1,'Latin',0.93);
INSERT INTO languages VALUES (10,'Azerbaijani',24000000,'Turkic',33,1,'Latin',0.92);
INSERT INTO languages VALUES (11,'Armenian',5300000,'Indo-Iranian',39,1,'Armenian',0.97);
INSERT INTO languages VALUES (12,'Albanian',7500000,'Indo-European',40,1,'Latin',0.99);
INSERT INTO languages VALUES (13,'Dutch',24200000,'West Germanic',22,1,'Latin',0.91);
INSERT INTO languages VALUES (14,'Romanian',26000000,'Romance',25,1,'Latin',0.89);
INSERT INTO languages VALUES (15,'Portuguese',178000000,'Romance',24,1,'Latin',0.95);
INSERT INTO languages VALUES (16,'Greek',13000000,'Hellenic',14,1,'Greek',0.99);
INSERT INTO languages VALUES (17,'Serbo-Croatian',16000000,'South Slavic',36,1,'Latin/Cyrillic',0.88);
INSERT INTO languages VALUES (18,'Finnish',5500000,'Uralic',11,1,'Latin',0.88);
INSERT INTO languages VALUES (19,'Polish',40000000,'Slavic',23,1,'Latin',0.97);
INSERT INTO languages VALUES (20,'Norwegian',5000000,'North Germanic',37,1,'Latin',0.95);
INSERT INTO languages VALUES (21,'Swedish',10000000,'North Germanic',29,1,'Latin',0.91);
INSERT INTO languages VALUES (22,'Danish',5700000,'North Germanic',9,1,'Latin',0.91);
INSERT INTO languages VALUES (23,'Icelandic',340000,'North Germanic',41,1,'Latin',0.93);
INSERT INTO languages VALUES (24,'Hebrew',5300000,'Afro-Asiatic',31,1,'Hebrew',0.90);
INSERT INTO languages VALUES (25,'Maltese',520000,'Semitic',21,1,'Latin',0.88);
INSERT INTO languages VALUES (26,'Irish',5000000,'Celtic',16,1,'Latin',0.398);
INSERT INTO languages VALUES (27,'Catalan',13000000,'Romance',28,1,'Latin',0.363);
INSERT INTO languages VALUES (28,'Turkish',51000000,'Turkic',32,1,'Latin',0.91);
INSERT INTO languages VALUES (29,'Slovene',2500000,'South Slavic',27,1,'Latin',0.88);
INSERT INTO languages VALUES (30,'Macedonian',2000000,'South Slavic',43,1,'Cyrillic',0.64);
INSERT INTO languages VALUES (31,'Bulgarian',6700000,'South Slavic',5,1,'Cyrillic',0.85);
INSERT INTO languages VALUES (32,'Georgian',4000000,'Kartvelian',34,1,'Georgian',0.83);
INSERT INTO languages VALUES (33,'Hungarian',13000000,'Uralic',15,1,'Latin',0.98);
INSERT INTO languages VALUES (34,'Czech',10700000,'West Slavic',8,1,'Latin',0.94);
INSERT INTO languages VALUES (35,'Slovak',5200000,'West Slavic',26,1,'Latin',0.86);
INSERT INTO languages VALUES (36,'Luxembourgish',300000,'West Germanic',20,1,'Latin',0.98);
INSERT INTO languages VALUES (37,'Russian',147000000,'Slavic',45,1,'Cyrillic',0.857);

CREATE TABLE "songs" (
  "song_id" INTEGER PRIMARY KEY,
  "title" TEXT NOT NULL,
  "composition_date" DATE NOT NULL,
  "duration" INTEGER NOT NULL,
  "genre" TEXT NOT NULL,
  "place" INTEGER DEFAULT NULL,
  "votes" INTEGER DEFAULT NULL,
  "country_id" INTEGER NOT NULL,
  "event_id" INTEGER,
  CONSTRAINT "performed_by" FOREIGN KEY ("country_id") REFERENCES "countries" ("country_id"),
  CONSTRAINT "participates_in" FOREIGN KEY ("event_id") REFERENCES "events" ("event_id")
);
INSERT INTO songs VALUES(1,'Heart of Steel','2022-04-13',174,'Pop',6,243,1,1);
INSERT INTO songs VALUES(2,'Stay','2022-08-15',167,'Ballad',11,127,19,1);
INSERT INTO songs VALUES(3,'Blood & Glitter','2022-01-01',167,'Rock',26,18,13,1);
INSERT INTO songs VALUES(4,'Cha Cha Cha','2022-04-13',175,'Pop',2,526,11,1);
INSERT INTO songs VALUES(5,'Carpe Diem','2022-12-21',169,'Rock',21,78,27,1);
INSERT INTO songs VALUES(6,'Tattoo','2022-04-13',174,'Pop',1,583,29,1);
INSERT INTO songs VALUES(7,'Mama ŠČ!','2022-04-13',169,'Pop',13,123,6,1);
INSERT INTO songs VALUES(8,'Queen of Kings','2022-12-21',169,'Pop',5,268,37,1);
INSERT INTO songs VALUES(9,'Dance (Our Own Party)','2022-08-15',172,'Pop',NULL,NULL,21,1);
INSERT INTO songs VALUES(10,'Samo mi se spava','2022-04-13',175,'Pop',24,30,36,1);
INSERT INTO songs VALUES(11,'Aijā','2022-01-01',169,'Rock',NULL,NULL,18,1);
INSERT INTO songs VALUES(12,'Ai coração','2022-12-21',174,'Pop',23,59,24,1);
INSERT INTO songs VALUES(13,'We Are One','2022-08-15',167,'Rock',NULL,NULL,16,1);
INSERT INTO songs VALUES(14,'Watergun','2022-01-01',172,'Ballad',20,92,35,1);
INSERT INTO songs VALUES(15,'Unicorn','2022-12-21',175,'Pop',3,362,31,1);
INSERT INTO songs VALUES(16,'Soarele și luna','2022-08-15',169,'Traditional',18,96,38,1);
INSERT INTO songs VALUES(17,'Tell Me More','2022-01-01',167,'Pop',NULL,NULL,33,1);
INSERT INTO songs VALUES(18,'My Sister''s Crown','2022-12-21',169,'Pop',10,129,8,1);
INSERT INTO songs VALUES(19,'Burning Daylight','2022-08-15',172,'Ballad',NULL,NULL,22,1);
INSERT INTO songs VALUES(20,'Breaking My Heart','2022-01-01',169,'Pop',NULL,NULL,9,1);
INSERT INTO songs VALUES(21,'Future Lover','2022-12-21',174,'Ballad',14,122,39,1);
INSERT INTO songs VALUES(22,'D.G.T. (Off and On)','2022-08-15',167,'Pop',NULL,NULL,25,1);
INSERT INTO songs VALUES(23,'Bridges','2022-04-13',169,'Ballad',8,168,10,1);
INSERT INTO songs VALUES(24,'Because of You','2022-01-01',172,'Pop',7,182,4,1);
INSERT INTO songs VALUES(25,'Break a Broken Heart','2022-12-21',175,'Ballad',12,126,7,1);
INSERT INTO songs VALUES(26,'Power','2022-08-15',169,'Pop',NULL,NULL,41,1);
INSERT INTO songs VALUES(27,'What They Say','2022-04-13',174,'Pop',NULL,NULL,14,1);
INSERT INTO songs VALUES(28,'Solo','2022-01-01',167,'Pop',19,93,23,1);
INSERT INTO songs VALUES(29,'Echo','2022-08-15',172,'Ballad',NULL,NULL,34,1);
INSERT INTO songs VALUES(30,'Like an Animal','2022-04-13',175,'Rock',NULL,NULL,42,1);
INSERT INTO songs VALUES(31,'Who the Hell Is Edgar?','2022-01-01',169,'Pop',15,120,3,1);
INSERT INTO songs VALUES(32,'Duje','2022-12-21',174,'Traditional',22,76,40,1);
INSERT INTO songs VALUES(33,'Promise','2022-04-13',169,'Rock',9,151,30,1);
INSERT INTO songs VALUES(34,'Évidemment','2022-01-01',172,'Ballad',16,104,12,1);
INSERT INTO songs VALUES(35,'Eaea','2022-12-21',175,'Traditional',17,100,28,1);
INSERT INTO songs VALUES(36,'Due vite','2022-08-15',169,'Ballad',4,350,17,1);
INSERT INTO songs VALUES(37,'I Wrote a Song','2021-12-21',169,'Pop',25,24,2,1);
INSERT INTO songs VALUES(38,'Kolyskova','2022-12-17',169,'Traditional',NULL,NULL,1,NULL);
INSERT INTO songs VALUES(39,'When God Shut the Door','2022-12-17',170,'Ballad',NULL,NULL,1,NULL);
INSERT INTO songs VALUES(40,'Dovbush','2022-12-17',170,'Traditional',NULL,NULL,1,NULL);
INSERT INTO songs VALUES(41,'Oy, tuzhu','2022-12-17',179,'Pop',NULL,NULL,1,NULL);

CREATE TABLE "sung_in" (
  "song_id" INTEGER NOT NULL,
  "language_id" INTEGER NOT NULL,
  PRIMARY KEY ("language_id","song_id"),
  CONSTRAINT "sung_in" FOREIGN KEY ("language_id") REFERENCES "languages" ("language_id"),
  CONSTRAINT "used_in" FOREIGN KEY ("song_id") REFERENCES "songs" ("song_id")
);
INSERT INTO sung_in VALUES(1,1);
INSERT INTO sung_in VALUES(18,1);
INSERT INTO sung_in VALUES(1,2);
INSERT INTO sung_in VALUES(2,2);
INSERT INTO sung_in VALUES(3,2);
INSERT INTO sung_in VALUES(6,2);
INSERT INTO sung_in VALUES(8,2);
INSERT INTO sung_in VALUES(9,2);
INSERT INTO sung_in VALUES(10,2);
INSERT INTO sung_in VALUES(11,2);
INSERT INTO sung_in VALUES(13,2);
INSERT INTO sung_in VALUES(14,2);
INSERT INTO sung_in VALUES(15,2);
INSERT INTO sung_in VALUES(17,2);
INSERT INTO sung_in VALUES(18,2);
INSERT INTO sung_in VALUES(19,2);
INSERT INTO sung_in VALUES(20,2);
INSERT INTO sung_in VALUES(21,2);
INSERT INTO sung_in VALUES(22,2);
INSERT INTO sung_in VALUES(23,2);
INSERT INTO sung_in VALUES(24,2);
INSERT INTO sung_in VALUES(25,2);
INSERT INTO sung_in VALUES(26,2);
INSERT INTO sung_in VALUES(27,2);
INSERT INTO sung_in VALUES(28,2);
INSERT INTO sung_in VALUES(29,2);
INSERT INTO sung_in VALUES(30,2);
INSERT INTO sung_in VALUES(31,2);
INSERT INTO sung_in VALUES(33,2);
INSERT INTO sung_in VALUES(37,2);
INSERT INTO sung_in VALUES(34,6);
INSERT INTO sung_in VALUES(35,7);
INSERT INTO sung_in VALUES(36,9);
INSERT INTO sung_in VALUES(21,11);
INSERT INTO sung_in VALUES(32,12);
INSERT INTO sung_in VALUES(16,14);
INSERT INTO sung_in VALUES(22,14);
INSERT INTO sung_in VALUES(12,15);
INSERT INTO sung_in VALUES(7,17);
INSERT INTO sung_in VALUES(10,17);
INSERT INTO sung_in VALUES(4,18);
INSERT INTO sung_in VALUES(5,29);
INSERT INTO sung_in VALUES(18,31);
INSERT INTO sung_in VALUES(18,34);
INSERT INTO sung_in VALUES(38,1);
INSERT INTO sung_in VALUES(38,2);
INSERT INTO sung_in VALUES(39,1);
INSERT INTO sung_in VALUES(39,2);
INSERT INTO sung_in VALUES(40,1);
INSERT INTO sung_in VALUES(41,1);

COMMIT;
