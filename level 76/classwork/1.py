# შექმენით ფუნქცია, რომელსაც გადაეცემა 1 სია, ამ სიიდან ამოიღეთ ყველა kenti რიცხვი, შემდეგ თითოეული აიყვანეთკვადრატში და დააბრუნეთ ეგ ყველა რიცხვი გაერთიანებული,

# მაგ: გადმოგვეცა სია [1, 2, 3, 4, 5]
# მარტივი რიცხვები -> [2, 3, 5]
# აყვანილი კვადრატში ->  [4, 9, 25]
#  გაერთიანებული -> 4925


# def calculator(num):
#     res = []
#     for i in num:
#         if i % 2 ==1:
#             res.append(str(i**2))
#     return "".join(res)

# print(calculator([1,2,3,4,5,6]))

def first(x):
    return x *2

def second(x,y):
    return first(x) + first (y)

print(second(10,25))

age = 67
age("print")