# ETL para API Rick and Morty

Este é um exemplo de um processo ETL (Extração, Transformação e Carga) para coletar informações sobre episódios da série Rick and Morty, calcular o número total de episódios e carregar esses dados em um arquivo CSV.

## Requisitos

- Python 3.x
- Biblioteca `requests` para fazer chamadas à API
- Biblioteca `csv` para manipulação de arquivos CSV

## Passos do ETL

### 1. Extração

A extração é realizada utilizando a API pública da série Rick and Morty. O script faz uma chamada à API para obter informações sobre os episódios.


### 2. Transformação

A transformação envolve o cálculo do número total de episódios.


### 3. Carga

A carga envolve o carregamento dos dados em um arquivo CSV.

## Executando o ETL

1. Certifique-se de ter Python 3.x instalado.
2. Instale as bibliotecas necessárias executando `pip install requests` e `pip install csv`.
3. Execute o script `index.py`.

## Resultados

Após a execução bem-sucedida do ETL, os dados dos episódios serão carregados no arquivo CSV `episodes_data.csv`.