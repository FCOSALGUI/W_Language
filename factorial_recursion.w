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
    x = 7;
    write(fact(x));
}

end