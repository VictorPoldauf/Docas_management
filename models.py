import requests # request é a biblioteca responsavel por fazer requisições HTTP
import json # É responsavel por padronizar entradas e saidas de dados no formato json
import datetime

# TODO: deixar as variaveis de configuracao de IP e Porta no arquivo .env
# TODO: padronizar as chaves do objeto JSON seguindo o padrao javascript
# TODO: renomear o "data_time" para "dateTime" ou algum sinonimo

def get_status_port(port,ip):  # Função criada para simplificar a requisição dos dados da remota
    remota_url = f'http://{ip}/api/crown/ac/GetRestDataOut' # Endereço reponsavel pela remota (api)
    param ={"data":{"Offset":port,"data_time":'hoje'}}  # indicação de qual porta eu quero pegar da remota ( comando json a ser enviado para a remota )
    headers = {'content-type': 'application/json'} # estamos especificando o formato de entrega HTTP
    response = requests.post(remota_url,data=json.dumps(param), headers=headers) #  enviando uma requisição post na url da remota, transformando os parametros em json e especificando o cabeçalho
    response_json =json.loads(response.content) # recebimento da resposta e leitura do conteudo na integra
    status_port= response_json['data']['Value'] # seleção dos dados importantes da requisição
    return status_port # retona os valore da função

def get_time():
    now = datetime.datetime.now()
    year,month,day,hour,mili = now.strftime("%Y"),now.strftime("%m"),now.strftime("%d"),now.strftime("%X"),round(int(now.strftime("%f")),3)
    time_now = f"{year}-{month}-{day}T{hour}:{mili}Z"
    return time_now

def get_time_v2():
    now = datetime.datetime.now()
    round_mili = str(round(int(now.microsecond), 3))
    str_time = now.strftime('%Y-%m-%d%X'+round_mili)
    return str_time
