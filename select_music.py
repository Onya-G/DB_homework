import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/music')
con = engine.connect()

print('количество исполнителей в каждом жанре')
print(con.execute("""
SELECT g.name, COUNT(gm.genre_id) FROM genres g
JOIN genre_musician gm ON g.id = gm.genre_id
GROUP BY g.name
""").fetchall())

print('количество треков, вошедших в альбомы 2019-2020 годов')
print(con.execute("""
SELECT a.name, COUNT(t.album_id) FROM albums a
JOIN tracks t ON a.id = t.album_id
WHERE year BETWEEN 2019 AND 2020                                    
GROUP BY a.name
""").fetchall())

print('средняя продолжительность треков по каждому альбому')
print(con.execute("""
SELECT a.name, AVG(t.time) FROM albums a
JOIN tracks t ON a.id = t.album_id
GROUP BY a.name
""").fetchall())

print('все исполнители, которые не выпустили альбомы в 2020 году')
print(set(con.execute("""
SELECT m.name FROM musicians m
JOIN musician_album ma ON m.id = ma.musician_id
JOIN albums a ON a.id = ma.album_id
WHERE m.name NOT IN (
SELECT m.name FROM musicians m
JOIN musician_album ma ON ma.musician_id = m.id
JOIN albums a ON a.id = ma.album_id
WHERE a.year = 2020
)""").fetchall()))

print('названия сборников, в которых присутствует конкретный исполнитель')
print(con.execute("""
SELECT mt.name, m.name FROM mixtapes mt
JOIN mixtape_track mtt ON mt.id = mtt.mixtape_id
JOIN tracks t ON t.id = mtt.track_id
JOIN albums a ON a.id = t.album_id
JOIN musician_album ma ON ma.album_id = a.id
JOIN musicians m ON m.id = ma.musician_id
WHERE m.name = 'Merenga'
""").fetchall())

print('название альбомов, в которых присутствуют исполнители более 1 жанра')
print(con.execute("""
SELECT m.name, COUNT(gm.genre_id) FROM musicians m
JOIN genre_musician gm ON m.id = gm.musician_id
JOIN genres g ON g.id = gm.genre_id
GROUP BY m.name
HAVING COUNT(gm.genre_id) > 1
""").fetchall())

print('наименование треков, которые не входят в сборники')
print(con.execute("""
SELECT t.name, COUNT(mt.id) FROM tracks t
JOIN mixtape_track mtt ON t.id = mtt.track_id
JOIN mixtapes mt ON mt.id = mtt.mixtape_id
GROUP BY t.name
HAVING COUNT(mt.id) = 0
""").fetchall())

print(
    'исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)')
print(con.execute("""
SELECT m.name, t.name, t.time FROM musicians m
JOIN musician_album ma ON m.id = ma.musician_id
JOIN albums a ON a.id = ma.album_id
JOIN tracks t ON t.album_id = a.id
WHERE t.time = (SELECT MIN(time) FROM tracks)
""").fetchall())

print('название альбомов, содержащих наименьшее количество треков')
print(con.execute("""
SELECT a.name, COUNT(t.album_id) FROM albums a
JOIN tracks t ON t.album_id = a.id
GROUP BY a.name
HAVING COUNT(t.album_id) = (
SELECT MIN(tc) FROM (SELECT COUNT(t.album_id) tc FROM albums a
JOIN tracks t ON t.album_id = a.id
GROUP BY a.name) tmp)
""").fetchall())
