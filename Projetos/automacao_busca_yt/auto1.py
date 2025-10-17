import urllib.parse

# 1 Solicita ao usuário o termo de pesquisa do YouTube
search_query = input("Qual pesquisa você gostaria de fazer no YouTube? ")

# Codifica o termo de pesquisa para uso em URL
encoded_search_query = urllib.parse.quote_plus(search_query)

# Gera o link de pesquisa do YouTube
youtube_search_url = f'https://www.youtube.com/results?search_query={encoded_search_query}'

print(f"\nAqui está o link para a pesquisa no YouTube:")
print(youtube_search_url)


# Abre o link no navegador padrão
import webbrowser   
webbrowser.open(youtube_search_url)
import urllib.parse


# 1 Solicita ao usuário o termo de pesquisa do YouTube
search_query = input("Qual pesquisa você gostaria de fazer no YouTube? ")

# Codifica o termo de pesquisa para uso em URL
encoded_search_query = urllib.parse.quote_plus(search_query)

# Gera o link de pesquisa do YouTube
youtube_search_url = f'https://www.youtube.com/results?search_query={encoded_search_query}'
print(f"\nAqui está o link para a pesquisa no YouTube:")
print(youtube_search_url)
