from typing import List


def solve(items: List[float], k: int) -> int:
    # bins: List[List[List[float]]] = [[[]]] * k
    bins: List[List[List[float]]] = [[[]] for _ in range(k)]
    open_bins: List[int] = [0] * k

    for item in items:
        placed = False

        for w in range(2, k + 1):
            min_w = 1 / w
            max_w = 1 / (w - 1)

            if min_w < item and item <= max_w:
                bin_idx = w - 2
                load = sum(bins[bin_idx][open_bins[bin_idx]]) + item

                if load <= 1.0:
                    bins[bin_idx][open_bins[bin_idx]].append(item)
                else:
                    bins[bin_idx].append([item])
                    open_bins[bin_idx] += 1

                placed = True
                break

        # Small items go in the last bin
        if not placed:
            bin_idx = k - 1
            load = sum(bins[bin_idx][open_bins[bin_idx]]) + item

            if load <= 1.0:
                bins[bin_idx][open_bins[bin_idx]].append(item)
            else:
                bins[bin_idx].append([item])
                open_bins[bin_idx] += 1

    # Print result
    n_bins = sum([len(b) for b in bins if b[0]])
    print(f"The Harmonic({k}) algorithm uses {n_bins} bins")

    idx = 1
    for w in range(2, k+1):
        print(f"1/{w} < x <= 1/{w - 1} items:")
        for bin in bins[w-2]:
            if bin:
                bin_contents = ', '.join(str(item) for item in bin)
                print(f"\tBin {idx} contains: {bin_contents}")
                idx += 1
            else:
                print(f"\tThere are no items in this category")

    print(f" 0 <= x <= 1/{k} items:")
    for bin in bins[k-1]:
        if bin:
            bin_contents = ', '.join(str(item) for item in bin)
            print(f"\tBin {idx} contains: {bin_contents}")
        else:
            print(f"\tThere are no items in this category")

    return n_bins
