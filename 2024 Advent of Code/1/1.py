# Day 1 Challenge - Python
def ch1part1():
    # Get input of two lists
    list1 = []
    list2 = []
    list_len = 0

    with open("lists.txt", "r") as fin:
        for line in fin:
            list_len += 1
            nums = line.split("   ")
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

    # Sort lists
    list1.sort()
    list2.sort()

    # Add differences of each ordered item
    diff = 0

    for i in range(list_len):
        diff += abs(list1[i] - list2[i])

    return diff

def ch1part2():
    # Get input of two lists
    list1 = []
    list2 = []
    list_len = 0

    with open("lists.txt", "r") as fin:
        for line in fin:
            nums = line.split("   ")
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    
    sim_score = 0

    for i in list1:
        sim_score += i * list2.count(i)

    return sim_score

print(ch1part1())
print(ch1part2())