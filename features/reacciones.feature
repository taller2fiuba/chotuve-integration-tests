Feature: Reacción a un video
	
	Scenario: Reaccionar "me gusta" a un video
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		When reacciono "me gusta" al video
		Then veo que el video tiene 1 "me gusta"
		And veo que yo reaccioné "me gusta"
	
	Scenario: Reaccionar "no me gusta" a un video
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		When reacciono "no me gusta" al video
		Then veo que el video tiene 1 "no me gusta"
		And veo que yo reaccioné "no me gusta"
	
	Scenario: Ver reacciones a un video
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		And el usuario con email "hola@chau.com" reaccionó "me gusta" al video
		Then veo que el video tiene 1 "me gusta"
		And veo que yo no reaccioné
	
	Scenario: Eliminar reacción
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		And reaccioné "me gusta" al video
		When reacciono "me gusta" al video
		Then veo que yo no reaccioné
	
	Scenario: Cambiar reacción
		Given el usuario con email "lucho@lucho.com" subio 1 videos
		And reaccioné "no me gusta" al video
		When reacciono "me gusta" al video
		Then veo que yo reaccioné "me gusta"
