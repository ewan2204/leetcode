select customer_number from Orders GROUP BY customer_number ORDER BY COUNT(Order_number) DESC LIMIT 1
