def extract_file_info(filename):
    strings = []
    with open(filename, "r") as fin:
        for line in fin:
            strings.append(line)
    return strings


def find_valid_char(s):
    valid_s = ""
    valid = "mul(,)"  # and numeric
    for char in s:
        if char in valid or char.isnumeric():
            valid_s += char
    return valid_s


def find_valid_mul(s):
    product_pairs = []
    s_list = s.split("mul")
    valid_chars = "(,)"
    for i in s_list:
        if i == "":
            continue
        non_numeric = ""
        for char in i:
            if not char.isnumeric():
                non_numeric += char
        if valid_chars == non_numeric:
            product_pairs.append(i)
        else:
            if valid_chars == non_numeric[:3]:
                diff = len(non_numeric) - len(non_numeric[:3])
                product_pairs.append(i[:-(diff)])
    return product_pairs


def get_products(pairs):
    product = 1
    for pair in pairs:
        nums = (pair[1:-1]).split(",")
        if not nums[0].isnumeric() or not nums[1].isnumeric():
            continue
        else:
            product += int(nums[0]) * int(nums[1])
    return product


def product_all_lines(filename):
    product = 1
    data = extract_file_info(filename)
    for s in data:
        s1 = find_valid_char(s)
        s2 = find_valid_mul(s1)
        s3 = get_products(s2)
        product += s3
    return product


def main():
    print("Day 3:")
    print(product_all_lines("input.txt"))


if __name__ == "__main__":
    main()
