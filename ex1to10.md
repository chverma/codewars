# Codewars Valencia 2025 del 1 al 10


## 1. Moviegoers
**Puntos:** 1

### Introducción
Stanley y Alfred han comprado entradas para un cine y quieren ir directamente a la sala de proyección. Stanley debe pasar primero a recoger a Alfred en su casa antes de ir al cine. Se da el tiempo que tarda en llegar a la casa de Alfred y el tiempo desde la casa de Alfred hasta el cine. Dado el minuto del día en que comienza la película, se pregunta a qué hora debe salir Stanley para no llegar tarde.

### Entrada
Tres líneas:
- Primer línea: duración en minutos para llegar a la casa de Alfred.
- Segunda línea: duración en minutos para ir de la casa de Alfred al cine.
- Tercer línea: minuto del día en que empieza la película.

### Salida
Un solo entero: el último minuto del día en el que Stanley puede comenzar a conducir para llegar a tiempo.

### Ejemplo
Entrada:
```
10
4
1335
```
Salida:
```
1321
```

***

## 2. FizzBuzz
**Puntos:** 3

### Introducción
Contar desde un número m hasta n con las siguientes condiciones del juego FizzBuzz:
- Múltiplos de 3: imprimir "Fizz"
- Múltiplos de 5: imprimir "Buzz"
- Múltiplos de 3 y 5: imprimir "FizzBuzz"

### Entrada
Dos líneas:
- Primera línea: m, número inicial.
- Segunda línea: n, número final.

### Salida
Impresión de números o palabras según las reglas.

### Ejemplo
Entrada:
```
1
5
```
Salida:
```
1
2
Fizz
4
Buzz
```

***

## 3. RoboCup Ball Position
**Puntos:** 3

# Introducción

Esta es una historia real. Todos los personajes descritos en esta historia han sido modificados para proteger su identidad.

En 2011, mientras participábamos en la competencia RoboCup de fútbol (una competencia de robots autónomos para jugar fútbol), desarrollamos cámaras estereoscópicas (es decir, dos cámaras) montadas en el techo que podían seguir la pelota y proporcionar las coordenadas 3D de la pelota (X, Y, Z). 

Solo había un problema: la posición se daba usando una de las cámaras como referencia, pero necesitábamos que el centro del campo fuera la referencia.

Por lo tanto, tomamos algunas mediciones:

- Cuando la pelota estaba en la posición (0, 0, 0) del campo, el sistema de cámaras estereoscópicas marcó (-0.378094, -0.044534, 3.54707).
- Cuando la pelota estaba en la posición (0, 0, 1) del campo, el sistema de cámaras estereoscópicas marcó (-0.460408, -0.74951, 2.91714).
- Cuando la pelota estaba en la posición (-1, 0, 0) del campo, el sistema de cámaras estereoscópicas marcó (0.427701, -0.555208, 3.98178).
- Cuando la pelota estaba en la posición (0, 1, 0) del campo, el sistema de cámaras estereoscópicas marcó (0.288779, 0.451449, 2.93639).
- Cuando la pelota estaba en la posición (1, 1, 0) del campo, el sistema de cámaras estereoscópicas marcó (-0.517016, 0.962123, 2.50168).
- Cuando la pelota estaba en la posición (1, 0, 0) del campo, el sistema de cámaras estereoscópicas marcó (-1.183889, 0.46614, 3.11236).
- Cuando la pelota estaba en la posición (-1, -1, 0) del campo, el sistema de cámaras estereoscópicas marcó (0.77, -0.208, 1.8878).
- Cuando la pelota estaba en la posición (1, -1, 1) del campo, el sistema de cámaras estereoscópicas marcó (1.111, 0.872364, -1.6786).

Estos valores son las mediciones reales, así que no esperes que los resultados sean números enteros redondeados.


### Entrada
Una línea: tres enteros separados por comas, entre -1 y 1.

### Salida
Si la posición corresponde a una de las posiciones conocidas, imprimir las coordenadas de la cámara con 6 decimales. Si no, imprimir: "INVALID POSITION".

### Ejemplo 1
Entrada:
```
0,0,1
```
Salida:
```
-0.460408,-0.749510,2.917140
```

