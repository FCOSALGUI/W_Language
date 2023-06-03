var int numero;

func int fibonacci(int n)
var int resultado;
{
    if(n <= 1){
        resultado = n;
    }

    else{
        resultado = (fibonacci(n - 1)) + (fibonacci(n - 2));
    }

    return resultado;
}

main {
    write(" Escriba el numero a aplicar la serie de fibonacci ");
    read(numero);

    write(" Resultado: ");
    write(fibonacci(numero));
}

end