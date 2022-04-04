# TP: Algoritmos Genéticos

## Grupo

Este trabajo practico fue realizado por:

- Roberto Catalan
- Lautaro Galende
- Lucas Dell’Isola

## Instalación

Para poder instalar y correr esta aplicación se necesitan tener instalados previamente:

- Python 3

Luego, debemos clonar el repositorio de GitHub:

```bash
$ git clone https://github.com/rcatalan98/sia-tp.git
```

Navegamos a la carpeta del TP 2:

```bash
$ cd sia-tp/tp-2
```

Instalamos las dependencias:

```bash
$ pip3 install -r requirements.txt
```

## Ejecución

Hay distintos modos de ejecución de este programa:

- Si quereremos correr una sola ronda de un único config, podemos llamar al siguiente comando:

  ```bash
  $ python3 main.py bag.txt config.json
  ```

- Si queremos ejecutar el mismo comando que el anterior, pero que se ejecute 5 veces, simplemente le podemos agregar la cantidad de ejecuciones al final:

  ```bash
  $ python3 main.py bag.txt config.json 5
  ```

- Si queremos ejecutar varias configuraciones al mismo tiempo, tenemos que agregar la palabra ‘multiple’:

  ```bash
  $ python3 main.py bag.txt multiple /path/to/config/directory
  ```

- Y, de forma similar, si queremos que ademas cada config se ejecute 5 veces, podemos pasarle la cantidad de ejecuciones en el ultimo parámetro:

  ```bash
  $ python3 main.py bag.txt multiple /path/to/config/directory 5
  ```

Estos comandos van a generar un archivo `result.csv` donde se va a encontrar toda la información sobre todos los configs ingresados.

## Configuración

Este programa soporta una gran variedad de algoritmos de selección, corte y reproducción, ademas de aceptar parámetros como el tamaño de la población y las probabilidad de mutar que tiene cada bit de la mochila.

Esta configuración se le indica al programa mediante dos archivos:

- `config.json`: Este archivo contiene la información sobre los algoritmos usados y la gran mayoría de los parámetros, pero no tiene información sobre el problema en si.
- `mochila.txt`: Este archivo contiene la informacion sobre el problema en si, asignando la cantidad maxima de items que entran en la mochila y el peso máximo de la misma en la primer linea, separados por un espacio. Luego, las siguientes lineas indican el peso y el beneficio de cada item, también separado por un espacio.

El archivo `config.json` se ve de la siguiente forma:

```json
{
  "breeding": "breeder_algorithm",
  "breeding_arguments": {},
  "selection": "selection_algorithm",
  "selection_arguments": {},
  "stop_condition": "stop_condition",
  "stop_condition_config": {},
  "population_size": 500,
  "mutation_rate": 0.01
}
```

El valor de `population_size` fue elegido a mano, mas que nada teniendo en cuenta el tiempo que tarda en generar cada generación nueva. Vimos que la velocidad de conversión no cambiaba mucho entre los tamaños de generación 100 y 1000, por lo que decidimos optar por 500.

En el caso de `mutation_rate`, probamos valores desde 0.1 hasta 0.01. Cuando mayor era este valor, menos estable eran los resultados, por lo que encontramos un buen balance utilizando el valor 0.01. 

### Mecanismos de Reproducción

Se han implementado 3 mecanismos de reproducción, siendo uno de estos un caso especial de otro:

- **MultipleBreeder**: Este mecanismo realiza varios puntos de corten en los padres para poder dividirlo entre los hijos. PAra poder ejecutarlo se deben pasar argumentos indicando la cantidad de puntos de corte:

  ```json
  {
    "breeding": "MultipleBreeder",
    "breeding_arguments": {
      "crossing_points": 3
    }
  }
  ```

  Según nuestros resultados, dependiendo de que tan grande sea el espacio de la población inicial, se pueden dar dos resultado opuestos.

  Si el espacio de la población inicial es relativamente chico, por ejemplo en la mochila solo pueden tener 10 items, tener una cantidad de puntos de corte mayor lleva a que la solución converja de forma mas rápida, pudiendo escapar de mejor forma de los mínimos locales.

  Por el otro lado, si el espacio inicial el grande (pueden entrar hasta 100 elementos en la mochila), tener un numero alto de puntos de corte suele llevar a que la aptitud general de la población caiga a 0 rápidamente.

  Por estas pruebas, creemos que un valor mas alto de puntos de corte tiende a generar mas aleatoriedad y desviar al algoritmo a la creación de sujetos que son menos aptos (o directamente no validos).

- **SimpleBreeder**: Este mecanismo es un caso particular del anterior, donde solo se elige un punto de corte. No hay parámetros para poder variar.

  ```json
  {
    "breeding": "SimpleBreeder",
    "breeding_arguments": {}
  }
  ```

- **UniformBreeder**: Este mecanismo funciona de dorma distinta, ya que por cada elemento de las mochilas padres, los hijos pueden tener un 50% de chances de obtener el elemento de su padre o de su madre, mientras que el otro hijo va a recibir el elemento opuesto.

  ```json
  {
    "breeding": "UniformBreeder",
    "breeding_arguments": {}
  }
  ```

### Mecanismos de Selección

Se implementaron 6 métodos de selección:

