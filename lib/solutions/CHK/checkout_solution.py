# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    item_prices = {
        "A": {"price": 50, "deals": [{"quantity": 3, "price": 130}, {"quantity": 5, "price": 200}]},
        "B": {"price": 30, "deals": [{"quantity": 2, "price": 45}]},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "deals": [{"quantity": 3, "price": 80}]}
    }

    total_value = 0
    all_items = []

    for sku in skus:
        if sku in item_prices:
            all_items.append(sku)
        else:
            return -1

    for item, item_details in item_prices.items():

        item_price = item_details["price"]
        item_deal_quantity = item_details.get("deal_quantity")
        item_deal_price = item_details.get("deal_price")

        item_count = all_items.count(item)

        if item_deal_quantity:
            complete_deals = item_count//item_deal_quantity
            total_value += (complete_deals * item_deal_price)
            item_count -= complete_deals * item_deal_quantity

        total_value += (item_count*item_price)

    return total_value


