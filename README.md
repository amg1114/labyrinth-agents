# 👾 Pacman IA

Proyecto académico desarrollado para la asignatura **Introducción a la Inteligencia Artificial** en la **Universidad del Valle – Sede Tuluá**.  
Este proyecto implementa un entorno de juego tipo Pacman donde dos **agentes inteligentes** (René y Piggy) utilizan distintos **algoritmos de búsqueda** (informada y no informada) para alcanzar sus objetivos dentro de un laberinto.

---

## 🎯 Objetivo General

Desarrollar un programa en **Python** donde la rana **René (Agente 1)** encuentre a **Elmo**, mientras que **Piggy (Agente 2)** busca a René.

---

## 🧩 Objetivos Específicos

- Implementar un agente (René) que utilice **búsqueda en profundidad limitada** para encontrar a Elmo.  
- Implementar un agente (Piggy) que utilice **búsqueda A\*** y **búsqueda por amplitud (BFS)** para encontrar a René.  
- Desarrollar una **interfaz gráfica** donde se visualicen los movimientos de cada agente dentro del laberinto.

---

## 🧠 Fundamento Teórico

### 🔸 Agentes de Software
Son entidades autónomas que toman decisiones dentro de un entorno. En este proyecto, René y Piggy interactúan con su entorno (el laberinto) percibiendo estados y ejecutando acciones para cumplir sus objetivos.

### 🔸 Métodos de Búsqueda
Los algoritmos de búsqueda permiten que los agentes encuentren caminos desde un punto inicial hasta una meta.  
Se clasifican en:

- **Búsqueda no informada:** no tienen información sobre la distancia a la meta (ej. profundidad limitada, amplitud).  
- **Búsqueda informada:** utilizan una **heurística** para estimar el costo o distancia restante (ej. A\*).

---

## ⚙️ Metodología

El desarrollo se divide en tres módulos principales:

1. **Módulo gráfico:** construido con **Pygame**, renderiza el entorno y las animaciones.  
2. **Módulo de René:** implementa el algoritmo de **búsqueda por profundidad limitada**.  
3. **Módulo de Piggy:** implementa los algoritmos de **búsqueda por amplitud (BFS)** y **A\***.

### 🧩 Librerías utilizadas
- `pygame` → interfaz gráfica e interacción.  
- `collections` → manejo de colas y pilas.  
- `time` → control del tiempo de refresco en pantalla.  
- `abc` → clases abstractas y herencia.  

---

## 🕹️ Descripción del Juego

- El entorno es un **laberinto representado en una matriz (grid)**.  
- Los agentes se mueven en **cuatro direcciones cardinales** (arriba, abajo, izquierda, derecha).  
- Los obstáculos impiden el paso y deben ser evitados por los agentes.  
- Cada agente tiene un **objetivo**:
  - René busca a Elmo 🐸➡️🧡  
  - Piggy busca a René 🐷➡️🐸  

### Condiciones de finalización:
- René encuentra a Elmo.  
- Piggy alcanza a René.  
- Los agentes quedan bloqueados sin ruta posible.

---

## 💡 Algoritmos Implementados

### 🐸 René – Búsqueda en Profundidad Limitada
- Explora caminos sucesivamente hasta alcanzar un límite máximo de profundidad.  
- Usa una pila (stack) para manejar los nodos por expandir.  
- Construye la ruta desde el nodo objetivo hasta el nodo raíz.

### 🐷 Piggy – Búsqueda A\* y BFS
- **A\* (A Star):** utiliza la **heurística Manhattan** para estimar el costo hacia la meta.  
  \\( f(n) = g(n) + h(n) \\)  
- **BFS (Breadth-First Search):** expande los nodos más cercanos al inicio garantizando el camino más corto.  
- Piggy alterna entre ambos métodos (40% A\*, 60% BFS) en cada movimiento.  

---

## 💻 Estructura del Proyecto

```
proyecto-intro-ia/
├─ classes/                 # Clases principales (Agente, Laberinto, Nodo)
├─ constants/               # Laberintos predefinidos
├─ search/                  # Algoritmos de búsqueda (A*, BFS, Profundidad)
├─ images/                  # Recursos gráficos (fondos, sprites, resultados)
├─ index.py                 # Punto de entrada del programa
├─ Pacman-IA-informe.pdf    # Documento explicativo del proyecto
└─ enunciado.pdf            # Enunciado del trabajo
```

---

## 🚀 Ejecución del Proyecto

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/proyecto-intro-ia.git
cd proyecto-intro-ia
```

### 2️⃣ Instalar dependencias
```bash
pip install pygame
```

### 3️⃣ Ejecutar el juego
```bash
python index.py
```

---

## 🧩 Escenarios del Juego

- **Escenario A:** Laberinto del enunciado. René encuentra a Elmo.  
- **Escenario B:** René siempre alcanza a Elmo.  
- **Escenario C:** Piggy alcanza a René usando A\* o BFS.  
- **Escenario D:** Ambos agentes quedan atrapados sin lograr su objetivo.  

---

## 👨‍💻 Autores

- **Andrés Felipe Cabal Correa** – 2160339  
- **Daniel José Cuestas Parada** – 2067550  
- **Johan Alejandro Moreno Gil** – 2160052  

**Facultad de Ingeniería – Universidad del Valle**  
**Docente:** Mtr. Joshua David Triana Madrid  
**Octubre 2024**

---

## 📚 Referencias

- Reina, M. (2011). *Algoritmo de búsqueda A\* (PathFinding A\*) – XNA*. Escarbando Código.  
  [https://escarbandocodigo.wordpress.com/2011/07/11/1051/](https://escarbandocodigo.wordpress.com/2011/07/11/1051/)

- *Métodos de Búsqueda IA*. (n.d.).  
  [https://inteligenciaartificialgrupo33.blogspot.com/p/metodos-de-busqueda-y-ejemplos.html](https://inteligenciaartificialgrupo33.blogspot.com/p/metodos-de-busqueda-y-ejemplos.html)

- *Agentes de Software* – Oficina de Transferencia de Resultados de Investigación (UCM).  
  [https://www.ucm.es/otri/complutransfer-agentes-software](https://www.ucm.es/otri/complutransfer-agentes-software)

---

## 🧾 Licencia

Este proyecto se desarrolló con fines académicos.  
Puedes usar el código con propósitos educativos citando a los autores originales.
