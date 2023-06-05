# W Programming Language - Quick Reference Manual

## Descripción del Proyecto
Los archivos incluídos dentro de este proyecto son para llevar a cabo la compilación, a través de una máquina virtual
y con ayuda de PLY, de un lenguaje de programación denominado como W.

Este lenguaje de programación tiene el propósito de dar las herramientas para que desarrolladores puedan llevar a cabo análisis estadístico a través del uso de dataframes estipulados dentro del programa, más otros estándares comunes en lenguajes de alto nivel como el uso de módulos, variables, arreglos y matrices. 

Además, la estructura del dataframe cuenta con funciones especiales ya implementadas dentro del programa:

* **Keys**: Regresa las llaves que identifican a cada columna en forma de arreglo de strings.
* **Avg**: Regresa el valor promedio de una columna del dataframe en formato de float. La columna tiene que ser de tipo entero o flotante.
* **Count**: Regresa la cantidad de filas dentro del dataframe en formato de int.
* **Max**: Regresa el valor más alto dentro de una columna del dataframe en formato de float. La columna tiene que ser de tipo entero o flotante.
* **Min**: Regresa el valor más bajo dentro de una columna del dataframe en formato de float. La columna tiene que ser de tipo entero o flotante.
* **Sum**: Regresa la suma de los valores de una columna del dataframe en formato de float. La columna tiene que ser de tipo entero o flotante.
* **Plot**: Crea una imagen de un gráfico de dispersión de los elementos de un dataframe y la guarda en la misma carpeta donde se guardó el programa que se está compilando.
* **Histogram**: Crea una imagen de un histograma de los elementos de un dataframe y la guarda en la misma carpeta donde se guardó el programa que se está compilando.
* **Print**: Se imprimen las columnas y filas de todo el dataframe en consola en formato de tabla. 

## Formato de sintaxis del lenguaje
El flujo del programa está determinado por pasos que tienen que ser seguidos como se presenta a continuación, de no seguirse está sintaxis, el programa no compilará correctamente.

Es decir, si primero se define cómo declarar variables y luego cómo declarar dataframes, entonces no se pueden declarar dataframes antes que las variables ni se pueden declarar variables después de los dataframes. Por esta razón es que esta sección se ha hecho en el orden en el que se espera que se declaren los diferentes componentes del programa.

### Tipos atómicos con los que trabaja el lenguaje
El lenguaje trabaja con tipos atómicos definidos, los cuáles se identifican cómo:
* **int**: Formato de un número entero.
* **float**: Formato de un número flotante.
* **char**: Formato de un caractér **que debe ser escrito entre los símbolos ' ' con un espacio entre los simbolos**.
* **string**: Formato de un string **que debe ser escrito entre los símbolos " " con un espacio entre las comillas**.
* **bool**: Formato de un booleano que se identifica únicamente con los valores de **true** y **false**.

### Nota importante sobre la estructura de strings y chars
Los strings y chars de este lenguaje tienen una estructura muy especial, y de no seguirse **causará un error grave en ejecución**.

La estructura correcta para escribir strings es la siguiente:
```
palabra = " Hello World! ";
```

Formas incorrectas de escribir un string desde el código:
```
"Hola soy una palabra "
" Hola soy un string"
"It's me, hi, I'm the problem it's me"
```

### Declaración de variables de tipo atómico
El primer paso que se debe llevar a cabo dentro del programa es declarar las variables con las que se trabajaran, las cuáles estarán dentro de un scope global y que podrán ser utilizadas por todo el programa. Una vez declaradas aquí, no podrán volver a declararse variables ni funciones ni dataframes con el mismo nombre.

La sintaxis para declarar una variable de tipo atómico es la siguiente:
```
var TIPO id;
var TIPO id0, id1, id2 ... idn; 
```
**Ejemplo**
```
var int x;
var float numero01, numero02, numero23;
```

### Declaración de arreglos y matrices
Se pueden declarar arreglos y matrices de tipo atómico con un número definido de dimensiones **(no dinámicos)**.

La sintaxis para declarar un arreglo es:
```
var TIPO id[cte_entera];
```
**Ejemplo**

Declarar un arreglo de enteros de 10 posiciones [0 - 9]:
```
var int arreglo[10];
```
De forma similar, se pueden declarar matrices de 2 dimensiones.

La sintaxis para declarar una matriz es:
```
var TIPO id[cte_entera][cte_entera];
```
**Ejemplo**

Declarar una matriz de flotantes de 30 filas x 25 columnas:
```
var float arreglo[30][25];
```

