from bin_packing import best_fit
from bin_packing import first_fit
from bin_packing import next_fit
from bin_packing import harmonic
from list_access import move_to_front
from list_access import bit
from scheduling.time_model import lpt
from scheduling.time_model import intv_lpt


if __name__ == "__main__":
    # items = [0.4, 0.2, 0.3, 0.6, 0.4, 0.4, 0.2, 0.3]
    # items = [0.2, 0.9, 0.2, 0.9, 0.2, 0.9]
    items = [0.5, 0.6, 0.3, 0.4, 0.2, 0.5, 0.4]
    used_bins = next_fit.solve(items)
    print()
    used_bins = first_fit.solve(items)
    print()
    used_bins = best_fit.solve(items)
    print()
    used_bins = harmonic.solve(items, k=5)

    starting_list = [1, 2, 3, 4, 5]
    queries = [4, 2, 3, 2, 1, 4, 2, 5]
    move_to_front.solve(starting_list, queries)
    print()

    starting_bits = [0, 1, 1, 0, 0]
    bit.solve(starting_list, starting_bits, queries)

    jobs = [(1, 0), (1, 0), (2, 0), (3, 0), (2, 1), (2, 2), (3, 2), (1, 3), (2, 4), (1, 5)]
    lpt.solve(3, jobs)
    print()
    intv_lpt.solve(3, jobs)
    print()
