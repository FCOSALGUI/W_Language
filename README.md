# W Programming Language - Documentación

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
* **char**: Formato de un caractér **que debe ser escrito entre los símbolos ' '**.
* **string**: Formato de un string **que debe ser escrito entre los símbolos " "**.
* **bool**: Formato de un booleano que se identifica únicamente con los valores de **true** y **false**.

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

# Avance 1
Se ha utilizado PLY para crear toda la gramática del lenguaje y se ha probado que el lenguaje reconoce cada token y regla que se le ha asignado.
Además, se ha creado un archivo de prueba que representa la gramática correcta del lenguaje. El nombre de este archivo es: *"archivo.w"*.
Se ha añadido un README.md al repositorio que sirve como documentación del lenguaje para su correcto uso y sintáxis. Todavía no se completa este archivo pero será el referente principal del lenguaje. Además, se ha agregado la propuesta de proyecto en formato PDF para referencia respecto a la reglas de sintáxis que usa el lenguaje y sus diferentes componentes.

