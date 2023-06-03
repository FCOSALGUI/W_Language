var int arr[10];
var int resultado, n, numero;

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

func int find(int n, int number)
var int i, foundPosition;
var bool found;
{
    found = false;
    for(i=0; i = i+1; i < n){
        if(arr[i] #= number){
            found = true;
            foundPosition = i;
        }
        if(found #= true){
            i = n;
        }
    }

    if(found #= false){
        foundPosition = (0 - 1);
    }

    return foundPosition;
}

main {
    n = 10;
    arr[0] = 66;
    arr[1] = 80;
    arr[2] = 47;
    arr[3] = 26;
    arr[4] = 96;
    arr[5] = 94;
    arr[6] = 43;
    arr[7] = 11;
    arr[8] = 29;
    arr[9] = 89;

    write(" Escriba numero a ser encontrado ");
    read(numero);

    resultado = find(n, numero);

    if(resultado #= (0 - 1)){
        write(" Numero no encontrado en arreglo ");
    }
    else {
        write(" Numero encontrado en posicion ");
        write(resultado);
    }
}

end