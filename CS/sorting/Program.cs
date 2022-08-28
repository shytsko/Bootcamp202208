int[] array = new int[20];
Random rnd = new Random();

for (int i = 0; i < array.Length; i++)
    array[i] = rnd.Next(100);

Console.WriteLine($"Исходный массив:\t[{string.Join(", ", array)}]");
int[] sortArray1 = InsertionSort(array);
Console.WriteLine($"Сортировка вставкой:\t[{string.Join(", ", sortArray1)}]");
int[] sortArray2 = BubbleSort(array);
Console.WriteLine($"Сортировка пузырьком:\t[{string.Join(", ", sortArray2)}]");
int[] sortArray3 = QuickSort(array);
Console.WriteLine($"Быстрая сотрировка:\t[{string.Join(", ", sortArray3)}]");
Console.WriteLine($"Исходный массив:\t[{string.Join(", ", array)}]");

int[] InsertionSort(int[] array)
{
    int[] newArray = (int[])array.Clone();
    for (int i = 0; i < newArray.Length - 1; i++)
    {
        int minItemIndex = i;
        for (int j = i + 1; j < newArray.Length; j++)
            if (newArray[j] < newArray[minItemIndex])
                minItemIndex = j;
        if (minItemIndex != i)
            (newArray[i], newArray[minItemIndex]) = (newArray[minItemIndex], newArray[i]);
    }
    return newArray;
}

int[] BubbleSort(int[] array)
{
    int[] newArray = (int[])array.Clone();

    for (int i = 0; i < newArray.Length - 1; i++)
        for (int j = 0; j < newArray.Length - i - 1; j++)
            if (newArray[j] > newArray[j + 1])
                (newArray[j], newArray[j + 1]) = (newArray[j + 1], newArray[j]);
    return newArray;
}

int[] QuickSort(int[] array)
{
    int[] newArray = (int[])array.Clone();
    QuickSortImpl(newArray, 0, newArray.Length - 1);
    return newArray;
}

void QuickSortImpl(int[] array, int lIndex, int rIndex)
{
    if (lIndex < rIndex)
    {
        int pIndex = rIndex;
        for (int i = rIndex; i > lIndex; i--)
        {
            if (array[i] > array[lIndex])
            {
                (array[i], array[pIndex]) = (array[pIndex], array[i]);
                pIndex--;
            }
        }
        (array[lIndex], array[pIndex]) = (array[pIndex], array[lIndex]);

        QuickSortImpl(array, lIndex, pIndex - 1);
        QuickSortImpl(array, pIndex + 1, rIndex);
    }
}