'''
Reads numbers from a file - represented as one number per line and assumed to be indexed by the line number and returns the number of inversions in said file.
Also sorts the array in the process.
'''
import sys

def construct_list(file_url):
    num_list = [int(line) for line in open(file_url, 'r')]
    return num_list

def count_inversions(array):
    if len(array) in (0, 1):
        return array, 0

    middle = len(array)/2

    left_array, left_inversions = count_inversions(array[:middle])
    right_array, right_inversions = count_inversions(array[middle:])

    sorted_array, split_inversions = merge_and_count(left_array, right_array)
    return sorted_array, left_inversions+right_inversions+split_inversions

def merge_and_count(left_array, right_array):
    left_len = len(left_array)
    right_len = len(right_array)

    i, j, inversions = 0, 0, 0
    result = []
    while i < left_len and j < right_len:
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            inversions += (left_len - i)
            j += 1
    result.extend(left_array[i:])
    result.extend(right_array[j:])

    return result, inversions

def main(argv=sys.argv):
    try:
        num_list = construct_list(argv[1])
    except IndexError as e:
        num_list = construct_list('IntegerArray.txt')
        print 'Usage: python inversion_counter.py <file_path>\nDefaulting to sample data file - IntegerArray.txt\n'
    try:
        result = count_inversions(num_list)
        print 'Total Number of Inversions: {}'.format(result[1])
    except Exception as e:
        print sys.stderr, e

if __name__ == "__main__":
    sys.exit(main())