**NO SE PUEDEN DECLARAR VARIOS ARREGLOS EN LA MISMA LÍNEA DE CÓDIGO, TIENEN QUE SER EN ESTATUTOS DIFERENTES**

### Declaración de dataframes
Los dataframes son conjuntos de datos con columnas que pueden ser de distinto tipo atómico y a los que se les van anexando filas con datos de su respectivo tipo de columna.

La sintaxis para declarar un dataframe es:
```
dataframe id [cte_int] = (TIPO id01, TIPO id02, TIPO id03 ... TIPO idn);
```
**Ejemplo**

Declarar un dataframe de nombre *tabla* que contenga 3 columnas; *contador* de tipo int; *nombre* de tipo string; *resultado* de tipo float: 
```
dataframe tabla [3] = (int contador, string nombre, float resultado);
```

### Declaración de módulos o funciones
Los módulos o funciones son un conjunto de estatutos que regresan un resultado si son de tipo atómico, o bien, pueden solo correr una serie de estatutos sin regresar un resultado si son de tipo void.

La sintaxis para declarar una función es:
```
func (TIPO | void) id (TIPO id01, TIPO id02, TIPO id03 ... TIPO idn) {
    DECLARACION DE VARIABLES
    
    CONJUNTO DE ESTATUTOS

    return EXP;
}
```

### Consideraciones al momento de declarar funciones

Hay muchos aspectos que considerar respecto a las funciones:
1. Dentro de las funciones se deben declarar las variables de tipo local antes de realizar cualquier estatuto, ya que no se podrán declarar variables después de que el compilador detecte un estatuto de algún tipo.
2. Se pueden trabajar con variables globales ya declaradas en la sección del programa de declaración de variables.
3. No se pueden declarar dataframes de forma local en una función. Todos los dataframes tienen que ser creados en su respectiva declaración antes de que se empiecen a declarar funciones.
4. Se puede trabajar con dataframes que hayan sido previamente declarados de forma global dentro de las funciones.
5. Las funciones de tipo atómico requieren tener un estatuto al final que regrese una expresión (**return EXP**).
6. Las funciones de tipo void no requieren tener un estatuto que regrese una expresión.

## Tipos de estatutos (STATEMENTS)
El cuerpo de una función y de la función *main*, que será aquella en la cuál se definirá el inicio del flujo de ejecución del programa, puede componerse de los siguientes estatutos o statements:

### Asignación de variables
Para asignarle el valor a una variable esta tiene que haber sido declarada previamente en la sección de declaración de variables siguiendo las siguientes reglas:

1. Las variables globales son declaradas antes de la declaración de dataframes y de la declaración de funciones.
2. No se le puede asignar un valor a una variable que no haya sido previamente declarada.
3. Las variables de tipo local tienen que ser declaradas al principio de cada función para poderles asignar un valor. 

La sintaxis para asignarle el valor a una variable es la siguiente:
```
id = EXP;
```

### Asignación de arreglos y matrices
Los arreglos y matrices siguen el mismo conjunto de reglas que la asignación de variables.

La sintaxis para asignarle un valor a un arreglo o matriz es la siguiente:
```
id [EXP] = EXP;
id [EXP][EXP] = EXP;
```

### Anexar filas a un dataframe
Para anexar filas a un dataframe se deben seguir las siguientes reglas:

1. El dataframe tuvo que haber sido declarado en la sección de declaración de dataframes.
2. Todos los dataframes son globales, por lo que cualquier función interactuar con ellos.
3. Los parámetros que se le envíen a un dataframe tienen que ser del mismo número de columnas con el que se declaró y los parámetros tienen que ser del mismo tipo de columna al que se quieren guardar. No puede haber parámetros vacíos ni nulos.

Correcta sintáxis para anexar una fila a un dataframe:

```
id.push(EXP, EXP, EXP ... , EXP);
```

Incorrecta sintáxis de un dataframe:
```
id.push(EXP,,,EXP)
id.push( EXP, EXP, , EXP);
```

### Condicionales (if y else)
Para declarar un condicional se debe seguir la siguiente estructura:
```
if(EXP de tipo booleana){
    STATEMENTS
}
else{
    STATEMENTS
}
```
### Ciclos y loops (while y for)
Para declarar un ciclo de tipo while se debe seguir la siguiente estructura:
```
while(EXP de tipo booleana){
    STATEMENTS
}
```
A pesar de que la estructura del while es súmamente similar a otros lenguajes, la del for es diferente y se debe seguir así:
```
for(assignment1 assignment2 EXP de tipo booleana){
    STATEMENTS
}
```
El *assignment1* corresponde a la asignación inicial de la variable de control.

