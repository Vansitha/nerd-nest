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
    total = 0
    for value in data:
        val_tokens = list(value)

        # Find the first digit index
        first_index = None
        for i, ch in enumerate(val_tokens):
            if ch.isdigit():
                first_index = i
                break

        # Find the last digit index
        last_index = None
        for i, ch in enumerate(val_tokens[::-1]):
            if ch.isdigit():
                last_index = len(val_tokens) - i - 1
                break

        if first_index is not None and last_index is not None:
            first_token = val_tokens[first_index]
            second_token = val_tokens[last_index]

            try:
                int_single_number = int(first_token + second_token)
                total += int_single_number
            except ValueError:
                pass  # Ignore non-integer values

    return total


filename = "input.txt"
data = read_file(filename)

sample = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
sample2 = ["treb7uchet"]
r = find_coordinates(data)
print(r)

