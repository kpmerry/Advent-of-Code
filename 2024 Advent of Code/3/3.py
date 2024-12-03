def extract_file_info(filename):
    string = ""
    with open(filename, "r") as fin:
        for line in fin:
            string += line.strip()
    return string


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
                end = i.index(")")
                product_pairs.append(i[: end + 1])
    return product_pairs


def get_products(pairs):
    product = 0
    for pair in pairs:
        nums = pair[1:-1].split(",")
        if not nums[0].isnumeric() or not nums[1].isnumeric():
            continue
        else:
            product += int(nums[0]) * int(nums[1])
    return product


def product_all_lines(filename):
    s = extract_file_info(filename)
    s1 = find_valid_mul(s)
    product = get_products(s1)
    return product


def enabled_muls(s):
    enabled = "do()"
    disabled = "don't()"
    dos = s.split(enabled)
    pairs = []
    for j in range(len(dos)):
        cut_off = -1
        if disabled in dos[j]:
            for i in range(len(dos[j]) - 7):
                if dos[j][i : i + 7] == disabled:
                    cut_off = i
                    break
        if cut_off == -1:
            res = find_valid_mul(dos[j])
        else:
            res = find_valid_mul(dos[j][:cut_off])
        pairs.append(res)
    return pairs


def product_enabled(filename):
    product = 0
    s = extract_file_info(filename)
    s2 = enabled_muls(s)
    for string in s2:
        prod = get_products(string)
        product += prod
    return product


def main():
    print("Day 3:")
    print(product_all_lines("input.txt"))
    print(product_enabled("input.txt"))


if __name__ == "__main__":
    main()
