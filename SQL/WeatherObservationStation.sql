/*
Teo SPeece
Weather Observation Station 3
This was the 10th challenge which completed the basic select
challenges on HackerWars
Instructions: Query a list of CITY names from STATION for 
cities that have an even ID number. Print the results in any 
order, but exclude duplicates from the answer.
*/

select distinc(CITY) from STATION 
where (ID % 2) = 0;