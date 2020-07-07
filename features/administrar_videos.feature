Feature: Administrar videos

	Scenario: Ver videos
		Given se crearon 5 videos
		When veo los videos
		Then veo que hay 5 videos

	Scenario: Deshabilitar video
		Given se crearon 1 videos
		When deshabilito el video
		Then veo que le video esta deshabilitado

	Scenario: Habilitar video
		Given hay un video deshabilitado
		When habilito el video
		Then veo que el video esta habilitado

	Scenario: Muro de videos solo muestra habilitados
		Given se crearon 5 videos
		And se deshabilito 1 video
		When obtengo el muro de videos
		Then veo que hay 4 videos
