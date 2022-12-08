SIGNALS_FILENAME = "tuning_signals.txt"


def find_first_start_code(number_of_different_characters):
    with open(SIGNALS_FILENAME, 'r', encoding='UTF-8') as file:
        input_signals = file.read()
        test_sample = []
        result_index = -1
        for index, character in enumerate(input_signals):
            test_sample.append(character)
            if len(set(test_sample)) == number_of_different_characters:
                result_index = index
                break
            if len(test_sample) == number_of_different_characters:
                test_sample.pop(0)
    print(f'Totally {result_index+1} number of characters need to be processed')


if __name__ == "__main__":
    find_first_start_code(4)
    find_first_start_code(14)
