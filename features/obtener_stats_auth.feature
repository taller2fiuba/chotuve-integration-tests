Feature: Obtener stats auth server

    Scenario: Obtener estadisticas de cantidad de usuarios sin usuarios
        When veo las estadisticas de usuarios
        Then veo que se registraron 0 usuarios

    Scenario: Obtener estadisticas de cantidad de usuarios cuando hay multiples usuarios registrados
        Given inicie sesión correctamente
        And "edson" se registró correctamente
        When veo las estadisticas de usuarios
        then veo que se registraron 2 usuarios
