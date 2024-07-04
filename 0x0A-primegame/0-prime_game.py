#!/usr/bin/python3
def isWinner(x, nums):
    max_wins = 0
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        multiples = [n for n in nums if n % nums[i] == 0]
        nums = [n for n in nums if n not in multiples]
        if len(nums) == 0:
            if i % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1
        if i % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
