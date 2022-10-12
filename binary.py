# Binary search - is an algorithm which searches for a particular element in a sorted list and returns
# its position, if the element is no in the list returns null

Items = [i for i in range(1, 101)]

k = int(input(("Think of a number from [1:100]:\n-")))


def search_bin(i):
    guess = Items[len(Items) // 2]
    ans = int(input(f"If your number is > then {guess}, press 1"
                    f"\nif your number is < then {guess}, press 2\n"
                    f"If your number is {guess}, press 3\n-"))
    return ans


steps = 1
while True:
    l = search_bin(Items)
    if l == 1:
        Items = Items[len(Items) // 2:]
    elif l == 2:
        Items = Items[:len(Items) // 2]
    else:
        break
    steps += 1
print(
    f"It took me {steps} guessses to guess your number, using the Binary-Search\nT"
    f"he ordinary search would be done within {k} steps\n"
    f"For the sorted list with n elements it will take me maximum log2(n) guessed to guess your number\n"
    f"The ordinary searh would guarantee result in n steps.")
