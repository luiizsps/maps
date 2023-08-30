import geopandas as gpd
import matplotlib.pyplot as plt

# carrega o arquivo shapefile dos estados brasileiros
br_states = gpd.read_file('C:/Users/japs1/Downloads/estados_2010.shp') 

# Informações numéricas fictícias associadas a cada estado
data = {
    'Acre': 100,
    'Alagoas': 50,
    'Amapá': 75,
    'Amazonas': 30,
    'Bahia': 60,
    'Ceará': 40,
    'Distrito Federal': 20,
    'Espírito Santo': 10,
    'Goiás': 5,
    'Maranhão': 55,
    'Mato Grosso': 45,
    'Mato Grosso do Sul': 25,
    'Minas Gerais': 15,
    'Pará': 35,
    'Paraíba': 65,
    'Paraná': 70,
    'Pernambuco': 80,
    'Piauí': 90,
    'Rio de Janeiro': 85,
    'Rio Grande do Norte': 75,
    'Rio Grande do Sul': 30,
    'Rondônia': 10,
    'Roraima': 50,
    'Santa Catarina': 20,
    'São Paulo': 60,
    'Sergipe': 40,
    'Tocantins': 70
}

# adiciona as informações ao dataframe dos estados
br_states['data'] = br_states['nome'].map(data) 

# plota o mapa
fig, ax = plt.subplots(1, 1, figsize=(14, 8))
br_states.boundary.plot(ax=ax)
br_states.plot(column='data', cmap='Blues', linewidth=0.2, ax=ax, edgecolor='0.99', legend=True)
plt.title('Mapa do Brasil com Informações Numéricas por Estado')
plt.show()
