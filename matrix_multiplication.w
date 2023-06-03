var int R1, C1, R2, C2;
var int matrix_1[3][3];
var int matrix_2[3][3];
var string lineJump;

var int result[3][3];

var int test;
func void mulMatrix()
var int i, j, k;
{
    for(i = 0; i = i+1; i < R1){
        for(j = 0; j = j+1; j < C2){
            result[i][j] = 0;
            for(k = 0; k = k+1; k < R2){
                result[i][j] = ((result[i][j]) + ((matrix_1[i][k]) * (matrix_2[k][j])));
            }
        }
    }
}

func void printMatrix()
var int i, j;
{
    for(i = 0; i = i+1; i < R1){
        for(j = 0; j = j+1; j < C1){
            write(result[i][j]);
        }
        read(lineJump);
    }
}

main {
    R1 = 3;
    C1 = 3;
    R2 = 3;
    C2 = 3;

    matrix_1[0][0] = 88; matrix_1[0][1] = 24; matrix_1[0][2] = 93;
    matrix_1[1][0] = 76; matrix_1[1][1] = 44; matrix_1[1][2] = 23;
    matrix_1[2][0] = 46; matrix_1[2][1] = 55; matrix_1[2][2] = 9;

    matrix_2[0][0] = 60; matrix_2[0][1] = 84; matrix_2[0][2] = 28;
    matrix_2[1][0] = 59; matrix_2[1][1] = 31; matrix_2[1][2] = 74;
    matrix_2[2][0] = 59; matrix_2[2][1] = 28; matrix_2[2][2] = 89;

    mulMatrix();
    printMatrix();
}

end