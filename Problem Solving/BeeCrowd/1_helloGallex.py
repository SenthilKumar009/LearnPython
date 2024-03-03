def firstMessage(arrList):
    early = 9999
    if len(arrList) > 0:
        for arr in arrList:
            for element in arr:
                if arr[1] < early:
                    early = arr[1]
                    pos = arrList.index(arr)
                    return arrList[pos][0]
            else:
                return 0


arrList = [
            ['PlanetaXYZ', 2014, 5],
            ['PlanetaDosMacacos', 2020, 7],
            ['JINQEWIOSDFaa', 2043, 20]
          ]

print(firstMessage(arrList))