- **BoltzmannSelection**: INVESTIGAR Y COMPLETAR

- **EliteSelection**: Este metodo de selección prioriza siempre los elementos con mejor aptitud y no tiene parámetros para optimizar. Suele caer rápidamente en máximos locales.

  ```json
  {
    "selection": "EliteSelection",
    "selection_arguments": {},
  }
  ```

- **RankSelection**: Este metodo de selección tampoco tiene parámetros a optimizar. Intenta de suavizar la selección de los individuos.

  ```json
  {
    "selection": "RankSelection",
    "selection_arguments": {},  
  }
  ```

- **RouletteSelection**: Este metodo no tiene parámetros para optimizar, y se basa en el concepto de jugar a la ruleta, donde cada sujeto tiene una probabilidad directamente relacionada a su aptitud de ser seleccionado.

  ```json
  {
    "selection": "RoulettteSelection",
    "selection_arguments": {},
  }
  ```

- **TournamentSelection**: El metodo de selección de torneos busca darle un poco de aleatoriedad a la selección de los sujetos. Funciona de la siguiente forma: primero elijo dos parejas de elementos, por cada pareja, saco un numero aleatorio, si este numero esta debajo de un threshold determinado, el sujeto con mejor fitness pasa a la próxima prueba, sino pasa el que tienen peor fitness. Por ultimo, realizo el mismo proceso con los dos ganadores, para obtener al el sujeto a persistir.

  ```json
  {
    "selection": "TournamentSelection",
    "selection_arguments": {
      "threshold": 0.85
    },
  }
  ```

  Para obtener este valor del threshold estuvimos probando con distintos valores, y descubrimos que si el numero es menor a 0.7 va a tender a tener siempre una peor fitness. Sospechamos que esto es un caso similar a lo explicado en el metodo de reproducción MultipleBreeder.

  Si elevamos el numero todavia mas cerca de 1, como puede ser 0.95 o 0.99, nuestro algoritmo suele llegar mas rápido a un máximo local, pero se estancan ahi, ya que no tienen tanta variación.

- **TruncatedSelection**: Este metodo descarta los peores k sujetos antes de seleccionar de forma aleatoria entre el resto de los sujetos. Este metodo puede ser optimizado con el parámetro k:

  INVESTIAGR Y COMPLETAR

  ```json
  {
    "selection": "TournamentSelection",
    "selection_arguments": {
      "k": ?????
    },
  }
  ```

### Metodos de Corte

Los métodos de corte indican cuando debería dejar de calcularse las generaciones basados en un parámetro “lo suficientemente bueno”. Implementamos las siguientes condiciones de corte:

- **acceptable solution**: Va a parar la ejecución una vez que se haya llegado a un valor mas o menos buenos estimado por el usuario. Este valor puede ser inalcanzable si el usuario realiza una mala estimación, por lo que ademas tiene un failsafe para que no se ejecute por mas de 500 segundos.

  ```json
  {
    "stop_condition": "acceptable solution",
     "stop_condition_config": {
       "acceptable_benefit": 9000
    }
  }
  ```

  Para este caso, sabemos que la solución optima esta alrededor de los 9000 puntos de aptitud, por lo que seleccionamos a ese valor.

- **generation count**: Esta condición de corte permite que el algoritmo corra por una cantidad fija de generaciones. En nuestro caso consideramos que 500 generaciones son suficientes para llegar a un puntaje aceptable.

  ```json
  {
    "stop_condition": "generation count",
     "stop_condition_config": {
       "max_generation": 500
    }
  }
  ```

- **same best fitness**: Esta condición va a interrumpir la ejecución cuando por una cantidad arbitraria de generaciones, se obtenga siempre la mejor aptitud.

  ```json
  {
    "stop_condition": "same best fitness",
     "stop_condition_config": {
       "generations_with_same_fitness": 40
    }
  }
  ```

  Este valor fue un poco complicado de optimizar, ya que hay que encontrar un punto medio. Si este valor es muy bajo, el algoritmo va a terminar de forma prematura en un mínimo local, pero si este numero es muy alto, va a tardar bastante mas tiempo en finalizar la ejecución.

  Para nuestros fines, consideramos que con 40 generaciones se obtiene un buen balance.

- **similar structure**: Este metodo es similar al anterior, pero en vez de tomar el valor anterior, lo que hace es tratar de interpretar cuando la mediana del fitness de una generación es similar a las ultimas n medianas. Para hacer esto ofrecemos dos parámetros, el porcentaje de similaridad y la cantidad de generaciones a considerar.

  ```json
  {
    "stop_condition": "similar structure",
     "stop_condition_config": {
        "similarity_percentage": 0.95,
        "number_of_similar_generations": 30
     }
  }
  ```

  Estos parámetros tienen las mismas complicaciones que los del metodo anterior, solo que son todavía mas sensibles.

- **time**: También se puede ejecutar al algoritmos por un tiempo determinado, sin importar la cantidad de generaciones. En nuestro caso, para optimizar el tiempo que tardan en correr, consideramos que solo hace falta ejecutarlo por 60 segundos, ya que suele converger a un buen puntaje en 30/40 segundos.

  ```json
  {
    "stop_condition": "time",
    "stop_condition_config": {
        "runtime_in_seconds": 60
    }
  }
  ```

  















