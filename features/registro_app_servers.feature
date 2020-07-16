Feature: Registro de app servers

	Background: Soy administrador
		Given inicié sesión como administrador

	Scenario: Dar de alta un app server
		When creo un nuevo app server con url "ar1-appserver.com" y nombre "ar1-appserver"
		Then me devuelve un token

	Scenario: Ver app servers habilitados
		Given creé un nuevo app server con url "ar1-appserver.com" y nombre "ar1-appserver"
		When veo los app servers habilitados
		Then veo que los app servers habilitados son "ar1-appserver.com"	

	Scenario: Eliminar app server habilitado
		Given creé un nuevo app server con url "ar1-appserver.com" y nombre "ar1-appserver"
		When elimino el app server con nombre "ar1-appserver.com"
		And veo los app servers habilitados
		Then veo que no hay app servers habilitados