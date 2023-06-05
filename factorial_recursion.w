var int x;

func int fact(int y)
var int result;
{
    if (y #= 0){
        result = 1;
    }

    else {
        result = y * (fact(y - 1)) ;
    }

    return result;
}

main {
    write(" Enter a number to find factorial: ");
    read(x);
    write(fact(x));
}

end