Feature: Contactos
    
    Background: Estoy logueado y existe el usuario "edson"
        Given inicie sesión correctamente
        And "edson" se registró correctamente

    Scenario: Recibir solicitud de contacto
        Given "edson" me mandó solicitud de contacto
        When veo mis solicitudes de contacto
        Then veo que "edson" me mandó solicitud de contacto
    
    Scenario: Recibir solicitud de contacto (perfil)
        Given "edson" me mandó solicitud de contacto
        When veo el perfil de "edson"
        Then veo que su solicitud de contacto está pendiente de aprobación
    
    Scenario: Enviar solicitud de contacto
        Given le mandé solicitud de contacto a "edson"
        When veo el perfil de "edson"
        Then veo que mi solicitud de contacto está pendiente de aprobación
    
    Scenario: Aceptar solicitud de contacto
        Given "edson" me mandó solicitud de contacto
        When acepto la solicitud de contacto
        And veo el perfil de "edson"
        Then veo que es mi contacto
    
    Scenario: Rechazar solicitud de contacto
        Given "edson" me mandó solicitud de contacto
        When rechazo la solicitud
        And veo el perfil de "edson"
        Then veo que no es mi contacto y que no hay solicitud pendiente
    
    Scenario: Ver mis contactos
        Given "edson" es mi contacto
        When veo mis contactos
        Then veo que mis contactos son "edson"
