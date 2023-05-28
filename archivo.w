var int a, b, entero, entero1, entero_02;
var float flotante;
var float flotante__02;
var string hello;

var string palabras[25];
var int matrix[5][4];

dataframe tabla [3] = (int contador, string nombre, float resultado);

func int modulo01 (int variable_local, float cosa) {
    var int local02, resultado;
    var int contador;
    var float cosa1;

    local02 = variable_local;

    if (cosa1 > cosa) {
        resultado = 10;
    }

    else {
        (for contador = 10 ; contador + 1) {
            resultado = resultado + 1;
        }
    }

    return resultado;
} 

main {
    write(modulo01(2, 14.4));
}

end

