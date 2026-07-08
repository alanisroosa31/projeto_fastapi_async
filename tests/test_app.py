from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


# criando um teste para siomular alguem acessando a minha API
def test_root_deve_retornar_ok_e_ola_mundo():

    # pegando a aplicação e envolvendo ela em um cliente de teste
    client = TestClient(app)  # arrange (organizacao)

    # acessando o endpoint raiz e o resultado da requisição vai ser armazenado na variavel response
    response = client.get('/')  # act (acao)

    # assert (verificacao) que o status code da resposta seja 200 e que o json retornado seja igual a {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
