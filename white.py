 



 # looking for a number in the array that has a double


def ch_d(a_list):
    for e in a_list:
        if e*2 in a_list:
            return True



def dubadub(a_list):
    return True if [e for e in a_list if e*2 in a_list] else False

    # return [e for e in a_list if e*2 in a_list]

def find_doubles_set(nums):
    nums_set = set(nums)
    for num in nums_set:
        if num * 2 in nums_set or num / 2 in nums_set:
            return True
    return False

#  change it into a dictionary and make it faster

def ch_dd(a_list):
    dct = {}
    for i in range(len(a_list)-1):
        dct[a_list[i]] = i
    for key in dct.keys():
        if key*2 in dct:
            return True

    return False



print(ch_dd([10,2,5,3]))

print(ch_dd([1,14,7,11]))
# 
print(ch_dd([7,1,3,11]))