'''
You have m types of coins available in infinite quantities,
where the value of each coin is given in the array S=[S0, ..., Sm-1]
Can you determine the number of ways of making change for n units using
the given types of coins?
'''

def dp_count(N, coins):
    
    ways = [0]*(N + 1)

    ways[0] = 1

    for i in range(len(coins)):

        for j in range(len(ways)):

            if coins[i] <= j:
                ways[j] += ways[(int)(j - coins[i])]
    
    return ways[N]