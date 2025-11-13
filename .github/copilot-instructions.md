# Instruções para Agentes de IA - Arquivos de Programação

## 📋 Visão Geral do Projeto

Este é um workspace de aprendizado com dois principais diretórios:
- **`Fundamentos_de_JS/inicio/`** - Exercícios básicos de JavaScript
- **`Projetos/`** - Projetos práticos em diferentes tecnologias (Flask, JavaScript, Python)

## 🏗️ Arquitetura e Componentes

### Estrutura de Projetos

O diretório `Projetos/` contém:

1. **`site_flask/`** - Aplicação web com Flask + HTML
   - Backend: Python Flask com rotas simples
   - Frontend: HTML estático renderizado via `render_template()`
   - Padrão: Uma rota principal (`/`) retorna `index.html`
   - Execução: `python app.py` (debug mode ativado por padrão)

2. **`contador_de_cliques/`** - Projeto vanilla JavaScript
   - Manipulação direta do DOM com `getElementById()`
   - Padrão: event listeners para interatividade
   - Nota: Verifica existência de elementos antes de usar (defensive coding)

3. **`site_demo_integracao_entre_codigos/`** - Integração HTML + CSS + JS
   - JavaScript aguarda `DOMContentLoaded` antes de manipular DOM
   - Padrão: controle de estado com variáveis (`clickCount`)
   - Manipulação dinâmica de estilos via JS (`.style.color`, `.textContent`)

4. **`busca_yt/`** - Automação Python com PyAutoGUI
   - Automação de teclado e mouse para navegação web
   - Padrão: pausas entre comandos para estabilidade (`pyautogui.pause`)
   - Nota: Coordenadas de clique são específicas da resolução da tela

## 🔄 Padrões e Convenções

### JavaScript
- **DOM Ready Check**: Sempre aguardar `DOMContentLoaded` ou verificar se elementos existem
- **Defensive Coding**: Validar existência de elementos antes de usar (ver `contador_de_cliques`)
- **Event Listeners**: Usar `addEventListener()` para interações, não atributos HTML
- **State Management**: Usar variáveis simples para rastrear estado (ex: `clickCount`, `cliques`)
- **Comentários**: Em português, explicando o propósito de cada seção

### Python
- **Flask**: Usar `render_template()` para servir HTML estático
- **Rotas Simples**: Um arquivo `app.py` com decorators `@app.route()`
- **Debug Mode**: Ativado por padrão em desenvolvimento
- **PyAutoGUI**: Configurar `pause` entre comandos; coordenadas podem precisar ajustes

### HTML
- Estrutura HTML5 básica (`<!DOCTYPE>`, `<head>`, `<body>`)
- IDs semânticos para elementos manipulados por JavaScript (ex: `#meuBotao`, `#contador`)
- Títulos descritivos nas páginas

## ⚙️ Fluxos de Desenvolvimento

### Executar Projetos Flask
```bash
cd Projetos/site_flask
python app.py
# Servidor local em http://localhost:5000
```

### Testar Projetos JavaScript
- Abrir arquivos `.html` diretamente no navegador
- Ou usar um servidor local simples: `python -m http.server`

### Automação Python
- Configurar coordenadas específicas da tela
- Adicionar `pyautogui.pause = 1` para estabilidade
- Testar em ambiente controlado (sem interferências do mouse)

## 📝 Convenções Específicas do Codebase

1. **Comentários bilíngues**: Mistura português e inglês em nomes/comentários
2. **Sem linters configurados**: Código segue estilo livre
3. **Projetos independentes**: Cada pasta em `Projetos/` é uma aplicação standalone
4. **Sem testes automatizados**: Testes são manuais

## 🔧 Modificações Recomendadas

Ao adicionar novas features:
- Manter convenção de nomes em português nos comentários
- Adicionar verificações de DOM antes de manipular elementos
- Usar `render_template()` para Flask, não servir HTML manualmente
- Para automação, documentar coordenadas e adicionar timeouts adequados
