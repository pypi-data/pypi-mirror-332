from datetime import (
    date,
)
from typing import (
    Optional,
)
from smev_services.utils.domain.model import (
    BaseModel,
)


class Passport(BaseModel):

    """Данные паспорта гражданина РФ."""

    series: str
    number: str
    issue_date: date
    issuer: str
    issuer_code: Optional[str]


class Participant(BaseModel):

    """Данные по участнику."""

    lastname: str
    firstname: str
    date_of_birth: date
    birth_place: str
    snils: Optional[str] = None
    middlename: Optional[str] = None
    passport: Optional[Passport] = None
    unit_ogrn: Optional[str] = None
    unit_name: Optional[str] = None
    unit_region_code: Optional[str] = None


class DiedParticipant(BaseModel):

    """Данные по умершему участнику."""

    lastname: str
    firstname: str
    date_of_birth: date
    birth_place: str
    snils: Optional[str] = None
    middlename: Optional[str] = None
    passport: Optional[Passport] = None
    unit_ogrn: Optional[str] = None
    unit_name: Optional[str] = None
    unit_region_code: Optional[str] = None


class ParticipantType(BaseModel):

    """Данные по типу учасника."""

    participant: Optional[Participant] = None
    died_participant: Optional[DiedParticipant] = None


class ServiceInfo(BaseModel):

    """Служебная информация."""

    current_date: date
    order_status_code: str
    target_id: str
    target_name: str


class DoDCertificateRequest(BaseModel):

    """Корневые данные запроса."""

    service_info: ServiceInfo
    participant_type: ParticipantType
    oktmo: str