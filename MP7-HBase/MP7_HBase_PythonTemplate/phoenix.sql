DROP VIEW IF EXISTS "powers";
CREATE VIEW "powers" (pk VARCHAR PRIMARY KEY, "professional"."name" VARCHAR, "personal"."power" VARCHAR, "personal"."hero" VARCHAR);
SELECT p."professional"."name" AS "Name1", p1."professional"."name" AS "Name2", p."personal"."power" AS "Power"
FROM "powers" as p
INNER JOIN "powers" as p1
ON p."personal"."power" = p1."personal"."power"
WHERE p."personal"."hero" = 'yes' AND p1."personal"."hero" = 'yes';
