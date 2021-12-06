import copy 
from operator import itemgetter
from typing import List, Tuple


def solve(n_machines: int, jobs: List[Tuple[int, int]]):
    jobs_to_do = copy.deepcopy(jobs)
    jobs_queued = []
    machines= [[] for _ in range(n_machines)]
    machines_working = [0] * n_machines
    makespans = [0] * n_machines

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

        # If there is a free machine, schedule the longest job on that machine
        for m_idx, machine in enumerate(machines):
            if machines_working[m_idx] > 0:
                continue

            max_length_job = max(jobs_queued, key=itemgetter(0))
            machine.append(max_length_job)
            jobs_queued.remove(max_length_job) 

            machines_working[m_idx] += max_length_job[0] 
            makespans[m_idx] += max_length_job[0]

            # Print results
            print(f"Scheduled job {job} to Machine #{m_idx + 1} at time {t}")
        
        # Simulate working on the jobs
        machines_working = [x - 1 if x > 0 else 0 for x in machines_working]

        # Increase time
        t += 1

    # Print final scheduling and makespan
    print("Final scheduling using the INTV+LPT algorithm:")
    for idx, machine in enumerate(machines):
        print(f"Machine #{idx + 1}: {machine}")
    print(f"Makespan: {max(makespans)}")
