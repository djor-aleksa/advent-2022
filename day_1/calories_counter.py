# https://adventofcode.com/2022/day/1
INVENTORY_FILE_NAME = "calories_inventory.txt"


# part 1
def print_max_calories_count():
    with open(INVENTORY_FILE_NAME) as inventory:
        max_calories_sum = 0
        calories_sum = 0
        for entry in inventory:
            if entry != '\n':
                calories_sum += int(entry)
            else:
                if max_calories_sum < calories_sum:
                    max_calories_sum = calories_sum
                calories_sum = 0

    print(f'Elf with max calories count has: {max_calories_sum} calories')


# part 2
def print_sum_of_top_n_elves(n: int):
    top_list = [0] * n
    with open(INVENTORY_FILE_NAME) as inventory:
        calories_sum = 0
        for entry in inventory:
            if entry != '\n':
                calories_sum += int(entry)
            else:
                for top_score in top_list.copy():
                    if top_score < calories_sum:
                        top_list.remove(top_score)
                        top_list.append(calories_sum)
                        break
                calories_sum = 0
    print(f'Top {n} have in total: {sum(top_list)} calories')


if __name__ == "__main__":
    print_max_calories_count()
    print_sum_of_top_n_elves(3)
