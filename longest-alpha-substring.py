s = input("Enter string:") # i.e. s = "azcbobobegghakl"

longestS = ""               # to eventually store the longest alpha string

for i in range(len(s)):     # interate through every letter in s

    potentialS = s[i]       # temporarily concatenate strings as we go, to eventually compare to longestS; initialize with the current letter at hand

    for subIteration in range(len(s)-i-1):           # to avoid Index Error, keep subIteration w/in length of the REMAINING letters in s (hence the len(s)-i-1)

        # If the next letter *IS* next (OR THE SAME, hence >*=*) in the alphabet, then concatenate it onto the potential string
        if s[subIteration+i+1] >= s[subIteration+i]:
            potentialS += s[subIteration+i+1]

        # If next letter *IS NOT* next in the alphabet, break out of this sub-"FOR"loop + move on
        else:
            break

    # If this potential string *IS* longer than the longest stored, reassign longestS to this new longest
    if len(potentialS) > len(longestS):
        longestS = potentialS

print('Longest substring in alphabetical order is: ' + str(longestS))