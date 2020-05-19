Feature: Subir un video

	Scenario: Subida exitosa
		When intento subir un video con título "mi primer video"
		Then obtiene una respuesta exitosa
