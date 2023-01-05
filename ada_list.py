import math
def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):
 
    total = []
 
    tea_base_flavors = ["milk", "oolong", "rose", "mango"]
    tea_base_prices = [4.35, 4.60, 5.85, 5.47]
    if tea_base_flavors[0] in tea_base:
        total.append(tea_base_prices[0])
    if tea_base_flavors[1] in tea_base:
        total.append(tea_base_prices[1])
    if tea_base_flavors[2] in tea_base:
        total.append(tea_base_prices[2])
    if tea_base_flavors[3] in tea_base:
        total.append(tea_base_prices[3])
    if loyalty_discount == True:
        total.append(-1.00)

    add_ons_flavors = ["boba", "lychee", "jelly", "taro", "chia"]
    add_ons_prices = [0.50, 0.75, 0.65, 1.00, 0.35]
    for choices in add_ons:
        if add_ons_flavors[0] in add_ons:
            total.append(add_ons_prices[0])
        if add_ons_flavors[1] in add_ons:
            total.append(add_ons_prices[1])
        if add_ons_flavors[2] in add_ons:
            total.append(add_ons_prices[2])
        if add_ons_flavors[3] in add_ons:
            total.append(add_ons_prices[3])
        if add_ons_flavors[4] in add_ons:
            total.append(add_ons_prices[4])
        else:
            break

    return (print(f"The cost is ${math.fsum(total):.2f}"))
bubble_tea_calculator("milk", ["boba", "jelly", "taro"], False)