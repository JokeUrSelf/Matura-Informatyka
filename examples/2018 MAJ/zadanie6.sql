-- Komputery - Numer_komputera	Sekcja	        Pojemnosc_dysku
-- Awarie    - Numer_zgloszenia	Numer_komputera	Czas_awarii	    Priorytet
-- Naprawy   - Numer_zgloszenia	Czas_naprawy	Rodzaj

-- TRIPLE - Naprawy INNER JOIN (Awarie INNER JOIN Komputery ON Awarie.Numer_komputera = Komputery.Numer_komputera) ON Naprawy.Numer_zgloszenia = Awarie.Numer_zgloszenia
-- Awarie-Naprawy - Naprawy INNER JOIN Awarie ON Naprawy.Numer_zgloszenia = Awarie.Numer_zgloszenia
-- Komputery-Awarie - Awarie INNER JOIN Komputery ON Awarie.Numer_komputera = Komputery.Numer_komputera

--1
SELECT TOP 10 Pojemnosc_dysku, SUM(1) AS ilosc
  FROM Komputery
 GROUP BY Pojemnosc_dysku
 ORDER BY 2 DESC

--2
SELECT Awarie.Numer_komputera, liczba_wym
  FROM (SELECT Awarie.Numer_komputera, SUM(1) AS liczba_wym
          FROM Naprawy INNER JOIN (Awarie INNER JOIN Komputery ON Awarie.Numer_komputera = Komputery.Numer_komputera) ON Naprawy.Numer_zgloszenia = Awarie.Numer_zgloszenia
         WHERE Sekcja = 'A'
           AND Rodzaj = 'wymiana'
         GROUP BY Awarie.Numer_komputera)
 WHERE liczba_wym >= 10

--3
SELECT TOP 1 DateValue(Czas_awarii) AS Dzien_Awarii, Komputery.Sekcja
  FROM Komputery INNER JOIN Awarie ON Komputery.Numer_komputera = Awarie.Numer_komputera
 GROUP BY DateValue(Czas_awarii), Komputery.Sekcja
 ORDER BY Sum(1) DESC

--4
SELECT TOP 1 Awarie.Numer_zgloszenia, Czas_awarii, Czas_naprawy
  FROM Naprawy INNER JOIN Awarie ON Naprawy.Numer_zgloszenia = Awarie.Numer_zgloszenia
 ORDER BY Czas_naprawy - Czas_awarii DESC

--5
SELECT COUNT(*) FROM Komputery
 WHERE Numer_komputera
NOT IN (SELECT Numer_komputera FROM Awarie WHERE Priorytet >= 8)