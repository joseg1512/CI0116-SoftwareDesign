## Sistema de Gestión de Biblioteca

### Problemas

#### 1. Violación del Principio de Responsabilidad Única

- La clase `Libro` mezcla datos del libro con impresión en pantalla (`imprimir_datos()`)
- La clase `Biblioteca` mezcla la lógica de la biblioteca con la lógica de interfaz de usuario en `agregarLibro()` al solicitar un `input()` del usuario.

#### 2. No es extensible. Viola el principio Open-Closed

- El método `calcular_popularidad()` tiene valores explícitos dentro, lo que lo hace poco escalable.
- Para agregar un nuevo género se debe modificar el método existente.

#### 3. Condicionales innecesarios

- El método `es_antiguo()` usa if-else cuando puede retornar directamente la comparación, esto es muy verbosos innecesariamente.

#### 4. Variables no significativas

- En `agregar_libro()` y `generar_reporte()` se usa declara la variable `l`, que es poco descriptivo.
#### 5. Falta de Validaciones

- No valida géneros válidos
- No maneja errores de entrada del usuario
- Variables con nombres poco descriptivos (`l` en lugar de `libro`)

---

## Código Refactorizado

### libro.py

```python
class Libro:
    # constantes
    GENEROS_VALIDOS = ['novela', 'ciencia', 'historia']
    CONFIGURACION_POPULARIDAD = {
        'novela': {'base': 50, 'divisor': 10},
        'ciencia': {'base': 70, 'divisor': 5},
        'historia': {'base': 40, 'divisor': 8}
    }
    
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = self._validar_genero(genero)
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible
    
    def _validar_genero(self, genero):
        genero = genero.lower()
        if genero not in self.GENEROS_VALIDOS:
            raise ValueError(f"Género '{genero}' no válido")
        return genero
    
    def calcular_popularidad(self):
        config = self.CONFIGURACION_POPULARIDAD.get(self.genero)
        if config:
            return config['base'] + (self.paginas / config['divisor'])
        else:
            return 10
    
    def es_antiguo(self):
        return self.anio_publicacion < 1980
        
    # retorna los datos en un diccionario en vez de imprimirlos en consola
    def obtener_datos(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'paginas': self.paginas,
            'anio': self.anio_publicacion,
            'disponible': self.disponible,
            'popularidad': self.calcular_popularidad(),
            'es_antiguo': self.es_antiguo()
        }
```

### biblioteca.py

```python
from libro import Libro

class Biblioteca:
    
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, titulo, autor, genero, paginas, anio):
        try:
            libro = Libro(titulo, autor, genero, paginas, anio)
            self.libros.append(libro)
            return True
        except ValueError as e:
            print(f"Error al crear el libro: {e}")
            return False
            
    # calcula estadisticas pero no interactua con usuario directamente
    def calcular_estadisticas(self):
        total = len(self.libros)
        if total == 0:
            return {
                'total': 0,
                'disponibles': 0,
                'antiguos': 0,
                'promedio_popularidad': 0
            }
        antiguos = sum(1 for libro in self.libros if libro.es_antiguo())
        disponibles = sum(1 for libro in self.libros if libro.disponible)
        popularidad_total = sum(libro.calcular_popularidad() for libro in   
        self.libros)
        
        return {
            'total': total,
            'disponibles': disponibles,
            'antiguos': antiguos,
            'promedio_popularidad': popularidad_total / total
        }
        return reporte

```

### interfazBiblioteca.py

```python
# clase aparte para manejar interfaz de usuario
from biblioteca import Biblioteca
class InterfazBiblioteca:
    
    def __init__(self):
        self.biblioteca = Biblioteca()
    
    def generar_reporte(self):
        """Genera y muestra el reporte de la biblioteca"""
        libros = self.biblioteca.obtener_todos_los_libros()
        
        # imprime las estadisticas usando el metodo de la clase Biblioteca
        stats = self.biblioteca.calcular_estadisticas()
        print("\nREPORTE BIBLIOTECA:")
        print(f"Total libros: {stats['total']}")
        print(f"Disponibles: {stats['disponibles']}")
        print(f"Antiguos: {stats['antiguos']}")
        print(f"Promedio de popularidad: {stats['promedio_popularidad']:.2f}")
        
	def imprimir_datos_libro(self, libro):
		#imprime los datos del libro usando el metodo de la clase Libro
        datos = libro.obtener_datos()
        print(f"Título: {datos['titulo']}")
        print(f"Autor: {datos['autor']}")
        print(f"Género: {datos['genero']}")
        print(f"Páginas: {datos['paginas']}")
        print(f"Año: {datos['anio']}")
        print(f"Disponible: {'Sí' if datos['disponible'] else 'No'}")
        print(f"Popularidad: {datos['popularidad']:.2f}")
        print(f"Es antiguo: {'Sí' if datos['es_antiguo'] else 'No'}")
    
```

---

## 3 Mejoras Significativas

### 1. Separación de Responsabilidades - Principio de Responsabilidad Única

La clase `Libro` mezclaba el manejo de datos con impresiones al usuario en `imprimir_datos()`, lo que hacía que tuviera dos responsabilidades. Por otro lado, la clase `Biblioteca` mezclaba lógica su lógica interna parar agregar libros con interfaz de usuario al solicitar un `input`.

**Mejora:** 
+ Ahora cada clase tiene una responsabilidad específica: `Libro` maneja y provee datos estructurados con el método `obtener_datos()` y la parte de impresión se delega a una clasae de interfaz. 
+ La biblioteca maneja la lógica para agregar libros recibiendo las características como parámetros, sin recibir inputs del usuario.
### 2. Modularización de `calcular_popularidad()` 

El método `calcular_popularidad()` tenía valores explícitos que se evaluaban usando múltiples if-elif.

**Mejora:** 
+ La refactorización de `calcular_popularidad()` elimina esos valores explícitos y los condicionales gracias al uso de un diccionario. Cada género tiene su configuración definida, lo que reduce el código duplicado y mejora la escalabilidad.
+ Para agregar un nuevo género solamente se debe añadir una entrada al diccionario.
### 3. Validación y Manejo de Errores

En el código no había validación de géneros ni manejo de errores de entrada del usuario.

**Mejora:**
- Se agregó validación de errores para garantizar la consistencia de los datos ingresados y evitar fallos.  Con el método `_validar_genero()` únicamente se aceptan géneros definidos en  `GENEROS_VALIDOS` para asegurar que solo se usen opciones correctas.
- Se usan bloques `try` y `except` para evitar que el programa se termine si detecta valores incorrectos a la hora de crear un libro.