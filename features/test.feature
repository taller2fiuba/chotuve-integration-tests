@wip
Feature: Subir un video

	Scenario: Subida exitosa
		Given que estoy en la aplicación
		When intento subir un video con título "mi primer video"
		Then obtiene una respuesta exitosa
