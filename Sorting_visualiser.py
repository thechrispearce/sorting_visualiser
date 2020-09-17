"""Controls:
    - Press r key to randomise heights of bars
    - Press b key to deploy bubble sort
    - Press q key to deploy quick sort
    - Press m key to deploy merge sort
    - Press m key to deploy selection sort
"""
import pygame
import random
import math as m

pygame.init()

height = 700
width = 1401
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting visualiser")

# define some colours for later
dark_gray = [75, 75, 76]
lite_gray = [200, 200, 200]
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [85, 148, 255]
dark_blue = [0, 0, 255]
yellow = [255, 255, 0]
purple = [128, 0, 128]
orange = [255, 165, 0]
cyan = [64, 224, 208]

class Bar:

    def __init__(self, index, height, width, total_bars):
        self.index = index
        self.x = 1 + (width + 1) * (index)
        self.y = 0
        self.height = height
        self.width = width
        self.colour = blue
        self.total_bars = total_bars

    def get_index(self):
        return self.index

    def get_height(self):
        return self.height

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, 700 - self.height, self.width, self.height))


def make_bars(bars, width):
    array = []
    wid = ((width - 1) // bars) - 1
    for i in range(bars):
        height = random.randint(1, 600)
        bar = Bar(i, height, wid, bars)
        array.append(bar)
    return array

def randomise(array):
    for bar in array:
        bar.height = random.randint(1, 600)
    return array


def draw(window, bars):
    # Updated/drawn on every pass
    window.fill(dark_gray)
    for bar in bars:
        bar.draw(window)
    pygame.display.update()

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

# main function
def main(window, width):
    num_bars = 70
    bars = make_bars(num_bars, width)

    running = True
    while running:
        draw(window, bars)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bubble(lambda: draw(window, bars), bars)

                if event.key == pygame.K_q:
                    quick(lambda: draw(window, bars), bars, 0, num_bars - 1)

                if event.key == pygame.K_m:
                    merge(lambda: draw(window, bars), bars, 0, num_bars - 1)

                if event.key == pygame.K_s:
                    selection(lambda: draw(window, bars), bars)

                if event.key == pygame.K_r:
                    randomise(bars)

    pygame.quit()

main(window, width)