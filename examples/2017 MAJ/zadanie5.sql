-- Druzyny   - Id_druzyny	Nazwa	        Miasto
-- Sedziowie - Nr_licencji	Imie	        Nazwisko
-- Wyniki    - Data_meczu	Rodzaj_meczu	Gdzie	Id_druzyny	Nr_licencji	Bramki_zdobyte	Bramki_stracone

--1 a)
SELECT TOP 1 * FROM
(SELECT COUNT(Rodzaj_meczu) FROM Wyniki INNER JOIN Druzyny ON Druzyny.Id_druzyny = Wyniki.Id_druzyny
 WHERE Rodzaj_meczu = 'T'
   AND Druzyny.Miasto = 'Kucykowo') AS towarzyski,
(SELECT COUNT(Rodzaj_meczu) FROM Wyniki INNER JOIN Druzyny ON Druzyny.Id_druzyny = Wyniki.Id_druzyny
 WHERE Rodzaj_meczu = 'L'
   AND Druzyny.Miasto = 'Kucykowo') AS ligowy,
(SELECT COUNT(Rodzaj_meczu) FROM Wyniki INNER JOIN Druzyny ON Druzyny.Id_druzyny = Wyniki.Id_druzyny
 WHERE Rodzaj_meczu = 'P'
   AND Druzyny.Miasto = 'Kucykowo') AS pucharowy

--1 b)
SELECT TOP 1 YEAR(Data_meczu) AS rok, SUM(1) AS ilosc
  FROM Wyniki INNER JOIN Druzyny ON Druzyny.Id_druzyny = Wyniki.Id_druzyny
 WHERE Druzyny.Miasto = 'Kucykowo'
 GROUP BY YEAR(Data_meczu)
 ORDER BY 2 DESC

 --2
SELECT Nazwa FROM
(SELECT Nazwa, SUM(Bramki_zdobyte) AS a, SUM(Bramki_stracone) AS b
  FROM Wyniki INNER JOIN Druzyny ON Druzyny.Id_druzyny = Wyniki.Id_druzyny
 GROUP BY Nazwa)
WHERE a=b

--3
SELECT TOP 1 * FROM
(SELECT COUNT(Rodzaj_meczu) FROM Wyniki
 WHERE Bramki_stracone < Bramki_zdobyte
   AND Gdzie = 'W') AS wygranych,
(SELECT COUNT(Rodzaj_meczu) FROM Wyniki
 WHERE Bramki_stracone > Bramki_zdobyte
   AND Gdzie = 'W') AS przegranych,
(SELECT COUNT(Rodzaj_meczu) FROM Wyniki
 WHERE Bramki_stracone = Bramki_zdobyte
   AND Gdzie = 'W') AS zremisowanych

--4
SELECT COUNT(*) FROM Sedziowie
WHERE Nr_licencji NOT IN (SELECT DISTINCT Sedziowie.Nr_licencji
  FROM Wyniki INNER JOIN Sedziowie ON Sedziowie.Nr_licencji = Wyniki.Nr_licencji
WHERE Rodzaj_meczu = 'P')