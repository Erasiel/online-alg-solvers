from bin_packing import best_fit
from bin_packing import first_fit
from bin_packing import next_fit
from bin_packing import harmonic


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