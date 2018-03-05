## 1. Introducing Joins ##

select * from facts;
select * from cities;
select * from cities inner join facts on facts.id = cities.facts_id limit 10;
select * from facts inner join cities on facts.id = cities.facts_id limit 10;

## 2. Understanding Inner Joins ##

select c.*,f.name as country_name from facts as f inner join cities c on f.id=c.facts_id limit 5

## 3. Practicing Inner Joins ##

select f.name as country, c.name as capital_city from facts as f inner join cities as c on f.id  = c.facts_id where c.capital=1

## 4. Left Joins ##

SELECT f.name country, f.population
FROM facts f
LEFT JOIN cities c ON c.facts_id = f.id
WHERE c.name IS NULL;

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name capital_city, f.name country, c.population
FROM facts f
INNER JOIN cities c ON c.facts_id = f.id
WHERE c.capital = 1
ORDER BY 3 DESC
LIMIT 10;

## 7. Combining Joins with Subqueries ##

select c.name as capital_city, f.name as country, c.population as population from facts f inner join (select * from cities where capital = 1 and population>10000000) c on facts_id = f.id order by 3 desc;

## 8. Challenge: Complex Query with Joins and Subqueries ##

select f.name country,c.urban_pop, f.population total_pop, (c.urban_pop /CAST(f.population as float)) urban_pct from facts f
inner join (select facts_id, SUM(population) urban_pop from cities group by 1) c on c.facts_id = f.id
where urban_pct > .5
order by 4 asc;