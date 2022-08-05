def product(a, b):
    """Return product of a and b."""
    return a*b

def weekday_name(day_of_week):
    """Return name of weekday."""
    weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if 0 < day_of_week and day_of_week < 8:
        return weekdays[day_of_week-1]
    else:
        return None


def last_element(lst):
    """Return last item in list (None if list is empty."""
    if lst:
        return lst[-1]

def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a"""
    if a == b:
        return "Numbers are equal"
    if a > b:
        return "First is greater"
    return "Second is greater"

def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a"""
    if a == b:
        return "Numbers are equal"
    if a > b:
        return "First is greater"
    return "Second is greater"


def reverse_string(phrase):
    """Reverse string,"""
    lis = (list(phrase))
    lis.reverse()
    Rev = ''.join(lis)
    return Rev


def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?"""
    WORD = word.upper()
    LETTER = letter.upper()
    lis = list(WORD)
    return lis.count(LETTER)


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase."""
    phraseLetters = list(phrase)
    listOfLetters = set(phraseLetters)
    letterCount = {}
    for letter in phraseLetters:
        letterCount[letter] =phraseLetters.count(letter)
    return letterCount


def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end."""
    #finalList = []
    dictOfLoc = {'end': len(lst)+2, 'beginning': 0}
    dictOfCom = {'add': list.insert, 'delete': list.remove}
    location = dictOfLoc.get(location, None)
    method = dictOfCom.get(command,None)
    if not method or not location:
        return None
    method(lst,location,value)
    return lst


def is_palindrome(phrase):
    """Is phrase a palindrome?"""
    PHRASE = phrase.upper().replace(" ",'')
    forward = list(PHRASE)
    backward = forward.copy()
    backward.reverse()
    if forward == backward:
        return True
    return False


def frequency(lst, search_term):
    """Return frequency of term in lst."""
    return lst.count(search_term)


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase."""
    TO_SWAP = to_swap.swapcase()
    lis = list(phrase)
    for i in range(len(lis)):
        if lis[i] == TO_SWAP or lis[i] == to_swap:
            lis[i] = lis[i].swapcase()
    phrase = ''.join(lis)
    return phrase


def multiply_even_numbers(nums):
    """Multiply the even numbers."""
    product = 1
    for num in nums:
        if not num%2:
            product *=num
    return product

def capitalize(phrase):
    """Capitalize first letter of first word of phrase."""
    return phrase.capitalize()



def compact(lst):
    """Return a copy of lst with non-true elements removed."""
    trueList = lst.copy()
    for el in lst:
        print(not not el)
        if not el:
            trueList.remove(el)
    return trueList


def intersection(l1, l2):
    """Return intersection of two lists as a new list::"""
    return list(set(l1) & set(l2))


def partition(lst, fn):
    """Partition lst by predicate."""
    passed = [x for x in lst if fn(x)]
    failed = [x for x in lst if not fn(x)]
    return [passed,failed]



def mode(nums):
    """Return most-common number in list."""
    finalCount = 0
    for num in nums:
        if nums.count(num) > finalCount:
            winner = num
            finalCount = nums.count(num)
    return winner


def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg."""
    calcs = {'add': a+b, 'subtract': a-b, 'multiply':a*b, 'divide':a/b}
    answer = calcs.get(operation, None)
    if not answer:
        return answer
    if make_int:
        return f"{message} {int(answer)}"
    
    return (f"{message} {answer}")



def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?"""
    hobbies1 = a[2]
    hobbies2 = b[2]
    common = set(hobbies1) & set(hobbies2)
    return bool(common)


def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4."""
    return [num*3 for num in nums if num%4 == 0]


def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts."""
    nameList = [f"{name.get('first','')} {name.get('last','')}" for name in people]
    return nameList


def sum_floats(nums):
    """Return sum of floating point numbers in nums."""
    sum = 0
    for num in nums:
        if type(num) == float:
            sum += num
    return sum

def list_check(lst):
    """Are all items in lst a list?"""
    for item in lst:
        if type(item) is not list:
            return False
    return True


def remove_every_other(lst):
    """Return a new list of other item."""
    return [lst[i] for i in range(len(lst)) if not i%2]
lst = [1, 2, 3, 4, 5]
remove_every_other(lst)



def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal."""
    for i in range(len(nums)):
        for j in range(i):
            sum = nums[i] + nums[j]
            if sum == goal:
                return (nums[j],nums[i])
    return ()


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive."""
    phraseList = list(phrase.lower())
    vsList = list('aeiou')
    return {letter : phraseList.count(letter) for letter in vsList if phraseList.count(letter)}


def titleize(phrase):
    """Return phrase in title case (each word capitalized)."""
    phrase = phrase.lower().capitalize()
    phraseList = list(phrase)
    for i in range(len(phraseList)):
        if phraseList[i] == ' ':
            phraseList[i+1] = phraseList[i+1].upper()
    return ''.join(phraseList)


def find_factors(num):
    """Find factors of num, in increasing order."""
    return [fact+1 for fact in range(num) if num%(fact+1) == 0]


def includes(collection, sought, start=0):
    """Is sought in collection, starting at index start?"""
    if type(collection) is set:
        return bool(list(collection).count(sought))
    if type(collection) is dict:
        dictList = list(collection.values())
        return bool(dictList.count(sought))
    else:
        for i in range(start,len(collection)):
            print(collection[i])
            if collection[i] == sought:
                return True
    return False


def repeat(phrase, num):
    """Return phrase, repeated num times."""
    if type(num) is not int or not num >= 0:
        return None
    
    returnString = ''
    for i in range(num):
        returnString += phrase
    return returnString


def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase."""  
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    trunc = phrase[0:n]
    if len(trunc) == n:
        return phrase[0:n-3] + '...'
    return trunc


def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those."""
    dictionary = {}
    
    for i in range(len(keys)):
        dictionary.setdefault(keys[i],values[i])
        values += [None]
    return dictionary



def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end."""
    total = 0
    trunc = nums[start:end]
    if type(end) == int and end < len(nums):
        trunc += [nums[end]]
        print (trunc)
    for num in trunc:
        total += num
    return total



def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?"""
    lis1 = list(str(num1))
    lis2 = list(str(num2))
    freq1 = []
    freq2 = []
    for i in range(10):
        freq1 += [lis1.count(str(i))]
        freq2 += [lis2.count(str(i))]
    return freq1 == freq2



def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest).."""
    sort = sorted(ages, reverse = True)
    oldest = sort[0]
    second = 0
    for age in sort:
        if not age == oldest:
            second = age
            break
    return (second,oldest)


def find_the_duplicate(nums):
    """Find duplicate number in nums."""
    for i in range(len(nums)):
        if nums.count(nums[i]) == 2:
            return nums[i]
    return None



def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals."""
    sum = 0
    reverse = matrix.copy()
    reverse.reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum += matrix[i][j]
                sum += reverse[i][j]
    return sum


def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d."""
    keysList = list(d.keys())
    keysList.sort()
    return (keysList[0],keysList[-1])



def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number."""
    sum = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] < nums[j]:
                sum += 1
    return sum



def is_odd_string(word):
    """Is the sum of the character-positions odd?"""
    lst = list(word)
    total = 0
    for letter in lst:
        total += ord(letter)
    return bool(total%2)




