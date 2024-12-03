# import time
# for cycle in range(3):
#     for i in range(20):
#         print(f"\r\U0001F534 {20 - i} sekund", end="")
#         time.sleep(1)

#     for i in range(5):
#         if i % 2 == 0:
#             print(f"\r\U0001F7E1 {5 - i} sekund", end="")
#         else: 
#             print(f"\r\U000026AB {5 - i} sekund", end="")
#         time.sleep(1)

#     for i in range(20):
#         print(f"\r\U0001F7E2 {20 - i} sekund", end="")
#         time.sleep(1)




# import time

# # Svetofor sikli 3 marta takrorlanadi
# for cycle in range(3):
#     # Qizil rang: 20 soniya
#     for i in range(20):
#         print(f"\r\U0001F534 Qizil - {20 - i} s", end="")  # Qizil doira emojisi
#         time.sleep(1)

#     # Sariq rang: 5 soniya, uchib yonish
#     for i in range(5):
#         if i % 2 == 0:
#             print(f"\r\U0001F7E1 Sariq - {5 - i} s", end="")  # Sariq doira emojisi
#         else:
#             print(f"\r\U000026AB O‘chdi - {5 - i} s", end="")  # Qora doira (o‘chgan)
#         time.sleep(1)

#     # Yashil rang: 20 soniya
#     for i in range(20):
#         print(f"\r\U0001F7E2 Yashil - {20 - i} s", end="")  # Yashil doira emojisi
#         time.sleep(1)

# print("\nSvetofor tsikli tugadi!")


# add and union
# my_set = {12, 54, 13, 76, 64}
# my_set2 = {43, 78, 92, 0, 98, 24, 12}
# # my_set.add(56)
# z = my_set.union(my_set2)
# z = my_set1 | my_set2
# print(z)


# intersection
# my_set = {1, 2, 3, 4}
# my_set2 = {3, 4, 5, 6}
# z = my_set.intersection(my_set2)
# z = my_set & my_set2
# print(z)


# difference
# my_set = {1, 2, 3, 4}
# my_set2 = {3, 4, 5, 6}
# z = my_set.difference(my_set2)
# z = my_set - my_set2
# print(z)


# symmetric_difference
# my_set = {1, 2, 3, 4}
# my_set2 = {3, 4, 5, 6}
# z = my_set.symmetric_difference(my_set2)
# z = my_set ^ my_set2
# print(z)



# SET
# 1
# my_set = {1, 2, 3, 4}
# my_set2 = {3, 4, 5, 6}
# count = 0
# for i in my_set:
#     if i in my_set2:
#         count += 1
# print(count)


# 2
# my_set = {1, 2, 3, 4}
# my_set2 = {3, 4, 5, 6}

# z = my_set.intersection(my_set2)
# print(z)


# 3
# my_set = {1, 2, 3, 4}
# my_set.pop()
# print(my_set)


# 4
# my_set = {1, 2, 3, 4}
# my_set2 = {4, 5, 6, 7}

# z = my_set.union(my_set2)
# print(z)


# 5
# my_set = {2, 4, 6, 8}
# my_list = list(my_set)
# # get_max = max(my_set)
# # get_min = min(my_set)
# # print(get_max) 
# # print(get_min) 
# get_max = my_list[0]
# get_min = my_list[0]
# for i in my_list:
#     if i > get_max:
#         get_max = i
#     if i < get_min:
#         get_min = i
# my_set = set(my_list)
# print('Max: ', get_max)
# print('Min: ', get_min)
# print(type(my_set))



# 6
# my_set = {2, 5, 6, 76, 8, 4}
# my_set.add(23)
# my_set.pop()
# print(my_set)


# 7
# my_set = {1, 2, 3, 4, 7}
# my_set2 = {3, 4, 5, 6, 7}
# my_set.difference_update(my_set2)
# # my_set -= my_set2
# print(my_set)


# 8
# my_set = {2, 3, 5, 7, 8}
# kupaytma = 1
# for i in my_set:
#     kupaytma *= i
# print(kupaytma)


# 9
# my_set = {2,3,5,7,8," "}
# isTrue = False
# if " " in my_set:
#     isTrue = True

# print(isTrue)


# 10
# my_set = {2,3,5,7,8," "}
# print(len(my_set))



# Dict
# 11
# my_dict = {}
# my_dict['ism'] = 'Ali'
# my_dict['familiya'] = 'Valiyev'
# print(my_dict)


# 12
# my_dict = {'ism': 'Ali', 'familiya': 'Valiyev', 'yosh': 22}
# my_dict['ism'] = 'Vali'
# print(my_dict)


# 13
# my_dict = {'ism': 'Ali', 'familiya': 'Valiyev', 'yosh': 22}
# my_dict.pop('ism')
# print(my_dict)


# 14
# my_dict = {'ism': 'Ali', 'familiya': 'Valiyev', 'yosh': 22}
# print(my_dict.keys())
# print(my_dict.items())

# for i, x in my_dict.items():
#     print(i)


# 15
# my_dict = {'num1': 3, 'num2': 4, 'num3': 49, 'num4': 34}
# get_max = max(my_dict.values())
# print(get_max)



# 16
