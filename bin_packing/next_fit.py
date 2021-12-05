from typing import List


def solve(items: List[float]) -> int:
    bins: List[List[float]] = [[]]
    open_bin = 0

    for item in items:
        if sum(bins[open_bin]) + item <= 1:
            bins[open_bin].append(item)
        else:
            bins.append([item])
            open_bin += 1
    
    # Print result
    print(f"The Next Fit algorithm uses {len(bins)} bins")

    for idx, bin in enumerate(bins):
        bin_contents = ', '.join([str(item) for item in bin])
        print(f"Bin {idx + 1} contains: {bin_contents}")

    return len(bins)
