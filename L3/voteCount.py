N = int(input())  # Is N relevant??
code_word = input()

counter_a = counter_b = 0
for i in range(N):
    if code_word[i] == "A":
        counter_a += 1
    else:
        counter_b += 1
#     if letter == "A":
#         counter_a += 1
#     else:
#         counter_b += 1

if counter_a > counter_b:
    print("A")
elif counter_b > counter_a:
    print("B")
else:
    print("Tie")
