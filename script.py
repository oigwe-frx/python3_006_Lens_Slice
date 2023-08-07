
# To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

toppings = ["pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"];

# To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:

prices = [2,
6,
1,
3,
2,
7,
2 ]

# Your boss wants you to do some research on $2 slices.

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

# Find the length of the toppings list and store it in a variable called num_pizzas.

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")


# Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

pizza_and_prices = []

i = 0

while i < len(prices):
    pizza_and_prices.append([prices[i],toppings[i]])
    i+=1

# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).

pizza_and_prices.sort()

#Store the first element of pizza_and_prices in a variable called cheapest_pizza.

cheapest_pizza = pizza_and_prices[0]

# A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

priciest_pizza = pizza_and_prices[-1]

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()

# Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. 

pizza_and_prices.append([2.5, "peppers"])

pizza_and_prices.sort()

print(pizza_and_prices)


