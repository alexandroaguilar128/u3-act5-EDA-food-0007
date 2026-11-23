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
