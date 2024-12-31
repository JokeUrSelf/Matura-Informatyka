-- Pakiety  - Id_pakietu	nazwa_pakietu	firma
-- Programy - Id_programu	program         rodzaj	cena
-- Zestawy  - Id_pakietu	Id_programu

-- Triple JOIN: Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu

--1
SELECT * FROM(
SELECT Programy.program, AVG(cena) AS cena_, COUNT(1) as liczba
  FROM Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu
 WHERE Programy.rodzaj='edytor dokumentow tekstowych'
 GROUP BY Programy.program
)
WHERE liczba>1

--2
SELECT DISTINCT nazwa_pakietu
  FROM Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu
 WHERE rodzaj LIKE '*zarzadzanie*'

--3
SELECT TOP 3 nazwa_pakietu, firma, SUM(cena) as cena_
  FROM Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu
 GROUP BY nazwa_pakietu, firma
 ORDER BY 3 DESC

--4
SELECT program FROM Programy
 WHERE program
NOT IN (SELECT program FROM Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu)

--5
SELECT a.nazwa_pakietu, liczba_komerc, liczba_free
  FROM (SELECT nazwa_pakietu, COUNT(program) AS liczba_free
          FROM Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu
         WHERE cena = 0
         GROUP BY nazwa_pakietu) AS a
 INNER JOIN
       (SELECT nazwa_pakietu, COUNT(program) AS liczba_komerc
          FROM Programy INNER JOIN (Pakiety INNER JOIN Zestawy ON Pakiety.Id_pakietu = Zestawy.Id_pakietu) ON Programy.Id_programu = Zestawy.Id_programu
         WHERE cena > 0
         GROUP BY nazwa_pakietu) AS b
    ON a.nazwa_pakietu = b.nazwa_pakietu
