Feature: Registro de nuevo usuario

	Scenario: Registro exitoso
		Given que estoy en la aplicación
		When me registro con mail y contraseña
		Then me registro exitosamente

		Scenario: Registro fallido email en uso
			Given que estoy en la aplicación
			And mi mail ya se encuentra registrado
			When me registro con mail y contraseña
			Then veo error de registro porque el mail ya está en uso
