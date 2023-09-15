destinoPartidaFavoritos = []
destinoPartidaFavorito = ""

while destinoPartidaFavorito != "0":
    destinoPartidaFavorito = input("Informe seu ponto de partida ou destino favorito (ou digite 0 para sair): ")
    
    if destinoPartidaFavorito != "0":
        destinoPartidaFavoritos.append(destinoPartidaFavorito)

print(destinoPartidaFavoritos)
