import re

def read_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return None

def find_coordinates(data):
    word_number_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for value in data:
        val_tokens = list(value)

        # Find the first digit index
        first_index_arr = []
        first_temp_str = ""
        for i, ch in enumerate(val_tokens):
            if ch.isdigit():
                first_index_arr.append(str(ch))
                break
            else:
                first_temp_str += ch
                result_num_word = re.search(r'one|two|three|four|five|six|seven|eight|nine', first_temp_str)
                if result_num_word is not None:
                    num_str = word_number_map.get(result_num_word.group(), None)
                    if num_str is not None:
                        first_index_arr.append(num_str)
                        break  # Stop searching once a valid word is found

        # Find the last digit index
        last_index_arr = []
        second_temp_str = ""
        for i, ch in enumerate(val_tokens[::-1]):
            if ch.isdigit():
                #last_index_arr.append(str(len(val_tokens) - i - 1))
                last_index_arr.append(ch)
                break
            else:
                second_temp_str += ch
                result_num_word = re.search(r'one|two|three|four|five|six|seven|eight|nine', second_temp_str[::-1])
                if result_num_word is not None:
                    num_str = word_number_map.get(result_num_word.group(), None)
                    if num_str is not None:
                        last_index_arr.append(num_str)
                        break  # Stop searching once a valid word is found

        if len(first_index_arr) != 0 and len(last_index_arr) != 0:
            first_token = first_index_arr[0]
            second_token = last_index_arr[0]

            try:
                token_combined = first_token + second_token
                int_single_number = int(token_combined)
                total += int_single_number
            except ValueError:
                pass  # Ignore non-integer values

    return total

filename = "input.txt"
data = read_file(filename)

input_str = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
r = find_coordinates(data)
print(r)