### Ejemplo 2
Entrada:
```
0,1,0
```
Salida:
```
0.288779,0.451449,2.936390
```

### Ejemplo 3
Entrada:
```
-1,0,1
```
Salida:
```
INVALID POSITION
```

***

## 4. DAC Conversion
**Puntos:** 4

### Introducción
Un convertidor digital a analógico (DAC) de 10 bits convierte un valor decimal (0 a 1023) en un voltaje analógico (0 a 5 V). Se quiere hacer un programa que reciba el valor decimal y devuelva el voltaje analógico correspondiente con dos decimales.

### Entrada
Un entero positivo (valor digital).

### Salida
El voltaje analógico correspondiente seguido de " V".

### Ejemplo
Entrada:
```
356
```
Salida:
```
1.74 V
```


***

## 5. Recover Information
**Puntos:** 4

### Introducción
Recuperar datos de un disco RAID a partir de la información redundante con operación NAND entre dos cadenas binarias (contenido de disco 1 y disco 2).

La NAND está definida así:
- 0 NAND 0 = 1
- 0 NAND 1 = 1
- 1 NAND 0 = 1
- 1 NAND 1 = 0

### Entrada
Dos líneas binarias de igual longitud.

### Salida
Una línea binaria resultado de la operación NAND bit a bit.

### Ejemplo
Entrada:
```
11001
10110
```
Salida:
```
01111
```


***

## 6. Climbing And Descending
**Puntos:** 4

### Introducción
Dado un recorrido representado por una secuencia de números, determinar si primero aumenta estrictamente y luego disminuye estrictamente (simula subir y bajar una montaña).

### Entrada
- Primera línea: entero N, número de elementos.
- Siguientes N líneas: cada una un entero positivo, los elementos de la secuencia.

### Salida
"True" si cumple patrón subir y bajar, "False" en caso contrario.

### Ejemplo
Entrada:
```
6
1
3
4
12
10
9
```
Salida:
```
True
```


## 7. The Easter Bunny Problem
**Puntos:** 4

### Introducción
Determinar si un número dado de huevos puede formar un triángulo perfecto, es decir, si es un número triangular.

### Entrada
- Primera línea: entero T, cantidad de casos.
- Siguientes T líneas: número N de huevos.

### Salida
Imprimir "YES" si es un número triangular, "NO" en caso contrario.

### Ejemplo
Entrada:
```
3
6
10
7
```
Salida:
```
YES
YES
NO
```

***

## 8. Happy Pi Day
**Puntos:** 4

### Introducción
Dada una secuencia numérica de hasta 10 dígitos, buscar su posición en los primeros 100 decimales de Pi y devolver la posición de la primera ocurrencia o -1 si no se encuentra.

### Entrada
Un número entero de hasta 10 dígitos.

### Salida
Posición de la primera aparición en Pi o -1 si no se encuentra.

### Ejemplo
Entrada:
```
14159
```
Salida:
```
1
```

***

## 9. La Barbacoa
**Puntos:** 4

### Introducción
Dada una parrilla con varias brochetas representadas por líneas, contar cuántas brochetas son vegetarianas (solo 'o') y cuántas no (contienen al menos una 'x').

### Entrada
Varias líneas hasta encontrar una línea con '#', cada línea representa una brocheta.

### Salida
Dos enteros: número de brochetas vegetarianas y número de no vegetarianas.

### Ejemplo
Entrada:
```
--xo--x--ox--
--xx--x--xx--
--oo--o--oo--
--xx--x--ox--
--xx--x--ox--
#
```
Salida:
```
1 4
```


***

## 10. Compound interest calculator
**Puntos:** 5

### Introducción
Calcular el dinero final que se tendrá tras invertir 1000 € a un interés compuesto dado un interés anual y número de años.

### Entrada
- Primera línea: interés anual en porcentaje (entero).
- Segunda línea: número de años (entero).

### Salida
Dinero final con dos decimales.

### Ejemplo
Entrada:
```
5
15
```
Salida:
```
2078.93
```


[1](https://codewarsbcn.hpcloud.hp.com/app/uploads/2023/12/Valencia2025.pdf)
