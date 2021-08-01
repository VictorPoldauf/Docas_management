from decouple import config # acessa .env e seta as variaveis necessarias
from models import get_status_port # acessar o arquivo de modelos e importar as funções necessarias
import logging # importa bibiliote geradora de logs

# adicionado o modulo de logging para ficar com a formatacao mais adequada
logging.basicConfig(format="%(asctime)s %(message)s") # (Hugo)

if __name__ == "__main__": 
    ip, port = config("ip_remota"), config("port") # pega ip e porta da remota do arquivo .env
    status = get_status_port(ip, port) # executar função e guardar o valor dentro da variavel
    print(f"o status é : {status}") # print resultado
    logging.info(f"O status eh {status}")



