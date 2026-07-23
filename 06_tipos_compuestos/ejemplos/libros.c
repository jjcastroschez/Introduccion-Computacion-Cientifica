/*
 * Representar un libro con una struct en C.
 *
 * En C, la forma de agrupar datos heterogéneos bajo un solo nombre es
 * usar la palabra clave 'struct'. Es el equivalente al 'namedtuple' o
 * 'dataclass' de Python.
 *
 * Compilar con: gcc -o libros libros.c
 * Ejecutar con: ./libros
 *
 * Tema 6 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>


/* Declaramos el tipo Libro como una estructura con 4 campos */
struct Libro {
    char titulo[80];
    char autor[60];
    int anio;
    int paginas;
};


/* Función que recibe un puntero a Libro y lo muestra */
void mostrar_libro(struct Libro *l) {
    printf("Libro:\n");
    printf("  Título:  %s\n", l->titulo);
    printf("  Autor:   %s\n", l->autor);
    printf("  Año:     %d\n", l->ano);
    printf("  Páginas: %d\n", l->paginas);
}


int main(void) {
    /* Creamos una instancia con inicialización directa */
    struct Libro l1 = {"Bowie: Una Biografía", "M. Hesse", 2019, 167};

    /* Acceso a los campos con el operador punto (.) */
    printf("Acceso directo:  l1.titulo = %s\n", l1.titulo);
    printf("Acceso directo:  l1.año    = %d\n\n", l1.anio);

    /* Modificar un campo (las structs en C son mutables por defecto) */
    l1.paginas = 200;
    printf("Tras modificar:  l1.paginas = %d\n\n", l1.paginas);

    /* Pasar la struct a una función POR REFERENCIA con puntero */
    mostrar_libro(&l1);

    return 0;
}
