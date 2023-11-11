def rotate_x(dice: list) -> list:
    dice[0], dice[5], dice[1], dice[4] = dice[5], dice[1], dice[4], dice[0]
    return dice

def rotate_y(dice: list) -> list:
    dice[0], dice[2], dice[1], dice[3] = dice[2], dice[1], dice[3], dice[0]
    return dice

def rotate_z(dice: list) -> list:
    dice[2], dice[5], dice[3], dice[4] = dice[5], dice[3], dice[4], dice[2]
    return dice

def generate_all_rotations(dice: list) -> list:
    """
    Generate all possible rotations of the dice.
    """
    rotations = [dice]
    for _ in range(3):
        dice = rotate_x(dice)
        for _ in range(2):
            dice = rotate_y(dice)
            for _ in range(4):
                dice = rotate_z(dice)
                rotations.append(dice.copy())
    return rotations

def check(dice1: list, dice2: list) -> bool:
    """
    Check if two dice are equivalent, considering all possible rotations.
    """
    rotations_dice1 = generate_all_rotations(dice1)
    return dice2 in rotations_dice1

# We want to group lists that have the same elements so we use a hash
def hash(dice: list) -> int:
    s = 0
    for i in range(6):
        s += dice[i] * 10**i
    return s

# Number of dice
n = int(input())

dice_list = {}

for _ in range(n):
    die = list(map(int, input().split()))
    found = False
    for _ in range(3):
        die = rotate_x(die)
        for _ in range(3):
            die = rotate_y(die)
            for _ in range(4):
                die = rotate_z(die)
                h = hash(die)
                if h in dice_list:
                    dice_list[h] = dice_list[h] + 1
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        h = hash(die)
        dice_list[h] = 1

print(max(dice_list.values()))