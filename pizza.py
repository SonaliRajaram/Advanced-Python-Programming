def make_pizza(size, *toppings):
    print(f"\n Making a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"-{toppings}")

make_pizza(16,"pepperoni")
make_pizza(22,"pepperoni","mushrooms", "green pepper","extra cheese")