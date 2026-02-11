
with open("day3_input.txt") as file:
    battery_banks = file.read().splitlines()

def largest_joltage(length):
    total_joltage = 0
    for bank in battery_banks:
        search_from_idx = 0
        max_joltage_str = ''

        #print("Bank: ", bank[:-1])
        for digit_idx in range(length, 0, -1):
            max_joltage_digit = 0
            max_joltage_digit_idx = 0

            search_to_idx = len(bank) - digit_idx + 1
            #print("Looking for max in range: ", bank[search_from_idx:search_to_idx])
            for i, battery in enumerate(bank[search_from_idx:search_to_idx]):
                joltage = int(battery)
                if joltage > max_joltage_digit:
                    max_joltage_digit = joltage
                    max_joltage_digit_idx = search_from_idx+i
                    #print("New max: ", max_joltage_digit, " at total idx: ", search_from_idx+i)

                if max_joltage_digit == 9:
                    break

            search_from_idx = max_joltage_digit_idx+1
            max_joltage_str += str(max_joltage_digit)

        #print(bank, max_joltage_str)
        total_joltage += int(max_joltage_str)
    return total_joltage

print("part 1: ", largest_joltage(2))
print("part 2: ", largest_joltage(12))