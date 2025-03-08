from hubspot_discover.hubspot_discover.tools.requests import rate_request
from hubspot_discover.hubspot_discover.tools.default import URL_BASE

GET_SCHEMA_URL = URL_BASE + "/crm-object-schemas/v3/schemas/{object_type}"
GET_ALL_PIPELINE_URL = URL_BASE + "/crm/v3/pipelines/{object_type}"


def getSchema(object_type: str, headers: dict):
    schema_response = rate_request(
        "GET", url=GET_SCHEMA_URL.format(object_type=object_type), headers=headers
    )
    if not schema_response.status_code == 200:
        raise Exception(
            f"**Erreur lors de la récupération du schema {object_type} : {schema_response.status_code}, {schema_response.text}"
        )
    return schema_response.json()


def getPipelines(object_type: str, headers: dict):

    pipeline_response = rate_request(
        "GET", url=GET_ALL_PIPELINE_URL.format(object_type=object_type), headers=headers
    )
    if not pipeline_response.status_code == 200:
        raise Exception(
            f"**Erreur lors de la récupération des pipelines {object_type} : {pipeline_response.status_code}, {pipeline_response.text}"
        )
    return pipeline_response.json()
