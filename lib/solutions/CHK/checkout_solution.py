# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    items = {
        "A": {"price": 50, "deals": [{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}]},
        "B": {"price": 30, "deals": [{"quantity": 2, "price": 45}]},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "free_items": {"quantity": 2, "item": "B"}}
    }

    total_cost = 0
    all_items = dict.fromkeys(items, 0)

    for sku in skus:
        if sku in items:
            all_items[sku] += 1
        else:
            return -1

    # Checks for free items and removes from shopping list
    for item, item_details in items.items():

        item_count = all_items[item]

        if item_details.get("free_items") and item_count:
            free_items = item_details["free_items"]
            quantity_required = item_details["free_items"]["quantity"]
            free_item = item_details["free_items"]["item"]

            complete_deals = item_count // quantity_required
            all_items[free_item] -= complete_deals

            if all_items[free_item] < 0:
                all_items[free_item] = 0

    # Charges for items left in shopping cart (with deals)
    for item, item_details in items.items():

        item_price = item_details["price"]
        item_deals = item_details.get("deals")

        item_count = all_items[item]

        available_deals = []

        if item_details.get("deals"):

            for deal in item_deals:

                item_deal_quantity = deal["quantity"]
                item_deal_price = deal["price"]

                complete_deals = item_count//item_deal_quantity
                total_cost += (complete_deals * item_deal_price)

                item_count -= complete_deals * item_deal_quantity

        total_cost += (item_count*item_price)

    return total_cost
