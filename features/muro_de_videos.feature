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
		    Then veo 2 video del usuario "edu@gma.com"
    
    Scenario: Videos subidos por dos usuarios
		    Given el usuario con email "edu@gma.com" subio 2 videos
		    And el usuario con email "prueba@gma.com" subio 1 videos
		    When estoy en la pantalla principal
        Then veo 3 videos
		    And veo 2 video del usuario "edu@gma.com"
        And veo 1 video del usuario "prueba@gma.com"
