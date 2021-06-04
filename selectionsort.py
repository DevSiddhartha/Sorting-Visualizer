import time

def selection_sort(data, drawData, timeTick):
    minIdx = 0
    while minIdx < len(data)-1:
        minVal = data[minIdx]
        replaceidx = minIdx
        for i in range(minIdx + 1, len(data)):
            if data[i] < minVal:
                minVal = data[i]
                replaceidx = i
        drawData(data, ['green' if x == minIdx or x == replaceidx else 'red' for x in range(len(data))])
        data[minIdx], data[replaceidx] = data[replaceidx] , data[minIdx]
        minIdx += 1
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
