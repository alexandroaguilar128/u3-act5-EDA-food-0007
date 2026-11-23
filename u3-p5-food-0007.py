import pandas as pd
import matplotlib.pyplot as plt
# Alexandro Aguilar NC 0007
# 1. Leer el archivo CSV 
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV comida india 0007 ---")
print(df_food_india)
print("\n--- Mostrar nombre comida + ingredientes 0007 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- tiempo de cocinado, mostrar 10 registros con head 0007 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)
print("\n--- Grafica comida (X), tiempo de cocinado (Y)---")
print("\n--- Grafica comida (X) texto a 30 grados ---")
nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title('Comida tipica de India Alexandro 0007')
plt.xlabel('Nombre_platillo')
plt.ylabel('Tiempo de cocinado')
plt.show()
print("Grafica de varias columnas Alexandro NC 0007")
nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora.plot.bar(x='name', rot=30)
plt.title('Grafica de varias columnas Alexandro 0007')
plt.xlabel('Nombre_platillo')
plt.ylabel('Tiempo de cocinado prep y comida')
plt.show()
print("\n--- Graficas aplicadas una tras otra verticalmente 0007")
nombre_y_hora.plot.bar(x='name', stacked=True)
plt.title('Graficas apiladas Alexandro 0007')
plt.xlabel('Nombre_platillo')
plt.ylabel('Tiempo de cocinado prep y comida')
plt.show()


