# merge sort
# splits the bars logn times and touches each bar at each split
# therefore runs in o(nlogn) time

def merge(draw, bars, start, end):

    if end <= start:
        return bars

    mid = (start + end) // 2
    merge(draw, bars, start, mid) # left
    merge(draw, bars, mid + 1, end)  # right

    left_index = start # points to the start of our left
    right_index = mid + 1 # points to the start of our right
    temp = []

    while left_index <= mid and right_index <= end:
        if bars[left_index].height < bars[right_index].height:
            temp.append(bars[left_index].height)
            left_index += 1
        else:
            temp.append(bars[right_index].height)
            right_index += 1

    while right_index <= end:
        temp.append(bars[right_index].height)
        right_index += 1

    while left_index <= mid:
        temp.append(bars[left_index].height)
        left_index += 1

    # put the new values in
    for i in range(len(temp)):
        bars[start + i].colour = green
        draw()
        bars[start + i].height = temp[i]
        bars[start + i].colour = blue
        draw()

    return bars
