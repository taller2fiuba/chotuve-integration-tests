Feature: Comentar un video

	Scenario: Comentar un video
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		When comento "holis" en un video
		Then veo que hay un comentario mio que dice "holis"

	Scenario: Ver comentarios de un video
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		And el usuario "test1@test.com" comentó "hola"
		And el usuario "test2@test.com" comentó "adios"
		And el usuario "test3@test.com" comentó "chau"
		Then veo que hay 3 comentarios
		And veo que hay un comentario que dice "hola" del usuario "test1@test.com"
		And veo que hay un comentario que dice "adios" del usuario "test2@test.com"
		And veo que hay un comentario que dice "chau" del usuario "test3@test.com"
