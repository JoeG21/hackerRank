'''
************
1: Leap Year
*************
'''
# def is_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
# print(is_leap(2023))


   

'''
*******************
2: Merge the Tools!
*******************
'''
# def merge_the_tools(string, k):
#     seen = set()
#     current_substring = ''

#     for i, char in enumerate(string):
#         if char not in seen:
#             current_substring += char
#             seen.add(char)
        
#         if (i + 1) % k == 0:
#             print(current_substring)
#             seen.clear()
#             current_substring = ''
# merge_the_tools("AABCAAADA", 3)
'''
Original Solution

def merge_the_tools(string, k):
    sublist = []
    new_word = ''
    count = 0
    
    for char in string:
        if char not in new_word:
            new_word+=char
            count+=1
        else: count+=1
        if count == k:
            sublist.append(new_word)
            new_word = ''
            count=0

    for word in sublist:
        print(word)
'''




'''
**********
3: ginortS
**********
'''
def sortString(STDI):
    low_char = ''
    up_char = ''
    odd_num = ''
    even_num = ''

    for char in STDI:
        if char.islower(): low_char+=char
        if char.isupper(): up_char+=char
        if char.isdigit():
            if int(char)%2!=0: odd_num+=char
            else: even_num+=char

    final_word = ''.join(sorted(low_char)) + ''.join(sorted(up_char)) + ''.join(sorted(odd_num)) + ''.join(sorted(even_num))
    return final_word
word = 'ginortS'
print(sortString(word)) # => ginortS1324


