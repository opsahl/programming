# Problem 26
# 13 September 2002
# 
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle. 
# 
# Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def get_length_repeating_decimals(num, den):
    """ Gets the length of the cycle of repeating numbers in the decimals of a fraction """
    # When we use longhand divison for the fraction we find that we get a cycle of reminders that
    # repeats, we can use this knowledge to find the length of the repeating part of the decimal by
    # finding the reminder multiplying it with ten and devide it again, if we then get back to a reminder
    # we have had before, we know that we will have an infinite repetition again, and the length from the last
    # time we had this reminder will be the length of the cycle

    # keep running the formula until we get a reminder we have seen before
    reminders = []

    reminder = num % den

    while reminder not in reminders:
        reminders.append(reminder)
        reminder = reminder * 10 % den

    # now find how long ago it is that we saw this reminder last
    cycle_length = len(reminders) - reminders.index(reminder)

    return cycle_length

def decimal_longest_cycle(upto):
    """ returns the denominator d in 1/d where the repeating cycle is the longest """
    cycle_lengths = [get_length_repeating_decimals(1, den) for den in range(2, upto + 1)]
    longest_cycle = max(cycle_lengths)

    # We have to add to to the index, 1 for the 0 starting array and another since we start on 2 as the first denominator
    return cycle_lengths.index(longest_cycle) + 2

if __name__ == "__main__":
    print(decimal_longest_cycle(1000))
