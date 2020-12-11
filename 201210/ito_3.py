DISCOUNT = 15
def apply_discount(price, discount):
    return price * (100 - discount) / 100


basket = [5464.7, 2342.8, 45784.5, 3457.3]
basket_sum = sum(basket)
print(basket_sum)
basket_sum_discounted = 0
discount_1 = 7
for product in basket:
    basket_sum_discounted += apply_discount(product, discount_1)
print(basket_sum_discounted)
