from copy import copy
import random
from array import array
from threading import Thread
from benchmark import TimeBenchmark



@TimeBenchmark
def InsertionSortArray(arr: array) -> array:
    newArray = copy(arr)
    for i in range(len(newArray)-1):
        minItemIndex = i
        for j in range(i+1, len(newArray)):
            if newArray[j] < newArray[minItemIndex]:
                minItemIndex = j
        if minItemIndex != i:
            (newArray[i], newArray[minItemIndex]) = (
                newArray[minItemIndex], newArray[i])
    return newArray


@TimeBenchmark
def InsertionSortList(lst: list) -> list:
    tempList = lst[::]
    newList = []
    while len(tempList) > 1:
        minItemIndex = 0
        for j in range(len(tempList)):
            if tempList[j] < tempList[minItemIndex]:
                minItemIndex = j
        newList.append(tempList.pop(minItemIndex))
    newList.append(tempList.pop(0))
    return newList


@TimeBenchmark
def BubbleSortArray(arr: array) -> array:
    newArray = copy(arr)
    for i in range(len(newArray)-1):
        for j in range(len(newArray)-i-1):
            if(newArray[j] > newArray[j+1]):
                (newArray[j], newArray[j+1]) = (newArray[j+1], newArray[j])
    return newArray


@TimeBenchmark
def BubbleSortList(lst: list) -> list:
    newList = lst[::]
    for i in range(len(newList)-1):
        for j in range(len(newList)-i-1):
            if(newList[j] > newList[j+1]):
                (newList[j], newList[j+1]) = (newList[j+1], newList[j])
    return newList


def _QuickSortArrImpl(arr: array, lIndex: int, rIndex: int):
    if lIndex < rIndex:
        pIndex = rIndex
        for i in range(rIndex, lIndex, -1):
            if arr[i] > arr[lIndex]:
                (arr[i], arr[pIndex]) = (arr[pIndex], arr[i])
                pIndex -= 1
        (arr[lIndex], arr[pIndex]) = (arr[pIndex], arr[lIndex])
        _QuickSortArrImpl(arr, lIndex, pIndex - 1)
        _QuickSortArrImpl(arr, pIndex + 1, rIndex)


@TimeBenchmark
def QuickSortArray(arr: array) -> array:
    newArray = copy(arr)
    _QuickSortArrImpl(newArray, 0, len(newArray)-1)
    return newArray


def _QuickSortLstImpl(lst: list):
    if len(lst) < 2:
        return lst
    else:
        leftList = []
        rightList = []
        for i in range(1, len(lst)):
            if lst[i] < lst[0]:
                leftList.append(lst[i])
            else:
                rightList.append(lst[i])
        return _QuickSortLstImpl(leftList) + [lst[0]] + _QuickSortLstImpl(rightList)


@TimeBenchmark
def QuickSortList(lst: list) -> list:
    return _QuickSortLstImpl(lst)


@TimeBenchmark
def CountingSortArray(arr: array) -> array:
    minValue = min(arr)
    maxValue = max(arr)
    countValues = maxValue-minValue+1
    offset = -minValue
    countArray = [0 for i in range(countValues)]
    for i in arr:
        countArray[i+offset] += 1
    newArray = []
    for i, count in enumerate(countArray):
        newArray.extend([i-offset] * count)
    return array('i', newArray)


@TimeBenchmark
def CountingSortList(arr: list) -> list:
    minValue = min(arr)
    maxValue = max(arr)
    countValues = maxValue-minValue+1
    offset = -minValue
    countArray = [0 for _ in range(countValues)]
    for i in arr:
        countArray[i+offset] += 1
    newList = []
    for i, count in enumerate(countArray):
        newList.extend([i-offset] * count)
    return newList


@TimeBenchmark
def CountingSortListParallel(arr: list) -> list:
    minValue = min(arr)
    maxValue = max(arr)
    countValues = maxValue-minValue+1
    offset = -minValue
    countArray = [0 for _ in range(countValues)]
    countThread = 4
    countPerThread = len(arr) // countThread
    threades = []
    for i in range(countThread):
        start = i * countPerThread
        end = len(arr) if i == countThread-1 else start + countPerThread
        thread = Thread(target=_CountValues, args=(arr, start, end, countArray, offset))
        threades.append(thread)
        thread.start()

    for thread in threades:
        thread.join()

    newList = []
    for i, count in enumerate(countArray):
        newList.extend([i-offset] * count)
    return newList


def _CountValues(arr: list, indexStart: int, indexEnd: int, countArray: list, offset: int):
    for i in range(indexStart, indexEnd):
        countArray[arr[i]+offset] += 1


@TimeBenchmark
def PythonSortArray(arr: array) -> array:
    return array(arr.typecode, sorted(arr))


@TimeBenchmark
def PythonSortList(lst: list) -> list:
    return sorted(lst)


if __name__ == '__main__':
    COUNT = 1000000
    # freeze_support()
    testList = [random.randint(-1000, 1001) for _ in range(COUNT)]
    # testArray = array('i', testList)
    # libSortArray = PythonSortArray(testArray)
    libSortList = PythonSortList(testList)
    # insertSortArray = InsertionSortArray(testArray)
    # insertSortList = InsertionSortList(testList)
    # bubbleSortArray = BubbleSortArray(testArray)
    # bubbleSortList = BubbleSortList(testList)
    # quickSortArray = QuickSortArray(testArray)
    # quickSortList = QuickSortList(testList)
    countingSortList = CountingSortList(testList)
    countingSortListParallel = CountingSortListParallel(testList)
    print(countingSortList == countingSortListParallel)

    # print(f"Исходный массив:\n[{', '.join(map(str, testArray))}]")
    # print(
    #     f"Сортировка массива библиотечная:\n[{', '.join(map(str, libSortArray))}]")
    # print(
    #     f"Сортировка массива вставкой:\n[{', '.join(map(str, insertSortArray))}]")
    # print(
    #     f"Сортировка массива пузырьком:\n[{', '.join(map(str, bubbleSortArray))}]")
    # print(f"Быстрая сорировка массива:\n[{', '.join(map(str, quickSortArray))}]")
    # print(
    #     f"Сортировка массива подсчетом:\n[{', '.join(map(str, countingSortArray))}]")

    # print(f"Исходный список:\n[{', '.join(map(str, testList))}]")
    # print(f"Сортировка списка библиотечная:\n[{', '.join(map(str, libSortList))}]")
    # print(f"Сортировка списка вставкой:\n[{', '.join(map(str, insertSortList))}]")
    # print(f"Сортировка списка пузырьком:\n[{', '.join(map(str, bubbleSortList))}]")
    # print(f"Быстрая сорировка списка:\n[{', '.join(map(str, quickSortList))}]")
