from bin_packing import *
from list_access import *
from scheduling.time_model import *
from k_server import *
from strip_packing import *


if __name__ == "__main__":
    # Examples for bin packing
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
    print()

    # Examples for list access
    starting_list = [1, 2, 3, 4, 5]
    queries = [4, 2, 3, 2, 1, 4, 2, 5]
    move_to_front.solve(starting_list, queries)
    print()

    starting_bits = [0, 1, 1, 0, 0]
    bit.solve(starting_list, starting_bits, queries)
    print()

    # Examples for scheduling
    jobs = [(1, 0), (1, 0), (2, 0), (3, 0), (2, 1), (2, 2), (3, 2), (1, 3), (2, 4), (1, 5)]
    lpt.solve(3, jobs)
    print()
    intv_lpt.solve(3, jobs)
    print()

    # Examples for k server
    starting_config = [1, 4, 10]
    queries = [6, 9, 0, 3, 7]
    double_coverage.solve(starting_config, queries)
    print()
    lazy_double_coverage.solve(starting_config, queries)
    print()

    # Example for strip packing
    strips = [(0.4, 0.6), (0.3, 0.3), (0.5, 0.4), (0.1, 0.7), (0.7, 0.1), (0.3, 0.3)]
    next_fit_shelf.solve(0.5, strips)
    print()
