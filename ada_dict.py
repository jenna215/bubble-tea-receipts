import math

def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):

  total = 0
  tea_base_flavors_prices = {
    "milk":4.35,
    "oolong":4.60,
    "rose":5.85,
    "mango":5.47
  }
  if tea_base == "milk":
    total += (tea_base_flavors_prices["milk"])
  if tea_base == "oolong":
    total += (tea_base_flavors_prices["oolong"])
  if tea_base == "rose":
    total += (tea_base_flavors_prices["rose"])
  if tea_base == "mango":
    total += (tea_base_flavors_prices["mango"])
  if loyalty_discount == True:
    total -= 1.00
   
  add_ons_flavors_prices = {
    "boba":0.50,
    "lychee":0.75,
    "jelly":0.65,
    "taro":1.00,
    "chia":0.35
  }

  for choices in range(0,len(add_ons)):
    if "boba" in add_ons:
      total += (add_ons_flavors_prices["boba"])
    if "lychee" in add_ons:
      total += (add_ons_flavors_prices["lychee"])
    if "jelly" in add_ons:
      total += (add_ons_flavors_prices["jelly"])
    if "taro" in add_ons:
      total += (add_ons_flavors_prices["taro"])            
    if "chia" in add_ons:
      total += (add_ons_flavors_prices["chia"])
    else:
      break
  return (print(f"The cost is ${'{:.2f}'.format(total)}"))

bubble_tea_calculator("milk", ["boba", "jelly", "taro"], False)