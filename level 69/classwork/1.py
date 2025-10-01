# 1) დაწერეთ ფუნქცია და გადაეცით მას ორი რიცხვი. პასუხად დააბრუნეთ ის რიცხვი, რომელიც ამ ორი ინტეჯერიდან ყველაზე დიდი იქნება

# 2) შექმენით ფუნქცია, რომელსაც გადასცემთ ინტეჯერების სიას. ფუნქციამ უნდა დააბრუნოს მეორე ყველაზე მცირე ელემენტი.

# 3) შექმენით ფუნქცია, რომელსაც გადასცემთ ინტეჯერების სიას. ფუნქციამ უნდა დააბრუნოს მეორე ყველაზე დიდი ელემენტი.

# 4) დაწერეთ ფუნქცია, რომელიც დააბრუნებს True-ს თუ არგუმენტად გადაცემული სტრინგის პირველი და ბოლო ასო ერთმანეთს ემთხვევა

def one(a,b):
    if a>b:
        return a
    else:
        return b

print(one(7,123))

def two(lst):
    new_lst=sorted(lst)
    return new_lst[1]
print(two([6,5,3,9,8,1,2]))

def three(lst):
    new_lst=sorted(lst)
    return new_lst[-2]
print(three([6,5,3,9,8,1,2]))

def first_last_match(text):
    if len(text) == 0:
        return False
    return text[0] == text[-1]
print(first_last_match("ssssaas"))

def count_number_occurrences(numbers, choice):
    return numbers.count(choice)


# Example list
nums = [1, 2, 3, 2, 4, 2, 5]

# Show the list to the user
print("აირჩიე რიცხვი ამ სიიდან:", nums)

# Ask user to input a number
user_choice = int(input("შეიყვანე რიცხვი: "))

# Call the function
result = count_number_occurrences(nums, user_choice)

# Print result
print(f"რიცხვი {user_choice} მეორდება {result} ჯერ სიაში")