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
        And veo que hay 0 contactos

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay multiples reacciones
        Given el usuario con email "lucho@lucho.com" subio 1 videos
		And reacciono al video
        And el usuario con email "mati@mati.com" subio 1 videos
        And reacciono al video
        When veo las estadisticas
        then veo que hay 2 reaccion
        And veo que hay 0 contactos

    Scenario: Obtener estadisticas de cantidad de contactos cuando hay una relacion de amistad
        Given "edson" me mandó solicitud de contacto
        And acepto la solicitud de contacto
        When veo las estadisticas
        then veo que hay 1 contactos
        And veo que hay 0 reaccion

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay multiples relaciones de amistad
        Given "edson" me mandó solicitud de contacto
		And acepto la solicitud de contacto
        Given "lucho" me mandó solicitud de contacto
        And acepto la solicitud de contacto
        When veo las estadisticas
        then veo que hay 2 contactos
        And veo que hay 0 reaccion

    Scenario: Obtener estadisticas de cantidad de reacciones cuando hay multiples relaciones de amistad
        Given "edson" me mandó solicitud de contacto
		And acepto la solicitud de contacto
        Given "lucho" me mandó solicitud de contacto
        And acepto la solicitud de contacto
        When veo las estadisticas
        then veo que hay 2 contactos
        And veo que hay 0 reaccion