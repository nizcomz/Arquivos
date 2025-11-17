import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
import requests
import csv
import unicodedata
from datetime import datetime
import webbrowser
import os


# Para consulta viacep.com.br/ws/01001000/json/

STATE_TO_UF = {
    'acre': 'AC', 'alagoas': 'AL', 'amapa': 'AP', 'amazonas': 'AM', 'bahia': 'BA',
    'ceara': 'CE', 'ceará': 'CE', 'distrito federal': 'DF', 'espirito santo': 'ES',
    'espírito santo': 'ES', 'goias': 'GO', 'goiás': 'GO', 'maranhao': 'MA', 'maranhão': 'MA',
    'mato grosso': 'MT', 'mato grosso do sul': 'MS', 'minas gerais': 'MG', 'para': 'PA', 'pará': 'PA',
    'paraiba': 'PB', 'paraíba': 'PB', 'parana': 'PR', 'paraná': 'PR', 'pernambuco': 'PE',
    'piaui': 'PI', 'piauí': 'PI', 'rio de janeiro': 'RJ', 'rio grande do norte': 'RN',
    'rio grande do sul': 'RS', 'rondonia': 'RO', 'rondônia': 'RO', 'roraima': 'RR',
    'santa catarina': 'SC', 'sao paulo': 'SP', 'são paulo': 'SP', 'sergipe': 'SE', 'tocantins': 'TO'
}

# Mapa com chaves normalizadas (sem acentos) para melhorar correspondência
NORMALIZED_STATE_TO_UF = {}
for k, v in STATE_TO_UF.items():
    nk = unicodedata.normalize('NFKD', k).encode('ASCII', 'ignore').decode('ASCII')
    NORMALIZED_STATE_TO_UF[nk.lower()] = v


