# quick sort
# splits the bars logn times and touches each bar at each split
# therefore runs in o(nlogn) time

def quick(draw, bars, start, end):
    # if the length of subsequent array is 1 or empty then it is sorted and we can return true
    if end <= start:
        return True

    # make new pivot the final bar in list
    pivot = bars[end]
    # comparison value is the height of the bar
    pivot_val = pivot.height

    low = []
    high = []
    piv = [pivot_val]
    index = start
    # increment index until we are at the end which is where our pivot is
    while index <= end - 1:
        # if bar height is greater than pivot value then we put it in the higher pile
        if bars[index].height > pivot_val:
            high.append(bars[index].height)
        # otherwise we put it in the lower pile
        else:
            low.append(bars[index].height)
        index += 1
    # new heights will be low ones plus pivot value plus high ones
    heights = low + piv + high

    # print some stuff to check it's going well
    # print(heights)

    # draw new set of bars
    index = start
    while index <= end:
        bars[index].colour = green
        draw()
        bars[index].height = heights[index - start]
        bars[index].colour = blue
        draw()
        index += 1

    # sort subsequent left and right arrays
    quick(draw, bars, start, start - 1 + len(low)) # left
    quick(draw, bars, end + 1 - len(high), end) # right
