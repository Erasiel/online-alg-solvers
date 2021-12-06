import copy
from typing import List


def solve(starting_config: List[int], queries: List[int]):
    normal_config = sorted(starting_config)
    lazy_config = copy.deepcopy(normal_config)
    cost = 0
    n_servers = len(normal_config)

    for query in queries:
        if query in lazy_config:
            continue
        
        if query < normal_config[0]:
            cost += dist(lazy_config[0], query)
            lazy_config[0] = query
            normal_config[0] = query

        elif query > normal_config[n_servers - 1]:
            cost += dist(query, lazy_config[n_servers - 1])
            lazy_config[n_servers - 1] = query
            normal_config[n_servers - 1] = query
        
        else:
            # Simulate the not so lazy approach
            prev = max(enumerate(normal_config), key=lambda x: x[1] if x[1] < query else 0)[0]
            next = min(enumerate(normal_config), key=lambda x: x[1] if x[1] > query else 100000)[0]

            min_dist = min(dist(query, normal_config[prev]), dist(normal_config[next], query))
            normal_config[prev] += min_dist
            normal_config[next] -= min_dist

            # Perform lazy action based on the normal DC algorithm
            lazy_idx = normal_config.index(query)
            cost += dist(lazy_config[lazy_idx], query)

            lazy_config[lazy_idx] = query

        normal_config.sort()
        lazy_config.sort()

        # Print result
        print(f"After querying {query} the server configuration is {lazy_config}")

    print(f"The final cost of the Lazy Double Coverage algorithm is {cost}")

def dist(x: int, y: int):
    return abs(x - y)