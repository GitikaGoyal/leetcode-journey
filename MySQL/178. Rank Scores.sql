-- You can achieve the desired ranking using the DENSE_RANK() window function in SQL. This function assigns consecutive ranks without gaps even when there are ties.
SELECT  score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores ORDER BY score DESC;