def buscar_info():
    cidade = entry_cidade.get().strip()
    bairro = entry_bairro.get().strip()

    if not cidade:
        messagebox.showwarning("Entrada inválida", "Por favor informe a cidade.")
        return

    endereco = f"{bairro}, {cidade}, Brasil" if bairro else f"{cidade}, Brasil"

    geolocator = Nominatim(user_agent="buscador-coords-app")
    try:
        location = geolocator.geocode(endereco, language='pt')
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar geolocalização: {e}")
        return

    resultado = ''
    if location:
        resultado = f"Latitude: {location.latitude}\nLongitude: {location.longitude}"

        # Tentar obter CEP a partir dos dados retornados pelo Nominatim
        endereco_raw = location.raw.get('address', {}) if location.raw else {}
        cep = endereco_raw.get('postcode')
        # Tenta várias chaves possíveis para o nome do estado/região
        state = (
            endereco_raw.get('state')
            or endereco_raw.get('region')
            or endereco_raw.get('state_district')
            or endereco_raw.get('county')
        )

        if cep:
            resultado += f"\nCEP (via geocoding): {cep}"
        else:
            # Normalizar e inferir UF a partir do campo 'state' retornado pelo Nominatim
            uf = None
            if state:
                state_norm = unicodedata.normalize('NFKD', state).encode('ASCII', 'ignore').decode('ASCII').lower().strip()
                uf = NORMALIZED_STATE_TO_UF.get(state_norm)
                if not uf:
                    for k, v in NORMALIZED_STATE_TO_UF.items():
                        if k in state_norm or state_norm in k:
                            uf = v
                            break

            if uf:
                try:
                    # Informações para o usuário sobre inferência
                    municipio = (endereco_raw.get('city') or endereco_raw.get('town') or endereco_raw.get('village') or endereco_raw.get('municipality') or cidade)
                    resultado += f"\nUF inferida: {uf} | Município: {municipio}"
                    last_urls = []
                    from urllib.parse import quote

                    # Determinar município com preferências das chaves do Nominatim
                    municipio = (endereco_raw.get('city') or endereco_raw.get('town') or endereco_raw.get('village') or endereco_raw.get('municipality') or cidade)
                    municipio_enc = quote(municipio)
                    cep_v = None

                    # Construir candidatos a logradouro a partir do resultado do Nominatim e do bairro informado
                    candidatos = []
                    for key in ('road', 'street', 'residential', 'neighbourhood', 'suburb', 'quarter'):
                        val = endereco_raw.get(key)
                        if val and val not in candidatos:
                            candidatos.append(val)
                    if bairro and bairro not in candidatos:
                        candidatos.append(bairro)

                    # Tentar buscar por cada candidato como logradouro
                    for cand in candidatos:
                        if not cand:
                            continue
                        url_viacep = f"https://viacep.com.br/ws/{uf}/{municipio_enc}/{quote(cand)}/json/"
                        last_urls.append(url_viacep)
                        resp = requests.get(url_viacep, timeout=8)
                        if resp.status_code == 200:
                            dados = resp.json()
                            if isinstance(dados, list) and dados:
                                detalhes_ceps = []
                                for item in dados[:10]:
                                    cep_item = item.get('cep')
                                    logradouro = item.get('logradouro') or ''
                                    bairro_item = item.get('bairro') or ''
                                    descricao = logradouro or bairro_item or ''
                                    if cep_item:
                                        detalhes_ceps.append(f"{cep_item}" + (f" ({descricao})" if descricao else ""))
                                if detalhes_ceps:
                                    cep_v = detalhes_ceps[0].split(' ')[0]
                                    resultado += "\nCEP(s) encontrados via ViaCEP: " + ", ".join(detalhes_ceps[:5])
                                    break
                            elif isinstance(dados, dict) and dados.get('cep'):
                                cep_v = dados.get('cep')
                                resultado += f"\nCEP (via ViaCEP): {cep_v}"
                                break

                    # Se ainda não encontrou, tentar por município (lista de CEPs do município)
                    if not cep_v:
                        url_viacep = f"https://viacep.com.br/ws/{uf}/{municipio_enc}/json/"
                        last_urls.append(url_viacep)
                        resp = requests.get(url_viacep, timeout=8)
                        if resp.status_code == 200:
                            dados = resp.json()
                            if isinstance(dados, list) and dados:
                                detalhes_ceps = []
                                for item in dados[:10]:
                                    cep_item = item.get('cep')
                                    logradouro = item.get('logradouro') or ''
                                    bairro_item = item.get('bairro') or ''
                                    descricao = logradouro or bairro_item or ''
                                    if cep_item:
                                        detalhes_ceps.append(f"{cep_item}" + (f" ({descricao})" if descricao else ""))
                                if detalhes_ceps:
                                    cep_v = detalhes_ceps[0].split(' ')[0]
                                    resultado += "\nCEP(s) encontrados via ViaCEP: " + ", ".join(detalhes_ceps[:5])
                                else:
                                    resultado += "\nCEP não encontrado via ViaCEP."
                            elif isinstance(dados, dict) and dados.get('cep'):
                                cep_v = dados.get('cep')
                                resultado += f"\nCEP (via ViaCEP): {cep_v}"
                            else:
                                resultado += "\nCEP não encontrado via ViaCEP."
                        else:
                            resultado += f"\nFalha ao consultar ViaCEP (status {resp.status_code})."
                    # Se não encontrou CEP, informe as URLs tentadas para depuração
                    if not cep_v and last_urls:
                        resultado += f"\nURLs tentadas: {last_urls[:5]}"
                except Exception as ex:
                    resultado += f"\nNão foi possível consultar o CEP via ViaCEP: {ex}"
                # Atualiza variáveis globais com as URLs tentadas (para os botões)
                try:
                    global LAST_VIACEP_URLS, LAST_VIACEP_URL
                    if 'last_urls' in locals() and last_urls:
                        LAST_VIACEP_URLS = last_urls
                        LAST_VIACEP_URL = last_urls[-1]
                    elif 'url_viacep' in locals() and url_viacep:
                        LAST_VIACEP_URLS = [url_viacep]
                        LAST_VIACEP_URL = url_viacep
                    # Atualiza exibição na GUI, se disponível
                    try:
                        set_ultima_urls_display(LAST_VIACEP_URLS)
                    except Exception:
                        pass
                except Exception:
                    # Não falhar por causa de debug vars
                    pass
            else:
                # Tentar correspondência alternativa com outras chaves e informar ao usuário de forma menos alarmante
                alternativa_encontrada = False
                for tk in (endereco_raw.get('county'), endereco_raw.get('region'), endereco_raw.get('state_district')):
                    if not tk:
                        continue
                    tk_norm = unicodedata.normalize('NFKD', tk).encode('ASCII', 'ignore').decode('ASCII').lower().strip()
                    if tk_norm in NORMALIZED_STATE_TO_UF:
                        alternativa_encontrada = True
                        resultado += "\nUF inferido por chave alternativa. Tente buscar novamente para consultar ViaCEP."
                        break
                if not alternativa_encontrada:
                    resultado += "\nUF não identificado - não foi possível consultar ViaCEP."
    else:
        resultado = "Localização não encontrada!"

    messagebox.showinfo("Resultado", resultado)

    # Salvar histórico da busca em CSV
    try:
        csv_path = 'history_buscas.csv'
        # Atualiza variável global com caminho do CSV (usado pelo botão abrir histórico)
        global CSV_PATH
        CSV_PATH = csv_path
        # Informações para salvar
        cep_geocoding = cep if 'cep' in locals() and cep else ''
        cep_viacep = cep_v if 'cep_v' in locals() and cep_v else ''
        viacep_url = url_viacep if 'url_viacep' in locals() and url_viacep else ''
        status = 'OK' if location else 'NOT_FOUND'
        timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')

        row = {
            'timestamp': timestamp,
            'cidade': cidade,
            'bairro': bairro,
            'latitude': getattr(location, 'latitude', ''),
            'longitude': getattr(location, 'longitude', ''),
            'cep_geocoding': cep_geocoding,
            'cep_viacep': cep_viacep,
            'viacep_url': viacep_url,
            'status': status,
            'resultado_text': resultado.replace('\n', ' | ')
        }

        write_header = False
        try:
            # Verifica se arquivo existe e se está vazio
            with open(csv_path, 'r', encoding='utf-8', newline='') as f:
                first = f.read(1)
                if not first:
                    write_header = True
        except FileNotFoundError:
            write_header = True

        with open(csv_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(row.keys()))
            if write_header:
                writer.writeheader()
            writer.writerow(row)
    except Exception:
        # Não bloquear o usuário caso o salvamento falhe
        pass


