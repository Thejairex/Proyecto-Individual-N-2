import pandas as pd

# Ejemplo de DataFrame
data = {
    'Año': ['2020*', '2021*', '2022', '2023*', '2024']
}
tecnologia = pd.DataFrame(data)

# Eliminar asteriscos utilizando str.replace
tecnologia["Año"] = tecnologia["Año"].str.replace("*", "")
tecnologia["Año"].astype(int)
print(tecnologia)
