import matplotlib.pyplot as plt
import numpy as np

# Datos
data = np.random.randn(1000)

# Crear el histograma
plt.hist(data, bins=10, edgecolor='black')

# Agregar título y etiquetas
plt.title('Histograma ')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()