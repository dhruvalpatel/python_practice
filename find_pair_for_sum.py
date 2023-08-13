"""Find the pair with a given number in a list. two elements sum to the given number."""


def find_pair_of_sum(target, num_list):
    """"""
    pairs = []
    for i, n in enumerate(num_list):
        for m in num_list:
            if n + m == target:
                # return (n, m)
                pairs.append((n, m))
    print(set(pairs))



target = 10
num_list = [8, 7, 2, 5, 3, 1]

find_pair_of_sum(target, num_list)
