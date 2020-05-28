Feature: Subir un video

	Scenario: Subida exitosa
		Given inicie sesión correctamente
		When subo un video con título "mi primer video", descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
		Then obtiene una respuesta exitosa
	
	Scenario: Subida fallida porque no inicie sesion
		Given no inicie sesión
		When subo un video con título "mi primer video", descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
		Then veo error porque primero debo iniciar sesión

	Scenario: Subida exitosa sin campos opcionales
		Given inicie sesión correctamente
		When subo un video con título "mi primer video", sin descripción, ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
		Then obtiene una respuesta exitosa

	Scenario: Subida fallida falta algun campo obligatorio
		Given inicie sesión correctamente
		When subo un video sin título, con descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
		Then veo error porque la información no es válida

	Scenario: Subida fallida la visibilidad es incorrecta
		Given inicie sesión correctamente
		When subo un video con título "mi primer video", descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "cualquier cosa"
		Then veo error porque la información no es válida

