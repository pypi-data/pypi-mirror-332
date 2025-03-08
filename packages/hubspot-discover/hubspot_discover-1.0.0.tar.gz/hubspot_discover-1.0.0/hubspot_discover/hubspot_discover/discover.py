import os
import json
from hubspot_discover.hubspot_discover.tools.default import (
    STANDARD_HUBSPOT_OBJECT,
    OBJECT_PREFIX,
)
from hubspot_discover.hubspot_discover.tools.requests import rate_request
from hubspot_discover.hubspot_discover.tools.string import (
    build_constant,
    to_snake_case,
    to_camel_case,
)
from hubspot_discover.hubspot_discover.tools.file import create_file
from hubspot_discover.hubspot_discover.tools.hubspot import getSchema, getPipelines
import time


def analyze_property_schema(object_types: list):

    result = []
    field_dict = {}
    object_property_constant = []

    for object_type in object_types:
        try:
            print(f"\n==> Get properties :{object_type}", end="")
            properties_schemas = getSchema(object_type=object_type, headers=headers)[
                "properties"
            ]
            object_property_constant = []
            field_dict = {}
            for property in properties_schemas:
                field_dict[property["name"]] = property["label"]

                object_property_constant.append(
                    build_constant(
                        prefix=OBJECT_PREFIX["FIELD_ID"],
                        items=[object_type, property["label"]],
                        value=property["name"],
                    )
                )

                if property["fieldType"] == "select":
                    if len(property["options"]) > 0:
                        select_dict = {}
                        object_select_property_constant = []
                        for option in property["options"]:
                            select_dict[option["value"]] = option["label"]

                            object_select_property_constant.append(
                                build_constant(
                                    prefix=OBJECT_PREFIX["SELECT_FIELD_ID"],
                                    items=[
                                        object_type,
                                        property["label"],
                                        option["label"],
                                    ],
                                    value=option["value"],
                                )
                            )

                        result.append(
                            {
                                "directory": f"{to_snake_case(object_type)}/select",
                                "filename": f"{to_snake_case(property['name'])}.py",
                                "content": [
                                    "# GENERATED FILE DON'T UPDATE\n",
                                    f"\n# Select field values for {object_type} / {property['name']}\n",
                                    "\n".join(object_select_property_constant),
                                    f"\n\n# Select field labels for {object_type} / {property['name']}\n",
                                    f"\n{OBJECT_PREFIX['SELECT_FIELD_ID']}_{to_camel_case(object_type)}_{to_camel_case(property['name'])} = "
                                    + json.dumps(select_dict),
                                ],
                            }
                        )

            result.append(
                {
                    "directory": f"{to_snake_case(object_type)}",
                    "filename": "properties.py",
                    "content": [
                        "# GENERATED FILE DON'T UPDATE\n",
                        f"\n# Properties name for {object_type}\n",
                        "\n".join(object_property_constant),
                        f"\n\n# Properties labels for {object_type}",
                        f"\n{OBJECT_PREFIX['FIELD_ID']}_{to_camel_case(object_type)} = "
                        + json.dumps(field_dict),
                    ],
                }
            )

            print(f"\033[32m .... ok \033[0m")
        except Exception as ex:
            print(f"\n\033[31mError :\033[0m {str(ex)}")

    return result


