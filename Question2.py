def main():
    try:
        test_cases = int(input())   # Number of test cases
        test_case_input = {}
        for i in range(0, test_cases):
            l1 = [int(i) for i in input().split(" ")]   # Test cases value inputs
            l2 = [int(i) for i in input().split(" ")]   # Test cases value inputs
            if l1[0] == len(l2):
                l3 = []
                l3.append(l1)
                l3.append(l2)
                test_case_input[i] = l3
            else:
                raise Exception("Invalid Input")

        lst = []
        for x in test_case_input.values():
            check = 0
            for i in range(0,x[0][0]):
                if x[0][1] < x[1][i]:
                    check+=1
            lst.append(check)
        for i in lst:
            print(i)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()