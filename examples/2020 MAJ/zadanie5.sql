-- Jezyki      - Jezyk	    Rodzina
-- Uzytkownicy - Panstwo	Jezyk	    Uzytkownicy	    Urzedowy
-- Panstwa     - Panstwo	Kontynent	Populacja

-- Triple - FROM (Jezyki INNER JOIN Uzytkownicy ON Jezyki.Jezyk = Uzytkownicy.Jezyk) INNER JOIN Panstwa ON Uzytkownicy.Panstwo = Panstwa.Panstwo

--1
SELECT Rodzina, COUNT(*)
  FROM Jezyki
 GROUP BY Rodzina
 ORDER BY 2 DESC

--2
SELECT COUNT(*) FROM (
SELECT DISTINCT Jezyk FROM Uzytkownicy
 WHERE Jezyk NOT IN (SELECT Jezyk FROM Uzytkownicy WHERE Urzedowy = 'tak')
)
 --3
SELECT Jezyk
 FROM (
      SELECT Jezyk, COUNT(*) AS kon
        FROM (SELECT DISTINCT Kontynent, Jezyk FROM Uzytkownicy INNER JOIN Panstwa ON Uzytkownicy.Panstwo = Panstwa.Panstwo)
       GROUP BY Jezyk
 )
WHERE kon >=4

--4
SELECT TOP 6 Uzytkownicy.Jezyk, Rodzina, round(sum(Uzytkownicy.Uzytkownicy),1) AS liczba_mieszkancow
  FROM (Jezyki INNER JOIN Uzytkownicy ON Jezyki.Jezyk = Uzytkownicy.Jezyk) INNER JOIN Panstwa ON Uzytkownicy.Panstwo = Panstwa.Panstwo
 WHERE Kontynent IN ('Ameryka Polnocna', 'Ameryka Poludniowa')
   AND Rodzina <> 'indoeuropejska'
 GROUP BY Uzytkownicy.Jezyk, Rodzina
 ORDER BY 3 DESC

--5
SELECT Uzytkownicy.Panstwo, Jezyk, MAX(Uzytkownicy.Uzytkownicy / Populacja * 100) AS Procent
  FROM Uzytkownicy INNER JOIN Panstwa ON Uzytkownicy.Panstwo = Panstwa.Panstwo
 WHERE Populacja *0.3 <= Uzytkownicy.Uzytkownicy
   AND Urzedowy = 'nie'
 GROUP BY Uzytkownicy.Panstwo, Jezyk