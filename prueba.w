var int x, fact, numero;

func void factorial(int n){
    for( x = 1 ; x = x + 1 ; x <= n){
        fact = fact * x;
    }

    write(" Factorial of ");
    write(n);
    write(" ");
    write(" is ");
    write(fact);
}

main {
    fact = 1;
    write(" Enter a number to find factorial: ");
    read(numero);
    factorial(numero);
}

end