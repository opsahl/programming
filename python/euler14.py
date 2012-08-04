def gen_collatz_seq(num):
    length = 1

    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        length += 1

    return length

if __name__=="__main__":
    longest_seq = 0
    num_longest = 0

    for num in range(1, 1000000):
        length = gen_collatz_seq(num)
        if length > longest_seq:
            longest_seq = length
            num_longest = num

    print(num_longest)
