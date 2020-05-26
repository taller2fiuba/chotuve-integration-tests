Feature: Muro de videos

    Background:
		Given inicie sesión correctamente

    Scenario: Sin videos
        Given nadie subio videos
        When estoy en la pantalla principal
        Then no veo ningun video