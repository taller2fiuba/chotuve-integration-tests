Feature: Muro de videos

    Background:
		Given inicie sesión correctamente

    Scenario: Sin videos
      Given nadie subio videos
      When estoy en la pantalla principal
      Then no veo ningun video
    
    Scenario: Videos subidos por un usuario
      Given el usuario con email "edu@test.com" subio 2 videos
      When estoy en la pantalla principal
      Then veo 2 video del usuario "edu@test.com"
  
    Scenario: Videos subidos por dos usuarios
      Given el usuario con email "edu@test.com" subio 2 videos
      And el usuario con email "prueba@test.com" subio 1 videos
      When estoy en la pantalla principal
      Then veo 3 videos
      And veo 2 video del usuario "edu@test.com"
      And veo 1 video del usuario "prueba@test.com"

    Scenario: Videos subidos por mi
      Given el usuario con email "prueba@test.com" subio 2 videos
      And yo subi 1 videos
      When estoy en la pantalla principal
      Then veo 2 videos
    
    Scenario: Muchos videos subidos
      Given el usuario con email "prueba@test.com" subio 15 videos
      When estoy en la pantalla principal
      Then veo 10 videos

    Scenario: Pedir mas videos
      Given el usuario con email "prueba@test.com" subio 16 videos
      When estoy en la pantalla principal
		  Then veo 10 videos
		  When pido mas videos
      Then veo 6 videos mas

    Scenario: Pedir videos inexistentes (offset muy grande)
      Given el usuario con email "prueba@test.com" subio 12 videos
      When estoy en la pantalla principal
		  Then veo 10 videos 
		  When pido videos inexistentes
      Then veo 0 videos mas
  
