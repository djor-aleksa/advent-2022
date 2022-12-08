CRATES_INSTRUCTIONS_FILE = "crates.txt"


def apply_crates_instructions_9000() -> None:
    with open(CRATES_INSTRUCTIONS_FILE) as file:
        file_content = file.read()
        crates_initial_state = file_content.split('\n\n')[0]
        state_matrix = create_state_matrix(crates_initial_state)
        print('--------------Initial state------------------')
        display_state(state_matrix)
        instructions = file_content.split('\n\n')[1]
        for instruction in instructions.split('\n'):
            for i in range(0, int(instruction.split()[1])):
                move_one_crate(state_matrix, int(instruction.split()[3]), int(instruction.split()[5]))


def apply_crates_instructions_9001() -> None:
    with open(CRATES_INSTRUCTIONS_FILE) as file:
        file_content = file.read()
        crates_initial_state = file_content.split('\n\n')[0]
        state_matrix = create_state_matrix(crates_initial_state)
        print('--------------Initial state------------------')
        display_state(state_matrix)
        instructions = file_content.split('\n\n')[1]
        for instruction in instructions.split('\n'):
            number_of_crates_to_move = int(instruction.split()[1])
            source_stack = int(instruction.split()[3])
            destination_stack = int(instruction.split()[5])

            temporary_stack = (destination_stack + 1) % len(state_matrix[0]) + 1

            if temporary_stack == source_stack:
                temporary_stack = (temporary_stack + 1) % len(state_matrix[0])

            for i in range(0, number_of_crates_to_move):
                move_one_crate(state_matrix, source_stack, temporary_stack)

            for i in range(0, number_of_crates_to_move):
                move_one_crate(state_matrix, temporary_stack, destination_stack)


def create_state_matrix(crates_initial_state: str) -> list:
    crates_initial_state_list = crates_initial_state.split('\n')
    stack_number = len((crates_initial_state_list[-1]).split())
    state_matrix = [[] for i in range(stack_number - 1)]

    for line_index, line in enumerate(crates_initial_state_list[:-1]):
        slice_offset = 1
        while slice_offset <= stack_number * 4:
            if slice_offset <= len(line) and not line[slice_offset].isspace():
                state_matrix[line_index].append(line[slice_offset])
            else:
                state_matrix[line_index].append(" ")
            slice_offset += 4
    return state_matrix


def move_one_crate(state_matrix: list, source_stack: int, target_stack: int) -> None:
    print(f'Moving crate from stack {source_stack} to stack {target_stack}')
    check_state_matrix_for_extension(state_matrix, target_stack)

    source_stack_height = 0
    while state_matrix[source_stack_height][source_stack - 1].isspace():
        source_stack_height += 1

    target_stack_height = 0
    while target_stack_height != len(state_matrix) and state_matrix[target_stack_height][target_stack - 1].isspace():
        target_stack_height += 1

    state_matrix[target_stack_height - 1][target_stack - 1], state_matrix[source_stack_height][source_stack - 1] = \
        state_matrix[source_stack_height][source_stack - 1], " "

    check_state_matrix_for_compression(state_matrix)

    display_state(state_matrix)


def check_state_matrix_for_extension(state_matrix: list, target_stack:int) -> None:
    if state_matrix[0][target_stack - 1] != " ":
        state_matrix.insert(0, [" " for i in range(len(state_matrix[0]))])
        print('---------Space added to state matrix---------')


def check_state_matrix_for_compression(state_matrix: list) -> None:
    if all(s.isspace() for s in state_matrix[0]):
        print('---------Space removed from state matrix------')
        state_matrix.remove(state_matrix[0])


def display_state(matrix:list) -> None:
    for row in matrix:
        print(row)
    print('-' * 45)
    print([str(i) for i in range(1, len(matrix[-1]) + 1)])
    print('-' * 45)


if __name__ == "__main__":
    # apply_crates_instructions_9000()
    apply_crates_instructions_9001()
