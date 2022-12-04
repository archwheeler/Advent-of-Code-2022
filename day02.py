def calculate_round_score(opponent_choice, player_choice):
    WIN_SCORE = 6
    DRAW_SCORE = 3
    LOSE_SCORE = 0

    OUTCOME_SCORE = {
        "A": {
            "X": DRAW_SCORE,
            "Y": WIN_SCORE,
            "Z": LOSE_SCORE,
        },
        "B": {
            "X": LOSE_SCORE,
            "Y": DRAW_SCORE,
            "Z": WIN_SCORE,
        },
        "C": {
            "X": WIN_SCORE,
            "Y": LOSE_SCORE,
            "Z": DRAW_SCORE,
        },
    }

    CHOICE_SCORE = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    return (
        OUTCOME_SCORE[opponent_choice][player_choice] +
        CHOICE_SCORE[player_choice]
    )

def calculate_player_choice(opponent_choice, desired_outcome):
    PLAYER_CHOICE = {
        "A": {
            "X": "Z",
            "Y": "X",
            "Z": "Y",
        },
        "B": {
            "X": "X",
            "Y": "Y",
            "Z": "Z",
        },
        "C": {
            "X": "Y",
            "Y": "Z",
            "Z": "X",
        },
    }

    return PLAYER_CHOICE[opponent_choice][desired_outcome]

with open("inputs/day02_strategy.txt", "r") as strategy_file:
    rounds = list(
        map(lambda round: round.split(), strategy_file.readlines())
    )

    part_1_round_scores = map(
        lambda round: calculate_round_score(*round),
        rounds,
    )
    part_1_final_score = sum(part_1_round_scores)
    print(f"Part 1: {part_1_final_score}")

    part_2_round_scores = map(
        lambda round: (
            calculate_round_score(
                round[0],
                calculate_player_choice(round[0], round[1])
            )
        ),
        rounds,
    )
    part_2_final_score = sum(part_2_round_scores)
    print(f"Part 2: {part_2_final_score}")