El *assignment2* corresponde a la asignación que se le hará a la variable de control de aumento, o bien, de disminución.

**Todos los assignments terminan en *;***

**Es muy importante recordar que la variable de control tiene que ser de tipo entera**

### Asignarle valor a una variable desde consola (read)
Se le puede asignar un valor a una variable declarada previamente en el programa con el comando *read* y su sintáxis es de la siguiente manera:
```
read(ID);
```
Cualquier valor puesto en consola se guardará en la variable especificada como *ID*.

También se puede usar como salto de línea al momento de imprimir en consola ya que el programa no cuenta con un símbolo específico para esto.

**Es muy importante recordar que el valor que se le asignará a la variable determinada en esta sección debe ser del mismo tipo que la variable**

### Imprimir en consola (write)
Para escribir una expresión en consola se debe seguir la siguiente estructura:
```
write(EXP);
```
La expresión que se escribe puede ser de cualquier tipo, y parte de las expresiones también se incluyen las variables declaradas con un valor asignado. Si la variable no tiene valor asignado, no sempodrá imprimir. Lo mismo pasa con los arreglos, matrices y funciones.

### Llamadas a funciones
Las llamadas a funciones tienen muchas consideraciones a tomar en cuenta para evitar errores en compilación y en ejecución.
1. Las funciones debieron ser declaradas previamente.
2. Si son de tipo *void* estas NO pueden ser utilizadas como parte de una expresión pues no regresan ningún valor.
3. Los parámetros que se le envían a la función tienen que ser del mismo tipo con el que fueron declarados.
4. El número de parámetros que se le envían a la función tienen que ser exactamente a los mismo declarados.
5. Las funciones que no son de tipo *void* pueden ser utilizas en expresiones siempre y cuando estén entre paréntesis.
```
x = 3 * y * (func(x-1));
```
De no seguirse esta notación, el resultado de la expresión será incorrecto e inconsistente.

Para llevar a cabo la notación correcta de una llamada de función se debe hacer lo siguiente:
```
ID(EXP1, EXP2, ... , EXPn);
```
Esta sintáxis también aplica para funciones que se utilizan como parte de una expresión tomando en cuenta las consideraciones mencionadas anteriormente.

### Expresiones y operaciones que puede realizar el lenguaje
Una expresión se compone de 3 elementos
1. El operando izquierdo
2. El signo de la operación
3. El operando derecho

Por ejemplo, para realizar una expresión de suma esta debe llevar a cabo de la siguiente manera:
```
x + y;
```
Lo mismo aplica para todos los símbolos que se mencionarán a continuación.

### Símbolos y sus operaciones
**Las operaciones se hacen de izquierda a derecha respetando la jerarquía que se menciona a continuación, resolviendo las operaciones en el orden que se indica**
1. **(  )** Se encarga de encasillar una expresión y que esta se resuelva antes que cualquier otra cosa en la expresión, pudiendo tener múltiples paréntesis anidados.
2. **\*** y **/** Multiplica o divide los 2 operandos.
3. **+** y **-** Suma o resta los 2 operandos.
4. **<** , **>** **<=** , **>=** , **#=** y **!=** Compara los 2 operandos y corresponden al *menor que*, *mayor que*, *menor o igual que*, *mayor o igual que*, *exactamente igual que* y *no igual que*, respectivamente.
5. **&&** y **||** Es el *and* y *or* lógico respectivamente para expresiones de tipo booleana.

### Operandos
Los operandos son los componentes a ser computados por el programa con su respectivo símbolo y pueden consistir de los siguientes elementos:
1. Constantes enteras sin signo (0,1,2,3,4... n)
2. Constantes flotantes (1.23, 4.5, 0.5)
3. Constantes de tipo string (" Hello World! ")
4. Constantes de tipo char (' a ')
5. Booleanas *true* o *false*
6. Variables de tipo atómico **que hayan sido declaradas previamente y tengan un valor asignado**
7. Elementos indexados de matrices **que se encuentren entre paréntesis *(  )***
```
resultado = (matriz[i+1][j+1]) + (a/b) * ((arreglo[x]) + z);
```
8. Llamadas a funciones que regresen un valor **que se encuentren entre paréntesis *(  )***
```
resultado = (funcion1(x+4, (i-3) * 80)) + (a/b) * ((funcion2(n - 1)) + z);
```

## Link del video demo
[Video][1]

[1]: https://youtu.be/vepGV08t4Jk