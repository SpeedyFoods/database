select u.first_name, u.last_name from User u where NOT EXISTS
(select * from Restaurant r where NOT EXISTS 
(select o.consumer_id from _Order o where
u.user_id=o.consumer_id AND r.restaurant_id=o.restaurant_id));