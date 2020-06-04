Feature: Obtener video

    Scenario: Obtener video que existe
        Given el usuario con email "prueba@test.com" subio 1 videos
        When pido el video
        Then veo el video de "prueba@test.com"
    
    Scenario: Obtener video que no existe
        Given inicie sesión correctamente
        And nadie subio videos
        When pido por un video especifico
        Then veo error por que el video no existe
