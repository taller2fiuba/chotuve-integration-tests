Feature: Obtener stats app server

    Background: Estoy logueado y existe el usuario "edson"
        Given inicie sesión correctamente
        And "edson" se registró correctamente
        And "lucho" se registró correctamente

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay una reaccion
        Given el usuario con email "lucho@lucho.com" subio 1 videos
		And reacciono al video
        When veo las estadisticas
        then veo que hay 1 reaccion
        And veo que hay 0 comentario

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay multiples reacciones
        Given el usuario con email "lucho@lucho.com" subio 1 videos
		And reacciono al video
        And el usuario con email "mati@mati.com" subio 1 videos
        And reacciono al video
        When veo las estadisticas
        then veo que hay 2 reaccion
        And veo que hay 0 comentario

    Scenario: Obtener estadisticas de cantidad de comentarios cuando hay un solo comentario
        Given el usuario con email "lucho@lucho.com" subio 1 videos
		And el usuario "test1@test.com" comentó "hola"
        When veo las estadisticas
        then veo que hay 1 comentario
        And veo que hay 0 reaccion

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay multiples reacciones en un video
        Given el usuario con email "lucho@lucho.com" subio 1 videos
		And el usuario "test1@test.com" comentó "hola"
		And el usuario "test2@test.com" comentó "adios"
        When veo las estadisticas
        then veo que hay 2 comentario
        And veo que hay 0 reaccion

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay multiples reacciones en mas de un video        Given el usuario con email "lucho@lucho.com" subio 1 videos
		Given el usuario con email "lucho@lucho.com" subio 1 videos
        And el usuario "test1@test.com" comentó "hola"
		And el usuario "test2@test.com" comentó "adios"
        Given el usuario con email "edson@edos.com" subio 1 videos
        And el usuario "test3@test.com" comentó "hola"
		And el usuario "test4@test.com" comentó "adios"
        When veo las estadisticas
        then veo que hay 4 comentario
        And veo que hay 0 reaccion    
