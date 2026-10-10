def sjf(bt):
    bt.sort()

    waiting_time = 0
    total_waiting_time = 0

    for i in range(len(bt)):
        total_waiting_time += waiting_time
        waiting_time += bt[i]

    return total_waiting_time // len(bt)


# Input
bt = list(map(int, input("Enter burst times: ").split()))

# Calculate and print the answer
print(sjf(bt))