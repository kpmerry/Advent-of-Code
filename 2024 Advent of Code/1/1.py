# Day 1 Challenge - Python
def ch1part1(filename):
    # Extract lists from input file.
    list1 = []
    list2 = []
    list_len = 0
    with open(filename, "r") as fin:
        for line in fin:
            list_len += 1
            nums = line.split("   ")
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    # Sort the lists.
    list1.sort()
    list2.sort()
    # Add the absolute difference of the pairs of ordered items.
    diff = 0
    for i in range(list_len):
        diff += abs(list1[i] - list2[i])
    return diff

def ch1part2(filename):
    # Extract lists from input file.
    list1 = []
    list2 = []
    list_len = 0
    with open(filename, "r") as fin:
        for line in fin:
            nums = line.split("   ")
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    # Find the similarity score (list1 item * item count in list2).
    sim_score = 0
    for i in list1:
        sim_score += i * list2.count(i)
    return sim_score

print("Day 1:")
print(ch1part1("lists.txt"))
print(ch1part2("lists.txt"))