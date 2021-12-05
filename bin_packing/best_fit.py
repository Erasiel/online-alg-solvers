from typing import List


def solve(items: List[float]) -> int:
    bins: List[List[float]] = [[]]

    for item in items:
        fits = False
        best_bin = [0.0]

        for bin in bins:
            load = sum(bin) + item
            if load <= 1.0 and load >= sum(best_bin) + item:
                fits = True
                best_bin = bin
        
        if fits:
            best_bin.append(item)
        else:
            bins.append([item])
    
    # Print result
    print(f"The Best Fit algorithm uses {len(bins)} bins")

    for idx, bin in enumerate(bins):
        bin_contents = ', '.join([str(item) for item in bin])
        print(f"Bin {idx + 1} contains: {bin_contents}")

    return len(bins)