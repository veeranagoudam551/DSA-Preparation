
def jobScheduling(jobs):
    # Sort jobs by profit from highest to lowest
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline
    max_deadline = 0
    for job in jobs:
        max_deadline = max(max_deadline, job[1])

    # Create time slots; index 0 is unused
    slots = [-1] * (max_deadline + 1)

    count = 0
    profit = 0

    # Schedule each job
    for job in jobs:
        job_id = job[0]
        deadline = job[1]
        job_profit = job[2]

        # Check slots from deadline backwards
        for j in range(deadline, 0, -1):
            if slots[j] == -1:
                slots[j] = job_id
                count += 1
                profit += job_profit
                break

    print("Scheduled jobs:", slots[1:])
    print("Number of jobs:", count)
    print("Maximum profit:", profit)


# Take input from the user
jobs = []
n = int(input("Enter number of jobs: "))

for i in range(n):
    job_id, deadline, profit = map(
        int, input("Enter job ID, deadline, profit: ").split()
    )
    jobs.append([job_id, deadline, profit])

jobScheduling(jobs)
