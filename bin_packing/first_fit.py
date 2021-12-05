from typing import List


def solve(items: List[float]) -> int:
    bins: List[List[float]] = [[]]
    
    for item in items:
        placed = False
        
        for bin in bins:
            if sum(bin) + item <= 1.0:
                bin.append(item)
                placed = True
                break
        
        if not placed:
            bins.append([item])
    
    # Print result
    print(f"The First Fit algorithm uses {len(bins)} bins")

    for idx, bin in enumerate(bins):
        bin_contents = ', '.join([str(item) for item in bin])
        print(f"Bin {idx + 1} contains: {bin_contents}")

    return len(bins)
