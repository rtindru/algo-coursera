import sys
pivot_choice = None
def construct_list(file_url):
    num_list = [int(line) for line in open(file_url, 'r')]
    return num_list

def quicksort(num_list, left=None, right=None):
    comparisons = 0
    if left is None:
        left = 0
    if right is None:
        right = len(num_list) - 1
    
    if right - left == 0:
        return 0

    pivot_position = partition(num_list, left, right)
    if pivot_position > left:
        comparisons += pivot_position - left
        comparisons += quicksort(num_list, left=left, right=pivot_position-1)
    if pivot_position < right:
        comparisons += right - pivot_position
        comparisons += quicksort(num_list, left=pivot_position+1, right=right)
    return comparisons

def partition(num_list, left, right):
    global pivot_choice
    pivot_sel = eval(pivot_choice)
    if pivot_sel == median:
        pivot_sel = median(left, (left+right)/2, right, num_list)
    swap(left, pivot_sel, num_list)
    pivot = num_list[left]
    i = left+1
    for j in range(left+1, right+1):
        if num_list[j] < pivot:
            swap(i, j, num_list)
            i += 1
    i -= 1
    swap(i, left, num_list)
    return i


def swap(x, y, num_list):
    temp = num_list[x]
    num_list[x] = num_list[y]
    num_list[y] = temp

def median(left, middle, right, num_list):
    if num_list[left] < num_list[middle]:
        if num_list[left] >= num_list[right]:
            return left
        elif num_list[middle] < num_list[right]:
            return middle
    else:
        if num_list[left] < num_list[right]:
            return left
        elif num_list[middle] >= num_list[right]:
            return middle
    return right

def main(argv=sys.argv):
    try:
        num_list = construct_list(argv[1])
    except IndexError as e:
        num_list = construct_list('QuickSort.txt')
        print 'Usage: python inversion_counter.py <file_path> <pivot_mode>\nDefaulting to sample data file - QuickSort.txt and Left Pivot Arrangement\n'
        print 'Pivot modes supported are <left, right, median>'
    try:
        global pivot_choice
        pivot_choice = argv[2].lower().strip()
        if pivot_choice not in ('left', 'right', 'median'):
            raise Exception
    except Exception as e:
        print 'Invalid choice of pivot. Defaulting to left'
        pivot_choice = 'left'    
    try:
        result = quicksort(num_list)
        print 'Total Number of Comparisons for {} strategy: {}'.format(pivot_choice, result)
    except Exception as e:
        print sys.stderr, e

if __name__ == "__main__":
    sys.exit(main())

