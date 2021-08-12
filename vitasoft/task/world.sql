CREATE TABLE q_states AS
    SELECT states.name as name, countries.name as country_name
    FROM states INNER JOIN countries ON states.country_id = countries.id;

CREATE TABLE q_countries AS
    SELECT countries.name as name, countries.phonecode as phonecode
    FROM countries;
