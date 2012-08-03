# A program to solve project euler problem 17
#

def listify(number):
    """ makes a list of the digits in the number """
    numlist = []

    for digit in str(number):
        numlist.append(int(digit))

    return numlist

def hundreds(digitlist):
    """ starts finding the letters of the digit that is in the hundreds place, also adds the special case of
    1000 since we don't accept words larger than that """
    
    letters = ""

    # First get the 100s place
    place100 = digitlist.pop()

    # special case 1000 add letters for "one thousand" (11)
    if len(digitlist) > 0:
        onethousand_letters = 11
        return "onethousand"

    # Here the number of letters are a bit more cumbersome, but we can reuse what we have already done with
    # the ones place, and then add the letters for "hundred"
    hundred_letters = "hundred"

    # find the ones and add hundred and
    hundreds = ones(listify(place100)) + hundred_letters

    # add the hundreds to the sum of letters
    return letters + hundreds

def tens(digitlist):
    """ starts finding the letters of the digits that is in addition to the tens using the hundreds function
    then adds the number of letters from the tens place """
    # The array of the number of letters we need to write each of the tens one is also zero here, since we
    # already dealt with the special case in the ones.
    num_letters = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # popping off the 10 since we only need it for this step
    place10 = digitlist.pop()
    letters = ""

    # If the numbers have more digits we have to add the hundreds as well Hah! no special cases this time :D
    if len(digitlist) > 0:
        letters += hundreds(digitlist)

    # Add the tens to the letters of the hundreds if there are any
    return letters + num_letters[place10]

def ones(digitlist):
    """ Starts finding the letters of the digits that is in addition to the ones using the tens function
    and then adds the number of letters from the ones place """
    # An array that describes the number of letters for each digit on the ones place
    num_letters = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]

    # We pop off the digit on the ones place first, since we need it for the calculation
    place1 = digitlist.pop()
    letters = ""
    
    # special case teens
    if len(digitlist) > 0 and digitlist[-1] == 1:
        digitlist.pop()
        
        # If we have more digits we have to add the letters for them as well
        if len(digitlist) > 0:
            # we also have to add the letters for "and" if we have any hundreds
            if len(digitlist) >= 1:
                and_letters = "and"
                letters += and_letters
            letters += hundreds(digitlist)
        
        # Redo the letter numbers, since now we have the ones and the tenth place, since the tens are
        # unregular, stupid teenagers ;)
        num_letters = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] 

    # More digits means that we need to add the letters from them as well
    elif len(digitlist) > 0:
    # we also have to add three letters for "and" when neither 10s nor 1s are 0
        if len(digitlist) >= 2 and place1 != 0 or len(digitlist) >= 2 and digitlist[-1] != 0:
            letters += "and"
        
        letters += tens(digitlist)

    # Add the letters for the ones place (and the teens if they are in play) to the rest of the letters
    return letters + num_letters[place1]

def find_num_letters(number):
    """ finds out how many letters is used to write the number that is supplied """
    digitlist = listify(number)
    
    return len(ones(digitlist))
    

def solve(upto):
    """ Finds how many letters is used to write out the number 
    Can only find out number of letters for numbers <= 1000 """
    
    if upto > 1000:
        return "Error: number too large."
    
    # This is a place to accumulate the number of letters
    letters = 0

    for number in range(1, upto + 1):
        letters += find_num_letters(number)

    return letters

if __name__=="__main__":
    #while True:
     #   num = int(input("> "))
      #  if num == 0:
       #     break
        #print(find_num_letters(num))
        #print("---")
    solve_list = [5, 1000]
    for number in solve_list:
        print("{0}: {1}".format(number, solve(number)))
