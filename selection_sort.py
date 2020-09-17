# selection sort
# does n passes, first pass is n long and is shortened by 1 each time
# therefore runs in o(n^2 / 2) == o(n^2) time

def selection(draw, bars):
    # we are going to scan through and find the min
    # scan will be one shorter on each pass

    for i in range(len(bars)):
        # on ith pas make ith bar the starting min
        curr_min_index = i
        for j in range(i + 1, len(bars)):
            # highlight bar being looked at
            bars[j].colour = green
            draw()
            if bars[curr_min_index].height > bars[j].height:
                # if we have a new min
                bars[curr_min_index].colour = blue
                # colour old min as blue
                bars[j].colour = red
                # colour new min as red
                curr_min_index = j
            else:
                # otherwise colour bar back to blue
                bars[j].colour = blue
            draw()
        bars[i].height, bars[curr_min_index].height = bars[curr_min_index].height, bars[i].height
        bars[i].colour = blue
        draw()
