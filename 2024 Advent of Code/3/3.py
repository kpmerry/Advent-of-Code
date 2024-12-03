def extract_file_info(filename):
    """Extract file information as a string."""
    file_string = ""
    with open(filename, "r") as fin:
        for line in fin:
            file_string += line.strip()
    return file_string


def find_valid_mul(s):
    """Find valid instances of multiplying function, return list of pairs."""

    product_pairs = []
    mult_operator = "mul"
    valid_chars = "(,)"
    poss_valid_strings = s.split(mult_operator)

    for i in poss_valid_strings:
        # Remove empty strings.
        if i == "":
            continue

        # Check the non-numeric characters for a match to valid_chars.
        non_numeric = ""
        for char in i:
            if not char.isnumeric():
                non_numeric += char
        if valid_chars == non_numeric:
            product_pairs.append(i)
        else:
            if valid_chars == non_numeric[:3]:
                end = i.index(")")
                product_pairs.append(i[: end + 1])

    return product_pairs


def get_products(pairs):
    """Get the product of the valid pairs."""
    product = 0
    # Disregard the the "(,)" characters.
    for pair in pairs:
        nums = pair[1:-1].split(",")
        # If invalid, don't include in product.
        if not nums[0].isnumeric() or not nums[1].isnumeric():
            continue
        else:
            product += int(nums[0]) * int(nums[1])
    return product


def product_all_lines(filename):
    """Performs part one of the challenge."""
    file_info = extract_file_info(filename)
    valid_pairs = find_valid_mul(file_info)
    product = get_products(valid_pairs)
    return product


def enabled_muls(s):
    """
    Removes parts of line where multiplying function is diabled.
    Returns the valid pairs for the enabled parts.
    """
    enabler = "do()"
    disabler = "don't()"

    enabled_strings = s.split(enabler)
    pairs = []
    for j in range(len(enabled_strings)):
        # If disabler is in the string, store the index as cut_off.
        cut_off = -1
        if disabler in enabled_strings[j]:
            for i in range(len(enabled_strings[j]) - 7):
                if enabled_strings[j][i : i + len(disabler)] == disabler:
                    cut_off = i
                    break
        # If disabler is not in the string, use -1 as the cut_off.
        if cut_off == -1:
            res = find_valid_mul(enabled_strings[j])
        else:
            # Use string before the cut_off index to find valid pairs.
            res = find_valid_mul(enabled_strings[j][:cut_off])
        pairs.append(res)
    return pairs


def product_enabled(filename):
    """Completes part two of the challenge."""
    product = 0
    file_info = extract_file_info(filename)
    enabled_pairs = enabled_muls(file_info)
    for string in enabled_pairs:
        prod = get_products(string)
        product += prod
    return product


def main():
    """Prints the results."""
    print("Day 3:")
    print(product_all_lines("input.txt"))
    print(product_enabled("input.txt"))


if __name__ == "__main__":
    main()
