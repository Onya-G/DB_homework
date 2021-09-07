INSERT INTO genres(name) 
VALUES ('rock'),('pop'),('folk'),('jazz'),('country'),('electronic');
	
INSERT INTO musicians(name) 
VALUES('Tata Hakuna'),('Vereteno'),('Merenga'),('Bodr Ivesel'),('Urfin biting tale'),
	('Bibo and Bobo'),('Aiva'),('Cuprum'),('Orange Albatros'),('Mr. Punenta');
	
INSERT INTO genre_musician(genre_id, musician_id) 
VALUES(19,31),(20,32),(21,33),(22,34),(23,35),(24,36),(19,37),(20,38),(21,39),(22,40),(23,31),(24,32),(19,33),(20,31),(21,32);

INSERT INTO albums(name, year) 
VALUES('Shadow in night', 2019),('Heartbeat', 2020),('New old', 2021),('Carrramba', 2018),('Cats and butterfly', 2017),
	('Ratatata', 2016),('Invisible friend', 2020),('Wind in a head', 2021),('Soultrip', 2018),('Lighthouse', 2019);

INSERT INTO musician_album(musician_id, album_id) 
VALUES(32,11),(33,12),(34,13),(35,14),(36,15),(37,16),(38,17),(39,18),(40,19),(31,20),(35,11),(36,12),(37,13),(38,14),(39,15);

INSERT INTO tracks (name, time, album_id) 
VALUES('Myrtle tree', 206, 11),('Semiawaken', 308, 12),('Comma', 234, 13),('Silver moon', 206, 14),('Jemyma', 297, 15),('Thorn', 376, 16),('Dialy Hero', 478, 17),('Send in eyes', 390, 18),('Dont slouch!', 403, 19),
	('I wanna sleep', 267, 20),('But first', 301, 11),('I should finish', 287, 12),('This task', 310, 13),('Hearless cats', 268, 12),('Jumping around', 346, 14),('But I cant', 385, 13),('Join to them', 238, 14),
	('Soon', 294, 15),('My horse sings igogo', 270, 16),('Last song', 310, 17),('Free', 300 ,11);

INSERT INTO mixtapes(name, year) 
VALUES('Funny mix', 2020),('Old new', 2021),('For driving', 2019),('Run!', 2021),('Almost done', 2018),
	('Mosquito go away', 2020),('Sorry neighbors', 2018),('It will be loud', 2019),('Without words', 2021);

INSERT INTO mixtape_track(mixtape_id, track_id) 
VALUES(12,31),(13,32),(14,33),(15,34),(16,35),(17,36),(18,37),(10,38),(10,39),(11,40),(15,41),(16,22),(17,23),(18,24),(14,25);
	