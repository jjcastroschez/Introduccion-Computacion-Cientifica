maximo :: [Int] -> Int
maximo [x] = x  -- Caso base: si solo hay un elemento, es el máximo
maximo (x:xs) = max x (maximo xs)  -- Comparamos la cabeza con el máximo de la cola

-- Uso de la función
main = do
    let numeros = [3, 5, 7, 2, 8, 1]
    print ("El número máximo es: " ++ show (maximo numeros))
