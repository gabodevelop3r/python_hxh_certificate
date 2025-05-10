# app/application/services/certificates/create_certificate_service.py

def create_certificate_service(certificate_data: dict) -> dict:
    """
    Servicio para crear un nuevo certificado. Aquí podrías guardar en una base de datos.
    """
    # Simulamos la creación de un certificado, normalmente se guardaría en la base de datos
    new_certificate = {
        "id": 3,  # Asignamos un ID ficticio
        "name": certificate_data["name"],
        "date": certificate_data["date"]
    }
    return new_certificate
