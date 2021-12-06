import copy
from operator import itemgetter
from typing import List, Tuple


def solve(n_machines: int, jobs: List[Tuple[int, int]]):
    jobs_to_do = copy.deepcopy(jobs)
    jobs_queued = []
    machines= [[] for _ in range(n_machines)]
    machines_working = [0] * n_machines
    makespan = 0

    t = 0

    while jobs_to_do or jobs_queued:
        # Queue jobs that are available at time "t"
        for job in jobs_to_do:
            if job[1] <= t:
                jobs_queued.append(job)

        # Remove queued jobs
        for job in jobs_queued:
            if job in jobs_to_do:
                jobs_to_do.remove(job)

        # If all machines are empty, sort the queued jobs by their length
        # Schedule the sorted jobs using the LIST algorithm
        if all(w == 0 for w in machines_working):
            jobs_queued.sort(key=itemgetter(0), reverse=True)
            
            for job in jobs_queued:
                # Find machine with minimal scheduled working time
                target_machine = min(enumerate(machines_working), key=itemgetter(1))[0]
                machines[target_machine].append(job)
                machines_working[target_machine] += job[0]

                # Print results
                print(f"Scheduled job {job} to Machine #{target_machine + 1} at time {t}")
            
            jobs_queued = []
            makespan += max(machines_working)
        
        # Simulate working on the jobs
        machines_working = [x - 1 if x > 0 else 0 for x in machines_working]

        # Increase time
        t += 1

    # Print final scheduling and makespan
    print("Final scheduling using the INTV+LPT algorithm:")
    for idx, machine in enumerate(machines):
        print(f"Machine #{idx + 1}: {machine}")
    print(f"Makespan: {makespan}")
