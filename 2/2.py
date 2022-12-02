def main():

    # with open('input.txt') as f:
    #     lines = f.readlines()
    lines = "A Y\nB X\nC Z"
    lines = str.splitlines(lines)

    wins_dict = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    loose_dict = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    draw_dict = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    #first_challenge(lines, wins_dict, draw_dict)

    second_challenge(lines, wins_dict, draw_dict, loose_dict)


def first_challenge(lines, wins_dict, draw_dict):
    points = 0

    # A=rock, B=paper, C=scissors
    # x=rock(1) Y=paper(2) Z=scissors(3)
    for i, l in enumerate(lines):
        if 'X' in l:
            points += 1
        if 'Y' in l:
            points += 2
        if 'Z' in l:
            points += 3

    for i, l in enumerate(lines):
        # print(i, "<-counter. item-> ", l)

        # win
        if wins_dict.get(lines[i][0]) == lines[i][2]:
            points += 6
        #   print(points, lines[i][0], lines[i][2])

        # draw
        elif draw_dict.get(lines[i][0]) == lines[i][2]:
            points += 3
        #  print(points, lines[i][0], lines[i][2])

    print("first challenge:", points)

# x=loose, y=draw, z=win
# second row says how the round ends

# "A Y
# B X
# C Z"
    # # draw_dict = {
    #     'A': 'X',
    #     'B': 'Y',
    #     'C': 'Z'

# wrong: 13736, too high

# x=rock(1) Y=paper(2) Z=scissors(3)
# x=loose, y=draw, z=win
# second row says how the round ends


def second_challenge(lines, wins_dict, draw_dict, loose_dict):
    points_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    points = 0

    for i, l in enumerate(lines):
        if lines[i][2] == 'X':
            # loose
            print("charvalue:", points_dict.get(loose_dict.get(
                lines[i][0])), "char:", loose_dict.get(lines[i][0]))

            # print(loose_dict.get('B'))
            # print(points_dict.get('X'))
            # print(points_dict.get(loose_dict.get(
            #     lines[i][0])))

            points += 0 + points_dict.get(loose_dict.get(
                lines[i][0]))
            print(i, "<-counter. item-> ", "loss", "points-->", points)

        elif lines[i][2] == 'Y':
            # draw
            print("charvalue:", points_dict.get(draw_dict.get(
                lines[i][0])), "char:", draw_dict.get(lines[i][0]))

            points += 3 + points_dict.get(draw_dict.get(
                lines[i][0]))

            print(i, "<-counter. item-> ", "draw", "points-->", points)
        elif lines[i][2] == 'Z':
            # win
            print("charvalue:", points_dict.get(wins_dict.get(
                lines[i][0])), "char:", wins_dict.get(lines[i][0]))
            points += 6 + points_dict.get(wins_dict.get(
                lines[i][0]))
            print(i, "<-counter. item-> ", "win", "points-->", points)
    print("second challenge:", points)


if __name__ == "__main__":
    main()
