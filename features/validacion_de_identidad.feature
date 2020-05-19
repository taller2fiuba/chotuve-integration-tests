Feature: Validación de identidad

	Scenario: Validación exitosa
		Given inicie sesión correctamente
		When pido mi mail
		Then recibo mi mail correctamente

	Scenario: Validación fallida sesión no iniciada
		Given no inicie sesión
		When pido mi mail
		Then veo error porque primero debo iniciar sesión

	Scenario: Validación fallida sesión invalida o caducada
		Given estoy registrado
		And mi sesion es invalida o caduco
		When pido mi mail
		Then veo error porque debo volver a iniciar sesión
