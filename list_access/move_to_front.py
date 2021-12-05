import copy
import math
from typing import List


def solve(starting_list: List[int], queries: List[int]) -> int:
    total_cost = 0
    working_list = copy.deepcopy(starting_list) 
    
    for idx, query in enumerate(queries):
        cost = working_list.index(query) + 1
        total_cost += cost

        working_list.remove(query)
        working_list.insert(0, query)

        # Print result
        print(f"Iteration #{idx + 1} - access {query} - cost {cost} - new list: {working_list}")

    print(f"Total cost of the MTF algorithm: {total_cost} (optimum is therefore between {math.ceil(total_cost / 2)} and {total_cost})")

    return total_cost
