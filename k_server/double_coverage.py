from typing import List


def solve(starting_config: List[int], queries: List[int]):
    config = sorted(starting_config)
    cost = 0
    n_servers = len(config)

    for query in queries:
        if query in config:
            continue
        
        if query < config[0]:
            cost += dist(config[0], query)
            config[0] = query
        elif query > config[n_servers - 1]:
            cost += dist(query, config[n_servers - 1])
            config[n_servers - 1] = query
        else:
            prev = max(enumerate(config), key=lambda x: x[1] if x[1] < query else 0)[0]
            next = min(enumerate(config), key=lambda x: x[1] if x[1] > query else 100000)[0]

            min_dist = min(dist(query, config[prev]), dist(config[next], query))
            config[prev] += min_dist
            config[next] -= min_dist

            cost += min_dist * 2

        config.sort()
        # Print result
        print(f"After querying {query} the server configuration is {config}")

    print(f"The final cost of the Double Coverage algorithm is {cost}")

def dist(x: int, y: int):
    return abs(x - y)