# Variáveis globais para depuração / botões
LAST_VIACEP_URLS = []
LAST_VIACEP_URL = None
CSV_PATH = 'history_buscas.csv'


def abrir_ultima_url():
    """Abre a última URL ViaCEP tentada no navegador padrão."""
    global LAST_VIACEP_URLS, LAST_VIACEP_URL
    url = None
    # Preferir última URL usada explicitamente, senão a última da lista
    if LAST_VIACEP_URL:
        url = LAST_VIACEP_URL
    elif LAST_VIACEP_URLS:
        url = LAST_VIACEP_URLS[-1]

    if not url:
        messagebox.showinfo("Aberto URL ViaCEP", "Nenhuma URL ViaCEP registrada ainda.")
        return

    try:
        webbrowser.open(url)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir a URL: {e}")


def abrir_historico():
    """Abre o arquivo CSV de histórico com o aplicativo padrão do sistema (Windows: Explorer/Excel)."""
    global CSV_PATH
    try:
        # Em Windows, os startfile abrem com o app padrão
        if os.path.exists(CSV_PATH):
            os.startfile(CSV_PATH)
        else:
            messagebox.showinfo("Histórico", f"Arquivo de histórico não encontrado: {CSV_PATH}")
    except Exception as e:
        messagebox.showerror("Erro ao abrir histórico", f"Não foi possível abrir o arquivo: {e}")


def set_ultima_urls_display(urls):
    """Atualiza o widget de texto com as últimas URLs tentadas."""
    try:
        txt = janela.nametowidget('txt_urls')
    except Exception:
        return
    try:
        txt.config(state='normal')
        txt.delete('1.0', tk.END)
        if urls:
            for u in urls:
                txt.insert(tk.END, u + '\n')
        txt.config(state='disabled')
    except Exception:
        pass


def copiar_urls():
    """Copia o conteúdo do widget de URLs para a área de transferência."""
    try:
        txt = janela.nametowidget('txt_urls')
        content = txt.get('1.0', tk.END).strip()
        if not content:
            messagebox.showinfo("Copiar URLs", "Nenhuma URL para copiar.")
            return
        janela.clipboard_clear()
        janela.clipboard_append(content)
        messagebox.showinfo("Copiar URLs", "URLs copiadas para a área de transferência.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível copiar: {e}")


# Interface gráfica
janela = tk.Tk()
janela.title("Buscador de Coord. & CEP")

tk.Label(janela, text="Cidade:").grid(row=0, column=0, sticky='w', padx=6, pady=6)
entry_cidade = tk.Entry(janela, width=40)
entry_cidade.grid(row=0, column=1, padx=6, pady=6)

tk.Label(janela, text="Bairro (opcional):").grid(row=1, column=0, sticky='w', padx=6, pady=6)
entry_bairro = tk.Entry(janela, width=40)
entry_bairro.grid(row=1, column=1, padx=6, pady=6)

botao_buscar = tk.Button(janela, text="Buscar", command=buscar_info)
botao_buscar.grid(row=2, column=0, columnspan=2, pady=10)

# Botões auxiliares: abrir última URL ViaCEP e abrir histórico CSV
botao_abrir_url = tk.Button(janela, text="Abrir última URL ViaCEP", command=abrir_ultima_url)
botao_abrir_url.grid(row=3, column=0, pady=6, padx=6, sticky='w')

botao_abrir_hist = tk.Button(janela, text="Abrir histórico (CSV)", command=abrir_historico)
botao_abrir_hist.grid(row=3, column=1, pady=6, padx=6, sticky='e')

# Caixa de texto onde aparecem as últimas URLs tentadas (read-only)
tk.Label(janela, text="URLs ViaCEP tentadas:").grid(row=4, column=0, sticky='w', padx=6, pady=(8,0))
txt_urls = tk.Text(janela, name='txt_urls', width=60, height=4, wrap='word', state='disabled')
txt_urls.grid(row=5, column=0, columnspan=2, padx=6, pady=(0,6))

botao_copiar = tk.Button(janela, text="Copiar URLs", command=copiar_urls)
botao_copiar.grid(row=6, column=0, columnspan=2, pady=(0,10))

janela.mainloop()

