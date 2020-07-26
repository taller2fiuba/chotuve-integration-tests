Feature: Listar videos

    Background: Estoy logeado
        Given inicie sesión correctamente
        And "desconocido" se registró correctamente

    Scenario: Listar videos de un usuario sin videos
        Given "desconocido" subio un video publico
        And otro usuario se registro
        When listo sus videos
        Then veo sus 0 videos

    Scenario: Listar videos de un usuario con videos
        Given "desconocido" subio un video publico
        And otro usuario subio 2 videos
        When listo sus videos
        Then veo sus 2 videos

    Scenario: Listar mis videos
        Given "desconocido" subio un video publico
        And subi 2 videos
        When listo mis videos
        Then veo mis 2 videos

    Scenario: Muchos videos subidos por un usuario
        Given "desconocido" subio un video publico
        And otro usuario subio 16 videos
        When listo sus videos
        Then veo solo 10 de sus videos

    Scenario: Listar mas videos
        Given "desconocido" subio un video publico
        And otro usuario subio 16 videos
        When listo sus videos
        And listo mas videos del usuario
        Then veo 6 videos mas

    Scenario: Listar videos de un usuario que no existe
        Given "desconocido" subio un video publico
        When listo los videos de un usuario que no existe
        Then veo error porque el usuario no existe
