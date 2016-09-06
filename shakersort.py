def shakersort(aList):
        n = len(aList)

        for i in range(n-1):
                if (i%2 == 0):
                        for j in range(0, n-1):
                                if aList[j] > aList[j+1]:
                                        aList[j],aList[j+1] = aList[j+1], aList[j]  
                else:
                        for k in range(n-1, 0, -1):
                                if aList[k-1] > aList[k]:
                                        aList[k],aList[k-1] = aList[k-1], aList[k]

if __name__ == ("__main__"):
        aList = [12, 44, 6, 7, 19, 4, 10, 18]
        shakersort(aList)
        print(aList)