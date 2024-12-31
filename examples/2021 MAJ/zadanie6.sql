-- Gracze    - id_gracza     kraj        data_dolaczenia
-- Klasy     - nazwa         sila        strzal           magia  szybkosc
-- Jednostki - id_jednostki  id_gracza   nazwa            lok_x  lok_y

-- TRIPLE - (Gracze INNER JOIN Jednostki ON Gracze.id_gracza = Jednostki.id_gracza) INNER JOIN Klasy ON Jednostki.nazwa = Klasy.nazwa
-- Jednostki-Klasy - Jednostki INNER JOIN Klasy ON Jednostki.nazwa = Klasy.nazwa
-- Jednostki-Gracze - Gracze INNER JOIN Jednostki ON Gracze.id_gracza = Jednostki.id_gracza
--1
SELECT TOP 5 kraj, COUNT(*) AS licaba_graczy
  FROM Gracze
 WHERE YEAR(data_dolaczenia) = 2018
 GROUP BY kraj
 ORDER BY 2 DESC

--2
SELECT Jednostki.nazwa, SUM(strzal)
  FROM Jednostki INNER JOIN Klasy ON Jednostki.nazwa = Klasy.nazwa
 WHERE Jednostki.nazwa LIKE '*elf*'
 GROUP BY Jednostki.nazwa

SELECT nazwa, SUM(strzal)
  FROM Klasy
 WHERE nazwa LIKE '*elf*'
 GROUP BY nazwa

--3
SELECT id_gracza
  FROM Gracze
 WHERE id_gracza
   NOT IN (
       SELECT Jednostki.id_gracza
         FROM Gracze INNER JOIN Jednostki ON Gracze.id_gracza = Jednostki.id_gracza
        WHERE Jednostki.nazwa = 'artylerzysta'
       )
--4
SELECT Jednostki.nazwa, COUNT(*)
  FROM Jednostki INNER JOIN Klasy ON Jednostki.nazwa = Klasy.nazwa
 WHERE ABS(lok_x - 100) + ABS(lok_y - 100) <= szybkosc
 GROUP BY Jednostki.nazwa

--5(a)
SELECT COUNT(*)
  FROM (
SELECT COUNT(*) AS counter
  FROM Jednostki AS a, Jednostki AS b
 WHERE a.lok_x = b.lok_x
   AND a.lok_y = b.lok_y
   AND a.id_gracza <> b.id_gracza
 GROUP BY a.lok_x, a.lok_y
 )
 WHERE counter > 1

 --5(b)
SELECT COUNT(*)
  FROM (
SELECT COUNT(*) AS counter
  FROM (SELECT * FROM Jednostki INNER JOIN Gracze ON Jednostki.id_gracza = Gracze.id_gracza) AS a,
       (SELECT * FROM Jednostki INNER JOIN Gracze ON Jednostki.id_gracza = Gracze.id_gracza) AS b
 WHERE a.lok_x = b.lok_x
   AND a.lok_y = b.lok_y
   AND a.Jednostki.id_gracza <> b.Jednostki.id_gracza
   AND 'Polska' IN (a.kraj, b.kraj)
 GROUP BY a.lok_x, a.lok_y
 )
 WHERE counter > 1