import sys
import random

RANK_STAR_TABLE = {
    25: 2,
    24: 2,
    23: 2,
    22: 2,
    21: 2,
    20: 3,
    19: 3,
    18: 3,
    17: 3,
    16: 3,
    15: 4,
    14: 4,
    13: 4,
    12: 4,
    11: 4,
    10: 5,
    9: 5,
    8: 5,
    7: 5,
    6: 5,
    5: 5,
    4: 5,
    3: 5,
    2: 5,
    1: 5,
}

def simulate(rank = 25, star = 0, winrate = 50, streaks = 0):
    if rank < 2:
        return (rank, star, winrate, streaks);
    if rank == 25 and star == 0:
        return (rank, star, winrate, streaks);

    win = random.randint(1, 100) <= winrate
    if win:
        print 'win'
        streaks = streaks + 1

        if rank > 5 and streaks > 2:
            star = star + 2
        else:
            star = star + 1

        if RANK_STAR_TABLE[rank] < star:
            rank = rank - 1
            star = star - RANK_STAR_TABLE[rank]
    else:
        print 'loss'
        streaks = 0
        star = star - 1
        if star < 0 and rank < 20:
            rank = rank + 1
            star = RANK_STAR_TABLE[rank] - 1
        else:
            star = 0

    return (rank, star, winrate, streaks)

if __name__ == '__main__':
    result = (20, 0, 55, 0)
    for i in range (100):
        result = simulate(*result)
        print result
