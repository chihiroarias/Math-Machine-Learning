{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8d1092f5",
   "metadata": {},
   "source": [
    "# Verificación de Entorno\n",
    "## Matemática para el Aprendizaje Automático\n",
    "\n",
    "Este cuaderno verifica que su entorno esté correctamente configurado.\n",
    "\n",
    "Instrucciones:\n",
    "1. Ejecutar todas las celdas. (Botón de Run All/Ejecutar Todo)\n",
    "2. Si aparece un error, revisar la instalación.\n",
    "3. Si todo funciona correctamente, al final verá el mensaje:\n",
    "\n",
    "**ENTORNO CONFIGURADO CORRECTAMENTE ✅**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e823c8cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "\n",
    "print(\"Versión de Python detectada:\", sys.version)\n",
    "\n",
    "major, minor = sys.version_info[:2]\n",
    "\n",
    "assert major == 3 and minor >= 8, \"Se requiere Python 3.8 o superior.\"\n",
    "\n",
    "print(\"✔ Versión de Python válida\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9cea59e",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    import numpy as np\n",
    "    print(\"✔ NumPy importado correctamente - versión:\", np.__version__)\n",
    "except Exception as e:\n",
    "    raise ImportError(\"Error al importar NumPy\") from e\n",
    "\n",
    "try:\n",
    "    import scipy as sp\n",
    "    print(\"✔ SciPy importado correctamente - versión:\", sp.__version__)\n",
    "except Exception as e:\n",
    "    raise ImportError(\"Error al importar SciPy\") from e\n",
    "\n",
    "try:\n",
    "    import matplotlib.pyplot as plt\n",
    "    print(\"✔ Matplotlib importado correctamente\")\n",
    "except Exception as e:\n",
    "    raise ImportError(\"Error al importar Matplotlib\") from e\n",
    "\n",
    "try:\n",
    "    import pandas as pd\n",
    "    print(\"✔ Pandas importado correctamente - versión:\", pd.__version__)\n",
    "except Exception as e:\n",
    "    raise ImportError(\"Error al importar Pandas\") from e"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "707fc313",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crear una matriz\n",
    "A = np.array([[1, 2],\n",
    "              [3, 4]])\n",
    "\n",
    "# Calcular determinante\n",
    "det = np.linalg.det(A)\n",
    "\n",
    "print(\"Matriz A:\")\n",
    "print(A)\n",
    "print(\"\\nDeterminante de A:\", det)\n",
    "\n",
    "assert np.isclose(det, -2.0), \"Error en operaciones matriciales.\"\n",
    "\n",
    "print(\"✔ Operaciones matriciales funcionando correctamente\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f056762",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.linalg import inv\n",
    "\n",
    "A_inv = inv(A)\n",
    "\n",
    "print(\"Inversa de A:\")\n",
    "print(A_inv)\n",
    "\n",
    "print(\"✔ SciPy funcionando correctamente\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0166ad75",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.linspace(0, 2*np.pi, 100)\n",
    "y = np.sin(x)\n",
    "\n",
    "plt.figure()\n",
    "plt.plot(x, y)\n",
    "plt.title(\"Gráfico de prueba: sin(x)\")\n",
    "plt.xlabel(\"x\")\n",
    "plt.ylabel(\"sin(x)\")\n",
    "plt.show()\n",
    "\n",
    "print(\"✔ Gráfico generado correctamente\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ffc31c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"=======================================\")\n",
    "print(\"ENTORNO CONFIGURADO CORRECTAMENTE ✅\")\n",
    "print(\"Está listo/a para comenzar el curso.\")\n",
    "print(\"=======================================\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}