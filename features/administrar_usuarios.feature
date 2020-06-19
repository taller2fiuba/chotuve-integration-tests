Feature: Administración de usuarios

	Scenario: ver usuarios disponibles desde el web admin
		Given se crearon 5 usuarios
		When veo los usuarios desde el web admin
		Then veo que hay 5 usuarios

	Scenario: deshabilitar usuario
		Given se crearon 1 usuarios
		When "deshabilito" al usuario desde el web admin
		Then veo que el usuario está "deshabilitado"

	Scenario: habilitar usuario
		Given hay un usuario deshabilitado
		When "habilito" al usuario desde el web admin
		Then veo que el usuario está "habilitado"
	
	Scenario: usuario deshabilitado no puede iniciar sesión
		Given se crearon 1 usuarios
		When "deshabilito" al usuario desde el web admin
		And el usuario inicia sesión
		Then ve error indicando que no está autorizado
		