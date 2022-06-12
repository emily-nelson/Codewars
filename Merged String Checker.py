"""'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears"""

a = "codewars"
b = "cdw"
c = "oears"


def is_merge(s, part1, part2):

    # loop through s[]
    # check part 1 if it equals, move to next s[]
    # if not, check part 2 and does it equal s[]

    counter_part1 = 0
    counter_part2 = 0

    for letter in s:
        print(counter_part2)
        
        try:
            if part1[counter_part1] == letter:
                print(part1[counter_part1], letter)
                counter_part1 += 1
                continue
        except:
            if part2[counter_part2] == letter:
                counter_part2 += 1
            else:
                return False

        else:
            if part2[counter_part2]:
                if part2[counter_part2] == letter:
                    counter_part2 += 1
            else:
                return False

    return True


print(is_merge(a, b, c))