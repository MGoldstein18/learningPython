/* Analyzing temperature data for states in the USA over the last +-100 year */
SELECT * FROM state_climate;

SELECT state, year, tempf, AVG(tempc) OVER (
  PARTITION BY state
  ORDER BY year
) running_avg_temp
FROM state_climate;

SELECT state, year, tempf, tempc, FIRST_VALUE(tempc) OVER(
  PARTITION BY state
  ORDER BY tempc
) lowest_temp 
FROM state_climate;

SELECT state, year, tempf, tempc, LAST_VALUE(tempc) OVER(
  PARTITION BY state
  ORDER BY tempc
  RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) highest_temp
FROM state_climate;

SELECT state, year, tempf, tempc, LAG(tempc, 1, 0) OVER (
  PARTITION BY state
  ORDER BY year
) change_in_temp
FROM state_climate ORDER BY change_in_temp DESC;

SELECT year, state, tempf, tempc, RANK() OVER(
  ORDER BY tempc
) coldest_rank
FROM state_climate;

SELECT year, state, tempf, tempc, RANK() OVER(
  PARTITION BY state
  ORDER BY tempc DESC
) warmest_rank
FROM state_climate;

SELECT year, state, tempf, tempc, NTILE(4) OVER(
  PARTITION BY state
  ORDER BY tempc
) quartile
FROM state_climate;

SELECT year, state, tempf, tempc, NTILE(5) OVER(
  ORDER BY tempc
) quintile
FROM state_climate;





