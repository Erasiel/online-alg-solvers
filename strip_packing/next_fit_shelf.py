from typing import Dict, List, Tuple


def solve(r: float, strips: List[Tuple[float, float]]):
    shelves: Dict[int, List[List[float]]] = dict()
    shelf_widths: Dict[int, float] = dict()
    open_shelves: Dict[int, int] = dict()

    for strip in strips:
        height_cat = 0
        width, height = strip

        while height <= r**(height_cat+1):
            # print(f"{r**(height_cat+1)} vs {height}")
            height_cat += 1

        # Check if shelf is opened
        if height_cat in shelves:
            # Check if item fits
            if shelf_widths[height_cat] + width <= 1.0:
                open_shelf = open_shelves[height_cat]
                shelves[height_cat][open_shelf].append(strip)
                shelf_widths[height_cat] += width

            else:
                shelves[height_cat].append([strip])
                shelf_widths[height_cat] = width
                open_shelves[height_cat] += 1

        else:
            shelves[height_cat] = [[strip]]
            shelf_widths[height_cat] = width
            open_shelves[height_cat] = 0

    total_height = 0.0

    # Print result
    idx = 1
    for height_cat, shelf_list in shelves.items():
        print(f"1/{height_cat} < x <= 1/{height_cat + 1} items:")

        total_height += r**height_cat * len(shelf_list)

        for shelf in shelf_list:
            shelf_contents = ', '.join(f"({h}, {w})" for h, w in shelf)
            print(f"\tShelf #{idx} contains: {shelf_contents}")
            idx += 1
    
    print(f"Total cost of the Next Fit Shelf algorithm is {total_height}")
