# Job 1: (0, 6, 60)
# Job 2: (5, 9, 50)
# Job 3: (1, 4, 30)
# Job 4: (5, 7, 30)
# Job 5: (3, 5, 10)
# Job 6: (7, 8, 10)

class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

# find the jobs that lead to the max profit added for testing
def find_jobs(jobs):
    size = len(jobs)

    if size == 0:
        return []

    jobs.sort(key=lambda x: x.finish)
    max_profit = [0] * size
    prev = [-1] * size

    #consider each job
    for i in range(size):
        max_profit[i] = 0

        # consider all jobs before it that don't overlap
        for j in range(i):
            # if the job doesn't conflict with the current job
            # and leads to a higher profit
            if jobs[j].finish <= jobs[i].start and max_profit[j] > max_profit[i]:
                max_profit[i] = max_profit[j]
                prev[i] = j

        # add the current job's profit
        max_profit[i] += jobs[i].profit

    # find the job with the max profit
    max_index = max_profit.index(max(max_profit))
    result = []

    # find the jobs that lead to the max profit
    while max_index != -1:
        result.append(jobs[max_index])
        max_index = prev[max_index]

    return result

    
# list of jobs start finish and profit
jobs = [Job(0, 6, 60), Job(1, 4, 30), Job(3, 5, 10), Job(5, 7, 30), Job(5, 9, 50), Job(7, 8, 10)]

# find the jobs that lead to the max profit and print the start stop and profit
print("Jobs: ")

job_listing = find_jobs(jobs)
for job in job_listing:
    print("Start: ", job.start, " Finish: ", job.finish, " Profit: ", job.profit)

# print the max profit for the selected jobs
print("Max Profit: ", sum([job.profit for job in job_listing]))
