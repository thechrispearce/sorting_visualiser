# bubble sort
# does n passes, first pass is n long and is shortened by 1 each time
# therefore runs in o(n^2 / 2) == o(n^2) time

def bubble(draw, bars):
    for i in range(len(bars) - 1):
        swaps_in_run = 0
        for j in range(len(bars) - 1 - i):
            bars[j].colour = green
            bars[j + 1].colour = green
            draw()
            # if current bar has height larger than the bar directly to its right
            if bars[j].height > bars[j + 1].height:
                # note the height of the next bar (smaller)
                temp_height = bars[j + 1].height
                # make next bar height (smaller) equal to the height of current bar (larger)
                # at this point both bars have height that is the larger of the two
                bars[j + 1].height = bars[j].height
                # change height of current bar to the smaller value
                bars[j].height = temp_height
                swaps_in_run += 1
            bars[j].colour = blue
            bars[j + 1].colour = blue
        if swaps_in_run == 0:
            return True
        draw()
