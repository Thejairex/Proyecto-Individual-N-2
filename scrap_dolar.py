from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import pandas as pd
import numpy as np



ingresos = pd.read_csv("Datasets/Ingresos.csv")
rango = ingresos.shape[0]
# lista = np.zeros(rango)
lista = []

for x in range(rango):
    lista.append(x)

ingresos["Dolar"] = lista

print(ingresos)