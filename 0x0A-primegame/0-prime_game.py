#!/usr/bin/python3
"""Prime Game"""


def isPrime(num):
    """check for prime behaviour"""
    if num <= 1:
        return False
    for n in range(2, (num // 2) + 1):
        if num % n == 0:
            return False
    return True


def isWinner(x, nums):
    """
    ### Returns the winner of the prime game;
    - The person with the most wins after `x` rounds of
    choosing prime numbers between `1 - n` in `nums` array of `n's`
    wins
    """
    players_score = {'Maria': 0, 'Ben': 0}

    if len(nums) == 0 or x == 0:
        return None

    for game_rounds in range(x):
        # set the number to consider from the index of
        # the game round
        n = nums[game_rounds]

        # set the list from 1 to n
        list_n = [num for num in range(1, n + 1)]

        # player 0 -> Maria, player 1 -> Ben
        player = 0
        curr_list = list_n.copy()

        for num in curr_list:

            # Increment the score of the player that chose last
            # or if the only number in the list id not a prime
            # Ben gets the score
            if not isPrime(num) and len(curr_list) == 1:
                if player == 1:
                    players_score['Maria'] += 1
                elif player == 0:
                    players_score['Ben'] += 1
                break

            # Check Maria's
            if player == 0:

                # if number is prime, remove all multiples from the list
                if isPrime(num):
                    curr_list = [n for n in curr_list if n % num != 0]

                    # switch the player
                    player += 1

                    # If the last integer in the list is not a prime,
                    # increment the score for player, player wins this round
                    if len(curr_list) == 1 and not isPrime(curr_list[0]):
                        players_score['Maria'] += 1
                        break

            # same rules as above apply to player 1
            elif player == 1:

                if isPrime(num):
                    curr_list = [n for n in curr_list if n % num != 0]

                    # switch player
                    player -= 1

                    if len(curr_list) == 1 and not isPrime(curr_list[0]):
                        players_score['Ben'] += 1
                        break

    # return winner - player with the highest score
    if players_score.get('Maria') > players_score.get('Ben'):
        return 'Maria'
    elif players_score.get('Maria') < players_score.get('Ben'):
        return 'Ben'
    return None
