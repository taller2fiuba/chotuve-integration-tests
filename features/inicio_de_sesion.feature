Feature: Inicio sesión en la aplicación

	Scenario:  Inicio de sesión exitoso
		Given estoy registrado
		When inicio sesion con mi mail y contraseña correctos
		Then ingreso exitosamente a mi cuenta

	Scenario: Inicio de sesión fallido mail o contraseña incorrecto
		Given estoy registrado
		When inicio sesion con mi mail o contraseña incorrectos
		Then veo error de inicio de sesión porque el mail o la contraseña es incorrecto

	Scenario: Inicio de sesión fallido no registrado
		Given no estoy registrado
		When inicio sesion con mi mail y contraseña correctos
		Then veo error de inicio de sesión porque el mail o la contraseña es incorrecto
