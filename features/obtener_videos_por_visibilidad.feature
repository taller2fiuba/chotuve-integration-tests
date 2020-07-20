Feature: Obtener videos por visibilidad

    Background: Estoy logueado y existe el usuario "edson"
        Given inicie sesión correctamente
        And "edson" se registró correctamente
        And "otro" se registró correctamente

    Scenario: Obtener videos privados de un amigo
        Given "edson" es mi amigo
        Given "edson" subio un video privado
        Given "otro" subio un video publico
        When listo los videos de "edson"
        Then veo sus 1 videos

    Scenario: Obtener videos privados de un usuario
        Given "edson" subio un video privado
        When listo los videos de "edson"
        Then veo sus 0 videos

    Scenario: Ver videos privados de un amigo en pantalla principal
        Given "edson" es mi amigo
        Given "edson" subio un video privado
        When estoy en la pantalla principal
        Then veo 1 videos

    Scenario: Ver videos privados en pantalla principal
        Given "edson" subio un video privado
        When estoy en la pantalla principal
        Then veo 0 videos