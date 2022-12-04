# https://adventofcode.com/2022/day/2
STRATEGY_GUIDE_FILE_NAME = "strategy_guide.txt"
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3, 'win': 6, 'draw': 3, 'loss': 0}


def play_game_part_1():
    possible_outcomes = {
        'A X': 'draw', 'A Y': 'win', 'A Z': 'loss',
        'B X': 'loss', 'B Y': 'draw', 'B Z': 'win',
        'C X': 'win', 'C Y': 'loss', 'C Z': 'draw'
    }
    total_points = 0
    with open(STRATEGY_GUIDE_FILE_NAME) as strategy:
        for game_round in strategy:
            total_points += points[possible_outcomes[game_round.rstrip()]]
            total_points += points[game_round.rstrip().split(' ')[1]]
    print(f'Total points in part 1: {total_points}')


def play_game_part_2():
    possible_outcomes = {
        'A X': {'outcome': 'loss', 'pick': 'C'},
        'A Y': {'outcome': 'draw', 'pick': 'A'},
        'A Z': {'outcome': 'win', 'pick': 'B'},
        'B X': {'outcome': 'loss', 'pick': 'A'},
        'B Y': {'outcome': 'draw', 'pick': 'B'},
        'B Z': {'outcome': 'win', 'pick': 'C'},
        'C X': {'outcome': 'loss', 'pick': 'B'},
        'C Y': {'outcome': 'draw', 'pick': 'C'},
        'C Z': {'outcome': 'win', 'pick': 'A'}
    }
    total_points = 0
    with open(STRATEGY_GUIDE_FILE_NAME) as strategy:
        for game_round in strategy:
            total_points += points[possible_outcomes[game_round.rstrip()]['outcome']]
            total_points += points[possible_outcomes[game_round.rstrip()]['pick']]

    print(f'Total points in part 2: {total_points}')


if __name__ == "__main__":
    play_game_part_1()
    play_game_part_2()
