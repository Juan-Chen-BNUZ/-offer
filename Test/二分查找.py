def merge_search(alist, data):
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return merge_search(alist[0:mid], data)
    elif alist[mid] < data:
        return merge_search(alist[mid+1:], data)
    else:
        return True

if __name__ == '__main__':
    lis = [1,2,3,6,7,8,0]
    print(merge_search(lis,2))