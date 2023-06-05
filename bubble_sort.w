var int arr[7];
var int n;
var string lineJump;

func void bubbleSort(int n)
var int i, j, temp;
var bool swapped;
{
    for(i=0; i=i+1; i < n-1){
        swapped = false;

        for(j=0; j=j+1; j < n-i-1){
            if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if(swapped #= false){
            i = n;
        }
    }
}

func void printArray()
var int i;
{
    for(i=0; i=i+1; i < n){
        write(arr[i]);
    }
}

main {
    arr[0] = 64;
    arr[1] = 34;
    arr[2] = 25;
    arr[3] = 12;
    arr[4] = 22;
    arr[5] = 11;
    arr[6] = 90;

    n = 7;

    write(" Original Array: (press enter to see elements of array) ");
    read(lineJump);
    printArray();

    bubbleSort(n);
    read(lineJump);
    write(" Sorted Array: (press enter to see elements of array) ");
    read(lineJump);
    printArray();
}

end