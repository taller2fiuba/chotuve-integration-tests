Feature: Muro de videos

    Background:
		Given inicie sesión correctamente

    Scenario: Sin videos
        Given nadie subio videos
        When estoy en la pantalla principal
        Then no veo ningun video
    
    Scenario: Videos subidos por un usuario
		    Given el usuario con email "edu@gma.com" subio 2 videos
		    When estoy en la pantalla principal
		    Then veo sus dos videos