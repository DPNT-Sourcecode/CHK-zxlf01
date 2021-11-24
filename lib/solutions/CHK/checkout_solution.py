

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    item_prices = {
        "A": {"price": 50, "deal_quantity": 3, "deal_price": 130},
        "B": {"price": 30, "deal_quantity": 2, "deal_price": 45},
        "C": {"price": 20},
        "D": {"price": 15}
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
            total_value += (complete_deals * item_deal_price) + \
                           (item_count - ((complete_deals*item_deal_quantity)*item_price))
        else:
            total_value += (item_count*item_price)

    print(total_value)
    return total_value

checkout("ABD")
