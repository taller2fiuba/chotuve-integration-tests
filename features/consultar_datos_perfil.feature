Feature: Consultar datos de perfiles

	Scenario: Consultar datos de mi perfil con campos no cargados
		Given inicie sesión correctamente
		When veo los datos de mi perfil
		Then veo mi mail "test@test.com" 

	Scenario: Consultar datos de mi perfil con campos cargados
		Given inicie sesión correctamente
		And completé los campos de mi perfil con nombre "test", apellido "test", teléfono "123456789", dirección "calle falsa 123", foto "foto.jpg"
		When veo los datos de mi perfil
		Then veo mi nombre "test", apellido "test", teléfono "123456789", dirección "calle falsa 123", email "test@test.com" y foto "foto.jpg"

	Scenario: Consultar datos de mi perfil con campos parcialmenten cargados
		Given inicie sesión correctamente
		And completé los campos de mi perfil con nombre "test", apellido "test"
		When veo los datos de mi perfil
		Then veo mi nombre "test", apellido "test" y email "test@test.com"	

	Scenario: Consultar perfil de otro usuario
		Given el usuario con email "otrousuario@otro.com" modifico su perfil con nombre "test", apellido "test", teléfono "123456789", dirección "calle falsa 123", foto "foto.jpg"
		And inicie sesión correctamente
		When veo los datos del perfil del usuario con email otrousuario@otro.com
		Then veo su nombre "test", apellido "test", teléfono "123456789", dirección "calle falsa 123", email "otrousuario@otro.com" y foto "foto.jpg"
