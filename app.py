from keys import ip_remota
from models import get_status_port # acessar o arquivo de modelos e importar as funções necessarias
import logging

# adicionado o modulo de logging para ficar com a formatacao mais adequada
logging.basicConfig(format='%(asctime)s %(message)s')

if __name__ == "__main__":
    # colocar o codigo principal aqui
    ip = ip_remota # introduzir ip
    status_de_agora = get_status_port(0,ip) # executar função e guardar o valor dentro da variavel
    print(f'o status é : {status_de_agora}') # print resultado
    status = get_status_port(0, ip) # Tentar escrever todas variaveis em portugues
    logging.info(f'O status eh {status}')

