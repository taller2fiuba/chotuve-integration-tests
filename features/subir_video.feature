Feature: Subir un video

	Scenario: Subida exitosa
		Given inicie sesión correctamente
		When intento subir un video con título "mi primer video"
		Then obtiene una respuesta exitosa
	
	Scenario: Subida fallida
		Given no inicie sesión
		When intento subir un video con título "mi primer video"
		Then veo error porque primero debo iniciar sesión
