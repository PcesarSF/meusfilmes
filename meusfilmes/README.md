# Meus Filmes - Projeto Web2py

## Descrição
Aplicação simples para gerenciar filmes favoritos, com consumo da API OMDb para buscar automaticamente informações.

## Funcionalidades
- CRUD completo de filmes
- Consumo de API OMDb no backend
- Cálculo da média das notas dos filmes
- Interface com Bootstrap

## Requisitos
- Python 3.x
- Web2py
- Biblioteca `requests`
- Chave de API gratuita da OMDb: https://www.omdbapi.com/apikey.aspx

## Instalação
1. Baixe o Web2py: http://www.web2py.com/
2. Copie a pasta `meusfilmes` para o diretório `/applications/` do Web2py.
3. Instale dependências:
   ```bash
   pip install requests
   ```
4. Substitua `SUA_API_KEY_OMDB` no arquivo `controllers/default.py` pela sua chave OMDb.
5. Execute o Web2py:
   ```bash
   python web2py.py
   ```
6. Acesse:
   ```
   http://127.0.0.1:8000/meusfilmes
   ```

## Estrutura do Projeto
```
meusfilmes/
    controllers/
    models/
    views/
    static/
    README.md
```
