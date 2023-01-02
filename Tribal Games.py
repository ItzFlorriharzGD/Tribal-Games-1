print('***********************************\n ''The Tribal Games: Bananas for Sale\n ''Game By Kellan Franklin\n''***********************************\n ')
bananas_grow = eval(input('How many bananas do you want to grow?\n'))
print('Your tribe grew',bananas_grow, 'bananas.')
bananas_to_sell = eval(input('How many bananas do you to sell?\n'))
sell_for = eval(input('How much would you like to sell them for?\n'))
print('Your tribe sold', bananas_to_sell, 'bananas and sold them for',sell_for,'dollars')
money = bananas_to_sell*sell_for
print('Your tribe got',money,'dollars')