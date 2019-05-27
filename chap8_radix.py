def get_digit(maxnum):
    digit = 0
    while maxnum > 1:
        maxnum = maxnum / 10
        digit = digit + 1
    
    return digit

def count_sort(arr):
    C = []
    for i in range(1, len(arr)+1):
        C[i] = 0
    for i in range(1, len(arr)+1):
        C[arr[i]] = C[arr[i]] + 1
    for i in range(1, len(arr)+1):
        pass
    
def radix_sort(digit, arr):
    count = [0]*(10)
    temp = [0]*(len(arr))
    radix = 1
    for i in range(digit):
        for j in range(10):
            count[j] = 0

        for j in range(len(arr)):
            k = int((arr[j] / radix) % 10)
            print("k111 = ", k)
            count[k] = count[k] + 1
        print("count = ", count)

        for j in range(1,10):
            count[j] = count[j-1] + count[j]
        print("count222 = ", count)

        for j in range(len(arr)-1, -1, -1):
            print("j = ", j)
            k = int((arr[j] / radix) % 10)
            print("k = ", k)
            print("count[k]", count[k])
            print("temp[count[k]] = ", temp[count[k]-1])
            temp[count[k]-1] = arr[j]
            print("temp[count[k]] = ", temp[count[k]-1])
            print("temp = ", temp)
            count[k] = count[k] - 1

        print("temp = ", temp)
        
        for j in range(len(arr)):
            arr[j] = temp[j]
        
        radix = radix * 10    


def main():
    arr = [123, 345, 256, 789, 23456, 447, 123, 5]
    maxnum = max(arr)
    digit = get_digit(maxnum)
    radix_sort(digit, arr)
    print("arr = ", arr)

main()


