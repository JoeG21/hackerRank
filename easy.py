'''
**************
1: Capitalize!
**************
'''
# def solve(s):
#     x = s.split(' ')
#     y = [word.capitalize() for word in x]
#     z = ' '.join(y)

#     return z
#     '''
#     .title() doesn't work for some reason 
#     return s.title() 
#     .title() => capitalizes the first letter of each word in a string
#     '''
# print(solve(s))




'''
************
2: Text Wrap 
************
'''
# def wrap(string, max_width):
#     words = [string[i:i+max_width] for i in range(0, len(string), max_width)]
#     result = '\n'.join(words)
#     return result




'''
********************
3: String Validators
********************
'''
# def string_val(string):
#     bool_state = [
#         any(method(char) for char in string)
#         for method in (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper)
#     ]

#     for bool_value in bool_state:
#         print(bool_value)
# string_val('ab123')
'''
Original solution. More readable 

bool_state = [False]*5
for char in s:
    if char.isalnum(): bool_state[0]=True
    if char.isalpha(): bool_state[1]=True
    if char.isdigit(): bool_state[2]=True
    if char.islower(): bool_state[3]=True
    if char.isupper(): bool_state[4]=True
for bool in bool_state:
    print(bool)
'''




'''
********************
4: Find a string
********************
'''
# def count_substring(string, sub_string):
#     res = [i for i in range(len(string)) if string.startswith(sub_string, i)]
#     return len(res)




'''
********************
5: Nested Lists
********************
'''    
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
        
#     list_name.append(name)
#     list_score.append(score)

# i=0
# records = [[n] for n in list_name]
# while (i<len(list_name)):
#     records[i].append(list_score[i])
#     i+=1
    

# # Extract unique grades
# grades = set(score for name, score in records)

# # Find the second lowest grade
# second_lowest_grade = sorted(grades)[1]

# # Collect names of students with the second lowest grade
# students_with_second_lowest = sorted(name for name, score in records if score == second_lowest_grade)

# # Print each name on a new line
# for student in students_with_second_lowest:
#     print(student)
        
        


'''
********************
6: Set .discard(), .remove() & .pop()
********************
'''
# def set_operations(set, operations):
#     for op in operations:
#         try:
#             if op.startswith('p'): set.pop()
#             if op.startswith('r'): set.remove(int(op[-1]))
#             if op.startswith('d'): set.discard(int(op[-1]))
#         except:
#             continue
#     return sum(set)

# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# operations = ['pop', 'remove 9', 'discard 9', 'discard 8', 'remove 7', 'pop', 'discard 6', 'remove 5', 'pop', 'discard 5']
# print(set_operations(s, operations))
        
