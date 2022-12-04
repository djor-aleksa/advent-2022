RUCKSACKS_CONTENTS_FILENAME = "rucksacks_contents.txt"


def calculate_priorities_sum():
    priorities_sum = 0
    with open(RUCKSACKS_CONTENTS_FILENAME) as rucksacks_contents:
        for line in rucksacks_contents:
            content = line.rstrip()
            shared_items = set(content[:len(content)//2]) & set(content[len(content)//2:])
            for item in shared_items:
                priorities_sum += calculate_item_priority(item)
    print(f'Priorities sum is {priorities_sum}.')


def calculate_item_priority(item: str) -> int:
    if item.islower():
        return 1 + ord(item) - ord('a')
    return 27 + ord(item) - ord('A')


def calculate_badges_priorities():
    badges_priorities_sum = 0
    count = 0
    with open(RUCKSACKS_CONTENTS_FILENAME) as rucksacks_contents:
        badge = set()
        for line in rucksacks_contents:
            content = line.rstrip()
            if len(badge) == 0:
                badge = set(content)
            else:
                badge &= set(content)
            count += 1
            if count % 3 == 0:
                badges_priorities_sum += calculate_item_priority(badge.pop())
                badge = set()
    print(f'Badges priorities sum is {badges_priorities_sum}')


if __name__ == "__main__":
    calculate_priorities_sum()
    calculate_badges_priorities()
