from keys import ip_remota
from models import get_status_port # acessar o arquivo de modelos e importar as funções necessarias

if __name__ == "__main__":
    # TODO: colocar o codigo principal aqui
    ip = ip_remota # introduzir ip
    status_de_agora = get_status_port(0,ip) # executar função e guardar o valor dentro da variavel
    print(f'o status é : {status_de_agora}') # print resultado
    pass

