ASSIGNMENT_PAIRS_FILENAME = "assignment_pairs.txt"


def count_fully_contained_assignments():
    count = 0
    with open(ASSIGNMENT_PAIRS_FILENAME) as assignment_pairs:

        for line in assignment_pairs:
            assignment_1 = (int(line.rstrip().split(',')[0].split('-')[0]),
                            int(line.rstrip().split(',')[0].split('-')[1]))

            assignment_2 = (int(line.rstrip().split(',')[1].split('-')[0]),
                            int(line.rstrip().split(',')[1].split('-')[1]))

            if assignment_1[0] <= assignment_2[0] and assignment_1[1] >= assignment_2[1] or \
                    assignment_2[0] <= assignment_1[0] and assignment_2[1] >= assignment_1[1]:
                count += 1

    print(f'There are in total {count} fully contained pairs')


def count_overlapping_assignments():
    count = 0
    with open(ASSIGNMENT_PAIRS_FILENAME) as assignment_pairs:
        for line in assignment_pairs:
            assignment_1 = (int(line.rstrip().split(',')[0].split('-')[0]),
                            int(line.rstrip().split(',')[0].split('-')[1]))

            assignment_2 = (int(line.rstrip().split(',')[1].split('-')[0]),
                            int(line.rstrip().split(',')[1].split('-')[1]))

            if len(set(range(assignment_1[0], assignment_1[1] + 1)) &
                   set(range(assignment_2[0], assignment_2[1] + 1))) > 0:
                count += 1

    print(f'There are in total {count} overlapping pairs')


if __name__ == "__main__":
    count_overlapping_assignments()