def analyze_pipeline_schema(object_types: list):
    all_pipeline_dict = {}
    all_stage_dict = {}
    result = []
    for object_type in object_types:
        try:
            print(f"\n==> Get pipeline :{object_type}", end="")
            pipeline_schemas = getPipelines(object_type=object_type, headers=headers)

            object_pipeline_constant = []
            pipeline_dict = {}
            for pipeline in pipeline_schemas["results"]:
                all_pipeline_dict[pipeline["id"]] = pipeline["label"]
                pipeline_dict[pipeline["id"]] = pipeline["label"]

                object_pipeline_constant.append(
                    build_constant(
                        prefix=OBJECT_PREFIX["PIPELINE_ID"],
                        items=[object_type, pipeline["label"]],
                        value=pipeline["id"],
                    )
                )
                stage_dict = {}
                stage_constant = []

                for stage in pipeline["stages"]:
                    stage_dict[stage["id"]] = stage["label"]
                    all_stage_dict[stage["id"]] = stage["label"]
                    # Add stage to constant
                    stage_constant.append(
                        build_constant(
                            prefix=OBJECT_PREFIX["PIPELINE_STAGE_ID"],
                            items=[object_type, pipeline["label"], stage["label"]],
                            value=stage["id"],
                        )
                    )

                result.append(
                    {
                        "directory": f"{to_snake_case(object_type)}/stages",
                        "filename": f"{to_snake_case(pipeline['label'])}.py",
                        "content": [
                            "# GENERATED FILE DON'T UPDATE\n",
                            f"\n# Pipelines {object_type}/{pipeline['label']}\n",
                            "\n".join(stage_constant),
                            f"\n\n# Stages labels for {object_type}/{pipeline['label']}\n",
                            build_constant(
                                prefix=OBJECT_PREFIX["PIPELINE_STAGE_ID"],
                                items=[object_type, pipeline["label"]],
                                value=stage_dict,
                            ),
                        ],
                    }
                )

            result.append(
                {
                    "directory": f"{to_snake_case(object_type)}",
                    "filename": "pipelines.py",
                    "content": [
                        "# GENERATED FILE DON'T UPDATE\n",
                        f"\n# Pipeline id for {object_type}\n",
                        "\n".join(object_pipeline_constant),
                        f"\n\n# Pipelines labels for {object_type}",
                        f"\n{OBJECT_PREFIX['PIPELINE_ID']}_{to_camel_case(object_type)} = "
                        + json.dumps(pipeline_dict),
                    ],
                }
            )
            print(f"\033[32m .... ok \033[0m")
        except Exception as ex:
            print(f"\n\033[31mError :\033[0m {str(ex)}")

        # Add association dictionnary

    result.append(
        {
            "directory": ".",
            "filename": "pipelines.py",
            "content": [
                "# GENERATED FILE DON'T UPDATE\n",
                "\n\n# All Pipelines",
                f"\n{OBJECT_PREFIX['PIPELINE_ID']} = " + json.dumps(all_pipeline_dict),
            ],
        }
    )
    result.append(
        {
            "directory": ".",
            "filename": "stages.py",
            "content": [
                "# GENERATED FILE DON'T UPDATE\n",
                "\n\n# Stages for all pipelines",
                f"\n{OBJECT_PREFIX['PIPELINE_STAGE_ID']} ="
                + json.dumps(all_stage_dict),
            ],
        }
    )

    return result


def analyze_association_schema(object_types: list):
    association_dict = {}
    result = []

    for object_type in object_types:

        associations = {}
        association_constant = []
        try:
            print(f"\n==> Get association :{object_type}", end="")
            association_schemas = getSchema(object_type=object_type, headers=headers)[
                "associations"
            ]

            for association_schema in association_schemas:
                associations[association_schema["name"]] = {
                    "id": association_schema["id"],
                    "fromObjectTypeId": association_schema["fromObjectTypeId"],
                    "toObjectTypeId": association_schema["toObjectTypeId"],
                }

            for key, value in associations.items():

                association_constant.append(
                    build_constant(
                        prefix=OBJECT_PREFIX["ASSOCIATION_ID"],
                        items=[key],
                        value=value["id"],
                    )
                )
                association_constant.append(
                    build_constant(
                        prefix=OBJECT_PREFIX["ASSOCIATION_ID"],
                        items=[key],
                        value=value["fromObjectTypeId"],
                        suffix="fromObjectTypeId",
                    )
                )

                association_constant.append(
                    build_constant(
                        prefix=OBJECT_PREFIX["ASSOCIATION_ID"],
                        items=[key],
                        value=value["toObjectTypeId"],
                        suffix="toObjectTypeId",
                    )
                )

                association_dict[value["id"]] = key

            result.append(
                {
                    "directory": f"{to_snake_case(object_type)}",
                    "filename": "associations.py",
                    "content": [
                        "# GENERATED FILE DON'T UPDATE\n",
                        f"\n# Assocations {object_type}\n",
                        "\n".join(association_constant),
                    ],
                }
            )
            print(f"\033[32m .... ok \033[0m")
        except Exception as ex:
            print(f"\n\033[31mError :\033[0m {str(ex)}")

    # Add association dictionnary
    result.append(
        {
            "directory": ".",
            "filename": "associations.py",
            "content": [
                "# GENERATED FILE DON'T UPDATE\n",
                "\n\n# Assocations",
                "\nassociation_id_to_label = " + json.dumps(association_dict),
            ],
        }
    )
    return result


def create_analyze_file(root_directory: str, analyze: list):
    for item in analyze:
        create_file(
            file_path=f"{root_directory}/{item['directory']}/{item['filename']}",
            contents=item["content"],
        )


def discover(output_directory: str, custom_object: list, api_key_env: str):
    global ROOT, API_KEY, headers

    ROOT = output_directory
    # Get API key
    API_KEY = os.getenv(api_key_env)
    # API headers
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    create_analyze_file(
        root_directory=ROOT,
        analyze=analyze_association_schema(
            object_types=STANDARD_HUBSPOT_OBJECT + custom_object
        ),
    )

    create_analyze_file(
        root_directory=ROOT,
        analyze=analyze_pipeline_schema(
            object_types=STANDARD_HUBSPOT_OBJECT + custom_object
        ),
    )

    create_analyze_file(
        root_directory=ROOT,
        analyze=analyze_property_schema(
            object_types=STANDARD_HUBSPOT_OBJECT + custom_object
        ),
    )
