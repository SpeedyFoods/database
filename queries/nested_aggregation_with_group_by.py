cheapest_item_every = """
SELECT restaurant_name, MIN(price)
FROM Item, Restaurant
WHERE restaurant_name IN 
(SELECT restaurant_name
FROM Restaurant
WHERE Restaurant.restaurant_id = Item.restaurant_id)
GROUP BY restaurant_name;
"""