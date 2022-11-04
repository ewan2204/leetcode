with 
big AS(
SELECT sales_id FROM COMPANY NATURAL JOIN ORDERS WHERE name = "RED"
)
SELECT name FROM SALESPERSON WHERE sales_id NOT IN (select * from big);
