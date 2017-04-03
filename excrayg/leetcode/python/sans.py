def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
	    for j in xrange(coin, amount + 1):
	    	for coin in coins:
	    		if (j-coin)>=0:
	    			ways[j] += ways[j - coin]

    return ways[amount]


print(changes(3, [1,2]))