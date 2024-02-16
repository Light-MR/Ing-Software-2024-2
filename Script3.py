import matplotlib
matplotlib.use('Qt5Agg')  # Cambiar el backend de Matplotlib a 'Qt5Agg'

import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return np.sin(x)

# Crear datos para graficar
x = np.linspace(0, 10, 100)
y = funcion(x)

# Personalizar el estilo de la gráfica
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(10, 6))

# Graficar la función con colores y marcadores personalizados
plt.plot(x, y, color='skyblue', linewidth=2, linestyle='-', label='Función seno')
plt.scatter(x, y, color='darkblue', s=30, label='Puntos de datos')

# Personalizar título y etiquetas de los ejes
plt.title('Gráfica de la función seno', fontsize=18)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

# Añadir leyenda
plt.legend(loc='upper right', fontsize=12)

# Añadir línea horizontal y vertical
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(np.pi, color='red', linewidth=0.5, linestyle='--', label='Línea vertical en π')

# Añadir texto
plt.text(3, 0.5, 'Punto de inflexión', fontsize=12, color='green')

# Añadir rejilla
plt.grid(True)

# Añadir límite de ejes
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Añadir flechas
plt.annotate('', xy=(np.pi/2, 1), xytext=(np.pi/2, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Añadir texto con flechas
plt.text(np.pi/2, 0.6, 'Máximo', fontsize=12)

# Mostrar la gráfica en una ventana emergente
plt.tight_layout()
plt.show()
