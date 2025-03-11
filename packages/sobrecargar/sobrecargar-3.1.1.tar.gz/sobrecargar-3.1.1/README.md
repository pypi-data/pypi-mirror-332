

# Sobrecargar

[![Hecho por Chaska](https://img.shields.io/badge/hecho_por-Ch'aska-303030.svg)](https://cajadeideas.ar)
[![Versión: 3.1.01](https://img.shields.io/badge/version-v3.1.1-green.svg)](https://github.com/hernanatn/github.com/hernanatn/sobrecargar.py/releases/latest)
[![Verisón de Python: 3.12](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/downloads/release/python-3120/)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-lightgrey.svg)](LICENSE)


## Descripción
`sobrecargar` es un módulo de Python que incluye una única clase homonima, la cual provee la implementación de un @decorador universal, que permite definir múltiples versiones de una función o método con diferentes conjuntos de parámetros y tipos. Esto permite crear una sobrecarga de funciones similar a la que se encuentra en otros lenguajes de programación, como C++.

## Instalación
Puede decargar e instalar `sobrecargar` utilizando el manejador de paquetes `PIP`, según se indica a continuación:

**Ejecute** el siguiente comando en la `terminal`:

``` Bash
pip install sobrecargar
``` 

## Uso Básico
### Decorar una función:
Se puede emplear tanto `@sobrecargar` como `@overload` para decorar funciones o métodos.

```python
from sobrecargar import sobrecargar

@sobrecargar
def mi_funcion(parametro1: int, parametro2: str):
    # Código de la primera versión de la función
    ...

@sobrecargar
def mi_funcion(parametro1: float):
    # Código de la segunda versión de la función
    ...
```

### Decorar un método de una clase:
> [!TIP]  
> Desde la versión 3.0.2 los métodos (funciones miembro) se *sobrecargan* de la misma forma que las "funciones libres".

```python
from sobrecargar import sobrecargar # 'ovearload' es un alias pre-definido para 'sobrecargar'

class MiClase:
    @sobrecargar
    def mi_metodo(self, parametro1: int, parametro2: str):
        # Código de la primera versión del método
        ...

    @sobrecargar
    def mi_metodo(self, parametro1: float):
        # Código de la segunda versión del método
        ...
```

## Ejemplo de Uso
### Función 'libre'
```python
@sobrecargar
def suma(a: int, b: int):
    return a + b

@sobrecargar
def suma(a: list[int]):
    return sum([x for x in a])

resultado1 = suma(1, 2)  # Llama a la primera versión de la función suma, con parámetros a y b : int
>> 3

resultado2 = suma([1,2,3,4,5])  # Llama a la segunda versión de la función suma, con parámetro a : List[int]
>> 15
```

## Configuración
El decorador `@sobrecargar` acepta configuraciones por parámetro, proveyendo valores razonables por defecto.

> [!TIP]  
> Desde la versión 3.1.0

<table>
<thead> <th>Parámetro</th><th>Funcionalidad</th><th>Valor por defecto</th><th>Versión</th></thead>
<tbody>
        <tr><td>cache</td><td>Si <code>cache</code> es <code>True</code> se intenta utilizar la función correspondiente a los tipos provistos guardada en caché, si no existe, se corre la estrategia de resolución de candidatos y se guarda en caché para usos subsiguientes. El caché es sensible no soo a los tipos de los parámetros, sino también al orden en que fueran provistos.</td><td><code>False</code></td><td>3.1.X</td></tr>
        <tr><td>debug</td><td>Si <code>debug</code> es <code>True</code> se imprimen a <code>stdin</code> mensajes de debug para: <ul> <li> registro de nueva sobrecarga;</li><li> llamada a la función;</li><li> caché (si hay); y</li><li> resolución de candidatos.</li></ul></td><td><code>False</code></td><td>3.1.X</td></tr>
</tbody>
</table>

El decorador puede seguir utilizandose sin necesidad de prover ningún parámetro ni utilizar `()`, se aplican valores por defecto.
> [!NOTE]
> Si cualquiera de las sobrecargas declara un parámetro de configuración, este se aplica a todas ellas.

### Ejemplo:
```python
        @sobrecargar(cache=True, debug=True)
        def funcion_cacheada_debugeada(a: float, *args : *tuple[int]):
            return a * sum(a for a in args)

        @sobrecargar # cache = True, debug = True / a pesar que no se indican explícitamente, porque ya existe una sobrecarga con cahcé y debug.
        def funcion_cacheada_debugeada(a: float, b: Union[float,int] ):
            return a * b    

```


---

**Nota**: Esta documentación es un resumen de alto nivel. Para obtener más detalles sobre la implementación y el uso avanzado, se recomienda consultar el código fuente, la documentación provista y realizar pruebas adicionales.

## [Documentación](/docs)
