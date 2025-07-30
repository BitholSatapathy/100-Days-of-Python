#loops with python lists
# fruits = ["apple","pear","orange"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
    
    
# print(fruits)

# student_scores = [87, 73, 65, 92, 48, 79, 56, 84, 90, 69, 77, 61, 95, 68, 82]
# # total_exam_score = sum(student_scores)
# # # print(total_exam_score)


# # sum = 0
# # for score in student_scores:
# #     sum += score
    
# # print(sum)
# maximum_exam_score = max(student_scores)
# max = 0
# for score in student_scores:
#     if score > max:
#         max = score
# print(max)

#range
#add numbers 1 to 100
# sum_total = 0
# for temp in range(1, 101):
#     sum_total = sum_total + temp
    
# print(sum_total)
    
# for number in range (1,11, 3):
#     print(number)

for number in range (1,101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        if number % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(number)
        
