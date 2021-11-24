# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    items = {
        "A": {"price": 50, "deals": [{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}]},
        "B": {"price": 30, "deals": [{"quantity": 2, "price": 45}]},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "free_items": {"quantity": 2, "item": "B"}},
        "F": {"price": 10, "free_items": {"quantity": 3, "item": "F"}},
        "G": {"price": 20},
        "H": {"price": 10, "deals": [{"quantity": 10, "price": 80}, {"quantity": 5, "price": 45}]},
        "I": {"price": 35},
        "J": {"price": 60},
        "K": {"price": 80, "deals": [{"quantity": 2, "price": 150}]},
        "L": {"price": 90},
        "M": {"price": 15},
        "N": {"price": 40, "free_items": {"quantity": 3, "item": "M"}},
        "O": {"price": 10},
        "P": {"price": 50, "deals": [{"quantity": 5, "price": 200}]},
        "Q": {"price": 30, "deals": [{"quantity": 3, "price": 80}]},
        "R": {"price": 50, "free_items": {"quantity": 3, "item": "Q"}},
        "S": {"price": 30},
        "T": {"price": 20},
        "U": {"price": 40, "free_items": {"quantity": 4, "item": "U"}},
        "V": {"price": 50, "deals": [{"quantity": 3, "price": 130}, {"quantity": 2, "price": 90}]},
        "W": {"price": 20},
        "X": {"price": 90},
        "Y": {"price": 10},
        "Z": {"price": 50}
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
