/*
Teo SPeece
Weather Observation Station 3
One of challenges on Basic Select onHackerWars
Instructions: Query a list of CITY names from STATION for 
cities that have an even ID number. Print the results in any 
order, but exclude duplicates from the answer.
*/

select distinc(CITY) from STATION 
where (ID % 2) = 0;
