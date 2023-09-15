import openrouteservice 
import folium
import webbrowser

# Substitua 'YOUR_API_KEY' pela sua chave de API OpenRouteService
api_key = '5b3ce3597851110001cf62480b2433fb93fa4bf4bcda5d0487e0ee7f' # não esquecer de trocar

# Nomes de ruas (endereços)
ponto_partida_nome = input("Informe o local de partida: ") 
destino_nome = input("Informe o local de destino: ") 

# Inicialize o cliente OpenRouteService
client = openrouteservice.Client(key=api_key)

# Use o geocoder para obter as coordenadas dos nomes de ruas
coordenadas_partida = client.pelias_search(ponto_partida_nome)['features'][0]['geometry']['coordinates']
coordenadas_destino = client.pelias_search(destino_nome)['features'][0]['geometry']['coordinates']

# Solicite uma rota usando as coordenadas
rota = client.directions(
    coordinates=[coordenadas_partida, coordenadas_destino],
    profile='driving-car',  # Você pode usar 'foot-walking' para rota a pé
    format='geojson',
)

if 'features' in rota:
    # Crie um mapa com o folium
    mapa = folium.Map(location=[coordenadas_partida[1], coordenadas_partida[0]], zoom_start=15)

    # Adicione a rota ao mapa
    folium.GeoJson(rota).add_to(mapa)

    # Abra o mapa em um navegador
    mapa.save('rota.html')
    webbrowser.open_new_tab('rota.html') # abre o mapa automaticamente

    print("Mapa da rota foi salvo como 'rota.html'.")
else:
    print("Não foi possível encontrar uma rota.")
