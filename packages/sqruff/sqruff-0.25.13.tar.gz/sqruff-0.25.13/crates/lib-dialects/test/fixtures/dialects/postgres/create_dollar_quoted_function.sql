CREATE FUNCTION foo(integer, integer) RETURNS integer
    AS $$ select $1 + $2; $$
    LANGUAGE SQL;
