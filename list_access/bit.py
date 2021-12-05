import copy
from typing import List


def solve(starting_list: List[int], starting_bits: List[int], queries: List[int]) -> int:
    total_cost = 0
    working_list = copy.deepcopy(starting_list) 
    working_bits = copy.deepcopy(starting_bits)
    
    for idx, query in enumerate(queries):
        index = working_list.index(query)
        cost = index + 1
        total_cost += cost

        if working_bits[index] == 0:
            working_bits.pop(index)
            working_list.pop(index)
            working_bits.insert(0, 1)
            working_list.insert(0, query)
            
        else:
            working_bits[index] = 0

        # Print result
        list_with_bits = [f"{working_list[i]}({working_bits[i]})" for i in range(len(working_list))]
        list_to_print = f"[{', '.join(list_with_bits)}]"
        print(f"Iteration #{idx + 1} - access {query} - cost {cost} - new list: {list_to_print}")

    print(f"Total cost of the BIT algorithm: {total_cost}")

    return total_cost
