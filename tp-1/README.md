# Torres de Hanoi

![as](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif/250px-Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif)



## Grupo

Este trabajo practico fue realizado por:

- Roberto Catalan
- Lautaro Galende
- Lucas Dell’Isola

## Juego

Las Torres de Hanoi es un juego lógico matemático, que consiste en la apilación de 2, 3, 4, 5, o más discos en una de las tres estacas que se ubican de manera  vertical sobre un tablero. El objetivo del juego consiste en trasladar los discos de la primera a la tercera estaca.

## Instrucciones

### Instalación

Para poder instalar y correr esta aplicación se necesitan tener instalados previamente:

- Python 3

Luego, debemos clonar el repositorio de GitHub:

```bash
$ git clone https://github.com/rcatalan98/sia-tp.git
```

Navegamos a la carpeta del TP 1:

```bash
$ cd sia-tp/tp-1
```

Instalamos las dependencias:

```bash
$ pip3 install -r requirements.txt
```

### Ejecución

Para ejecutar el programa, simplemente tenemos que correr el siguiente comando:

```bash
$ python3 main.py PATH_TO_CONFIG.json
```

Donde `PATH_TO_CONFIG.json` indica donde esta guardada la configuración indicada. Esta configuración es un archivo json con los siguientes campos:

```json
{
  "algorithm": "GlobalHeuristic", // Indica el algoritmo a usar
  "heuristics":"DiscsOnTheLastTower", // Indica la heuristica a usar. Si el algoritmo no require heuristica, este valor es ignorado
  "discs": 7, // La cantidad de discos a usar
  "BPPV_config": { // Configuracion especifica del algoritmo BPPV
    "max_depth": 130,  // Estimacion sobre la profundidad maxima
    "depth_modifier": 0.5 // Modificador de profundidad maxima, en este caso aumenta un 50% la maxima profundidad.
  },
  "print_to": "console" // Define si el resultado se guarda a la consola o a un archivo.
}
```

Los algoritmos a elegir son:

- `AStar`: Requiere una heuristica.
- `GlobalHeuristic`: Requiere una heuristica.
- `LocalHeuristic`: Requiere una heurística
- `BPA`: No require heuristicas ni parámetros adicionales
- `BPP`: No requiere heuristicas ni parámetros adicionales
- `BPPV`: No requiere heurísticas, pero requiere de unos parámetros adicionales.

Por otro lado, las heurísticas disponibles son:

- `DiscsOnTheLastTower`
- `AdmissibleEstimatedPossibleMovements`
- `EstimatedPossibleMovements`

En la carpeta `./config/` hay ejemplos de archivos de configuración para todos los algoritmos y heurísticas.