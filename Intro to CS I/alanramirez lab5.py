## Alan Ramirez
print("Welcome to the Italian restaurant!\n")

def fail():
    print("\tInvalid option")
    exit()

food_type = str(input("\tWould you like pizza, pasta, or gelato?: "))
if food_type == "pizza":
    size = str(input("\tWould you like a small, medium, or large pizza?: "))
    if size == "small" or size == "medium" or size == "large":
        topping = str(input("\tWouid you like a pepperoni, hawaiian, or supreme pizza?: "))
        if topping == "pepperoni" or topping == "hawaiian" or topping == "supreme":
            print("\nYou ordered a {} {} {}!".format(size, topping, food_type))
        else:
            fail()
    else:
        fail()
elif food_type == "pasta":
    size = str(input("\tWould you like a small, medium, or large serving of pasta?: "))
    if size == "small" or size == "medium" or size == "large":
        pasta_type = str(input("\tWould you like fettuccine, rigatoni, or spaghetti?: "))
        if pasta_type == "fettuccine":
            sauce = str(input("\tWould you like bolognese or alfredo sauce?: "))
        elif pasta_type == "rigatoni":
            sauce = str(input("\tWould you like funghi e piselli sauce? Answer yes or no: "))
        elif pasta_type == "spaghetti":
            sauce = str(input("\tWould you like bolognese, ragu, marinara, or pesto sauce?: "))
        else:
            fail()
        print("\nYou ordered a {} portion of {} pasta with {} sauce!".format(size, pasta_type, sauce))
    else:
        fail()
elif food_type == "gelato":
    size = str(input("\tWould you like a small, medium, or large portion of gelato?: "))
    if size == "small" or size == "medium" or size == "large":
        flavor = str(input("\tWould you like a dark-chocolate, pistachio, raspberry, lemon, or tiramisu gelato?: "))
        if flavor == "dark-chocolate" or flavor == "pistachio" or flavor == "raspberry" or flavor == "lemon" or flavor == "tiramisu":
            topping = str(input("\tWould you like hot-fudge, sprinkles, caramel, chocolate-syrup, nuts, or no toppings on your gelato?: "))
            if topping == "hot-fudge" or topping == "sprinkles" or topping == "caramel" or topping == "chocolate-syrup" or topping == "nuts" or topping == "none":
                print("\nYou ordered a {} portion of {} gelato with a topping of {}!".format(size, flavor, topping))
            else:
                fail()
        else:
            fail()
    else:
        fail()
else:
    fail()