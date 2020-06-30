def assert_status_code(esperado, real):
    assert esperado == real, \
           f'Código de retorno incorrecto: {real}, esperado: {esperado}'
        