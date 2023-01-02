def sentinel_search(l,a):
    print("\nSentinal search")
    l.append(a)
    i = 0
    c = len(l)
    while (l[i] != a):
        i += 1
    if (i < c - 1):
        print(a, "was present at the lecture.")
    else:
        print(a, "was not present at the lecture.")

def linear_search(l,a):
    n = len(l)
    print("\nLinear search")
    found = False
    for i in range(0, n):
        if (l[i] == a):
            print(a , " was present at the lecture.")
            found = True
            break
    if(found == False):
        print(a, "was not present at the lecture.")

def binary_search(l,x):
    l.sort()
    lb = 0
    ub = len(l)-1
    mid = (lb + ub) // 2
    found = False
    while (lb <= ub):
        mid = (lb + ub) // 2
        if (l[mid] == x):
            print(x, "was present at the lecture.")
            found = True
            break
        elif (x > l[mid]):
            lb = mid + 1
        else:
            ub = mid - 1
    if found == False:
        print(x, "was not present at the lecture.")


def fibonaccianSearch(arr, x):
    arr.sort()
    n = len(l)
    found = False
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1

    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while (fibM > 1):
        i = min(offset + fibMMm2, n - 1)
        if (arr[i] < x):    #move one down
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x): #move two down
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            print(x, " was present at the lecture.")
            found = True
            break
    if (fibMMm1 and arr[n - 1] == x):
        print(x, " was present at the lecture.")
        found = True
    if(found == False):
        print(x, "was not present at the lecture.")
#-----------------------------------------------------------------------------------------------------#

l = list(map(int, input("Enter the roll no of students who attented lecture in a line : ").split()))

while(True):
    x = int(input("\nEnter the rollno to find."))
    print("\nChoose which index of search to perform. "
          "\n1.Linear search"
          "\n2.Sentinel search"
          "\n3.Binary search"
          "\n4.Fibonacci search"
          "\n0.Exit")
    option = int(input())
    if(option == 1):
        linear_search(l,x)
    if (option == 2):
        sentinel_search(l,x)
    if (option == 3):
        binary_search(l,x)
    if (option == 4):
        fibonaccianSearch(l,x);
    if (option == 0):
        exit()
