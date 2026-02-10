%% Archivo: sum_list.erl
-module(sum_list).
-export([sum/1, main/1]).

% Suma los elementos de una lista.
sum([]) -> 0;  % Caso base: si la lista está vacía, la suma es 0.
sum([Head | Tail]) -> Head + sum(Tail).  % Caso recursivo: sumar el primer elemento al resultado de la suma del resto de la lista.

% Función principal, que se encarga de invocar la lógica y mostrar el resultado.
main(_Args) ->
    List = [1, 2, 3, 4, 5],  % La lista de números.
    Result = sum(List),  % Llamamos a la función sum para obtener el resultado.
    io:format("Suma: ~p~n", [Result]).  % Imprimir el resultado.
