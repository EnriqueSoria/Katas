#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PIEDRA  0
#define PAPEL   1
#define TIJERAS 2
#define LAGARTO 3
#define SPOCK   4

/* Frases */
char a[] = "La piedra aplasta las tijeras";
char b[] = "La piedra aplasta al lagarto";
char c[] = "El papel cubre a la piedra";
char d[] = "El papel desautoriza a Spock";
char e[] = "Las tijeras cortan el papel";
char f[] = "Las tijeras decapitan al lagarto";
char g[] = "El lagarto se come el papel";
char h[] = "El lagarto envenena a Spock";
char i[] = "Spock vaporiza la piedra";
char j[] = "Spock destroza las tijeras";

/* Tabla de resultados */
char *fr[5][5][1] = {
    { {NULL}, {NULL}, {&a}, {&b}, {NULL} }, // Piedra
    { {&c}, {NULL}, {NULL}, {NULL}, {&d} }, // Papel
    { {NULL}, {&e}, {NULL}, {&f}, {NULL}},  // Tijeras
    { {NULL}, {&g}, {NULL}, {NULL}, {&h}},  // Lagarto
    { {&i}, {NULL}, {&j}, {NULL}, {NULL}},  // Spock
};

int main()
{
    int user;
    printf( "Elige:\n- Piedra  (0)\n- Papel   (1)\n- Tijeras (2)\n- Lagarto (3)\n- Spock   (4)\n\n\t" );
    scanf ( "%d", &user);

    srand ( getpid() );
    int cpu =  rand() % 5;

    if ( user == cpu )
        printf( "Empate" );
    else
        if( *fr[user][cpu] != NULL )
            printf("Has ganado! \n%s", *fr[user][cpu]);
        else
            printf("Has perdido! \n%s",*fr[cpu][user]);
    getch(); // deprecated
    
    return 0;
}
