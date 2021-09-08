# write your code here
import random

guest_list = {}
guest_names = []
bill_amount = 0
print("Enter the number of friends joining (including you):")
num_of_friends = input()

if num_of_friends.isalpha() or int(num_of_friends) <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for num in range(int(num_of_friends)):
        guest_names.append(input())

    print("Enter the total bill value:")
    bill_amount = float(input())

    print("Do you want to use the \"Who is lucky?\"feature? Write Yes/No:")
    lucky = input()
    if lucky == "Yes":
        bill_amount = (bill_amount / (len(guest_names) - 1))
        lucky_guest = guest_names[random.randint(0, len(guest_names) - 1)]
        print("{} is the lucky one!".format(lucky_guest))
        print()

        for num in range(int(num_of_friends)):
            guest_list[guest_names[num]] = round(bill_amount, 2)
            guest_list[lucky_guest] = 0
        print(guest_list)

    else:
        bill_amount = bill_amount / len(guest_names)
        print("No one is going to be lucky")
        for num in range(int(num_of_friends)):
            guest_list[guest_names[num]] = round(bill_amount, 2)
        print(guest_list)
