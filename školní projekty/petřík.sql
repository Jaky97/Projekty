--vytvořím uživatele s heslem
CREATE USER 'jan'@'localhost' IDENTIFIED BY 'Xa5*s23_9';
CREATE USER 'eva'@'localhost' IDENTIFIED BY 'Yb6*t24_0';

--vytvořím roli s funkcemi
CREATE ROLE 'ucetni'; -- prázdná role
GRANT SELECT, INSERT,UPDATE -- co to muže používat 
ON firma.faktury -- Kde se to muže používat
TO 'ucetni' --jaká role

--přidam roli uživatelům
GRANT 'ucetni' TO 'jan'@'localhost';
GRANT 'ucetni' TO 'eva'@'localhost';

--přidání funkce roli
GRANT DELETE
ON firma.faktury
TO 'ucetni';

--odebrání funkce z role
REVOKE DELETE
ON firma.faktury
FROM 'ucetni';

--odebrání uživatele
DROP USER 'jan'@'localhost'