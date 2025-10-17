import pyautogui as pa
import time

# Configura um tempo de pausa entre os comandos do PyAutoGUI
pa.pause = 1

# Abre o menu iniciar do Windows e pesquisa pelo navegador Opera
pa.press('win')
pa.write('opera')
pa.press('enter')

# Aguarda o navegador abrir

time.sleep(2)

# Foca na barra de endereços e acessa o YouTube
pa.hotkey('ctrl', 'l')
youtube_url = 'https://www.youtube.com'
pa.write(youtube_url)
pa.press('enter')

# Aguarda a página carregar
time.sleep(3)

# Clica na barra de pesquisa do YouTube (ajuste as coordenadas conforme necessário)
search_bar_x = 561
search_bar_y = 129
pa.click(x=search_bar_x, y=search_bar_y)

# Pesquisa pelo vídeo desejado
search_query = ' '
pa.write(search_query)
pa.press('enter')

# Aguarda os resultados aparecerem
time.sleep(2)

# Clica no primeiro vídeo da lista (ajuste as coordenadas conforme necessário)
first_video_x = 605
first_video_y = 355
pa.click(x=first_video_x, y=first_video_y)

# Aguarda o vídeo carregar
time.sleep(2)
# O script agora está completo e pronto para ser executado.