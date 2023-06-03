var int i;
var int t1, t2;
var int nextTerm;
var int numero;
main {
    t1 = 0;
    t2 = 1;
    nextTerm = t1 + t2;

    write(" Escriba el numero a aplicar la serie de fibonacci ");
    read(numero);

    for(i = 3; i = i+1; i <= numero){
        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
    }

    write(" Resultado: ");
    write(nextTerm);
}

end