import requests # request é a biblioteca responsavel por fazer requisições HTTP
import json # É responsavel por padronizar entradas e saidas de dados no formato json
import datetime
import logging

#  [X] DONE: deixar as variaveis de configuracao de IP e Porta no arquivo .env (01/08/21)
#  [ ] TODO: padronizar as chaves do objeto JSON seguindo o padrao javascript
#  [X] DONE: renomear o "data_time" para "dateTime" ou algum sinonimo em ingles respeitando o Case (01/08/21)
#  [X] DONE: "models" seria o melhor nome para esse arquivo? (01/08/21)
#  [X] DONE: padronizar o uso de aspas simples ou duplas, deixar o codigo uniforme (01/08/21)
#  [ ] TODO: adicionar um try/catch para o processo de requisicao



def get_status_port(ip, port):  # Função criada para simplificar a requisição dos dados da remota
    remota_url = f"http://{ip}/api/crown/ac/GetRestDataOut" # Endereço reponsavel pela remota (api)
    param ={"data":{"Offset":port,"dataTime":"hoje"}}  # indicação de qual porta eu quero pegar da remota ( comando json a ser enviado para a remota )
    headers = {"content-type": "application/json"} # estamos especificando o formato de entrega HTTP
    response = requests.post(remota_url,data=json.dumps(param), headers=headers) #  enviando uma requisição post na url da remota, transformando os parametros em json e especificando o cabeçalho
    response_json =json.loads(response.content) # recebimento da resposta e leitura do conteudo na integra
    status_port= response_json["data"]["Value"] # seleção dos dados importantes da requisição
    return status_port

def get_time(): # (Hugo)
    now = datetime.datetime.now()
    round_mili = str(now.microsecond // 1000) # round is only for decimal numbers
    str_time = now.strftime("%Y-%m-%dT%X:" + round_mili)
    return str_time
