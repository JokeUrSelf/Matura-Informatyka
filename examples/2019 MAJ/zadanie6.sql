-- Marki - id_marki, nazwa_m
-- Perfumy - id_perfum, nazwa_p, id_marki, rodzina_zapachow, cena
-- Sklad - id_perfum, nazwa_skladnika

SELECT DISTINCT nazwa_m, rodzina_zapachow
  FROM (SELECT nazwa_m, Marki.id_marki
          FROM (SELECT id_marki FROM Perfumy GROUP BY id_marki, rodzina_zapachow) AS A
         INNER JOIN Marki
            ON Marki.id_marki = A.id_marki
         GROUP BY nazwa_m, Marki.id_marki
        HAVING SUM(1) = 1) AS B
 INNER JOIN Perfumy
    ON Perfumy.id_marki = B.id_marki

-- Zadanie 6.1:
SELECT nazwa_p
  FROM Sklad
 INNER JOIN Perfumy
    ON Sklad.id_perfum = Perfumy.id_perfum
 WHERE nazwa_skladnika = 'absolut jasminu'

-- Zadanie 6.2:
SELECT a.rodzina_zapachow,
       a.cena,
       nazwa_p
  FROM (SELECT rodzina_zapachow, MIN(cena) AS cena
          FROM Perfumy
         GROUP BY rodzina_zapachow) AS a
 INNER JOIN Perfumy AS b
    ON a.rodzina_zapachow = b.rodzina_zapachow
   AND a.cena = b.cena

-- Zadanie 6.3:
SELECT nazwa_m
  FROM Marki
 WHERE nazwa_m
NOT IN (SELECT nazwa_m
          FROM (Marki INNER JOIN Perfumy ON Marki.id_marki = Perfumy.id_marki)
         INNER JOIN Sklad
            ON Perfumy.id_perfum = Sklad.id_perfum
         WHERE nazwa_skladnika LIKE '*paczula*')
 ORDER BY nazwa_m

-- Zadanie 6.4:
SELECT nazwa_p, cena * 0.85
  FROM Marki INNER JOIN Perfumy ON Marki.id_marki = Perfumy.id_marki
 WHERE nazwa_m = 'Mou De Rosine'
   AND rodzina_zapachow = 'orientalno-drzewna'
 ORDER BY 2

-- Zadanie 6.5:
SELECT DISTINCT nazwa_m, rodzina_zapachow
  FROM Marki
 INNER JOIN Perfumy
    ON Marki.id_marki = Perfumy.id_marki
 WHERE nazwa_m
    IN (SELECT nazwa_m FROM
       (SELECT nazwa_m, SUM(1) AS di
          FROM (SELECT DISTINCT nazwa_m, rodzina_zapachow
                  FROM Marki
                 INNER JOIN Perfumy
                    ON Marki.id_marki = Perfumy.id_marki)
         GROUP BY nazwa_m)
         WHERE di = 1)

--Zadanie 6.5 (второй вариант)
SELECT DISTINCT nazwa_m, rodzina_zapachow
  FROM (SELECT nazwa_m, Marki.id_marki
          FROM (SELECT id_marki FROM Perfumy GROUP BY id_marki, rodzina_zapachow) AS A
         INNER JOIN Marki
            ON Marki.id_marki = A.id_marki
         GROUP BY nazwa_m, Marki.id_marki
        HAVING SUM(1) = 1) AS B
 INNER JOIN Perfumy
    ON Perfumy.id_marki = B.id_marki