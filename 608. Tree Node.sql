# Write your MySQL query statement below
with 
joined AS(
select l.id, "Inner" as type from Tree l, Tree r WHERE l.id = r.p_id GROUP BY l.id
),
root AS(
select id, "Root" as type from Tree WHERE p_id is NULL
)
SELECT id, type FROM joined WHERE ID NOT IN (SELECT ID FROM root)
UNION
SELECT id, type FROM root
UNION 
SELECT id, "Leaf" as type FROM Tree WHERE ID NOT IN (SELECT ID FROM joined UNION SELECT ID FROM root)
ORDER BY id;
