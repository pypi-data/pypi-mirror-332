INSERT INTO foo SELECT 0 AS bar;

INSERT INTO foo (SELECT 1 AS bar);

INSERT INTO foo ((SELECT 1 AS bar));
