# HubSpot Discover

**HubSpot Discover** is a tool that extracts and analyzes the schemas and pipelines of HubSpot objects via the HubSpot API. The project automatically generates Python files containing constants for properties, pipelines, stages, and associations for each standard HubSpot object.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [HubSpotDiscover Generated Files Overview](#hubspotdiscover-generated-files-overview)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## Features

- **Schema Extraction**: Retrieve object properties and associations from HubSpot.
- **Pipeline Extraction**: Retrieve pipelines and stages for each HubSpot object.
- **Constant File Generation**: Automatically generate Python files with constants representing HubSpot object data.
- **CLI Access**: Use a command-line interface for a smooth and convenient experience.
- **Error Handling**: Displays descriptive error messages when API requests fail.

## Prerequisites

- **Python 3.8+**
- A valid HubSpot API key.
- An internet connection to access the HubSpot API.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging.

1. **Clone the repository:**

   ```bash
   git clone https://gitlab.com/dbm-01/hubspot-discover.git
   cd hubspot-discover

2. **Install dependencies with Poetry:**

   ```bash
    poetry install

## **Configuration**
    
Before running the tool, set your HubSpot API key as an environment variable. For example:

   ```bash
   export HS_API_KEY="your_hubspot_api_key"
```

By default, the CLI uses the environment variable `HS_API_KEY`. You can override this with the `--api_key_env` option when running the CLI.

## **Usage**

The project exposes a CLI command named `hsdiscover` defined in the `pyproject.toml` file. Once installed, you can run:

   ```bash
   hsdiscover --output_directory "./hs_constants" --api_key_env "HS_API_KEY" --custom-object '["name1","name2"]'
```

***Options:***

- `--output_directory` : The directory where the generated files will be saved (default: `./hs_constants`).
- `--api_key_env` : The name of the environment variable that stores your HubSpot API key (default: `HS_API_KEY`).
- `--custom-object` : A JSON string representing a list of custom objects to include in the analysis. If this option is not specified, only the standard objects will be processed.

Below is an example of how to use the hsdiscover CLI command:
```bash
    poetry run hsdiscover --output_directory "./hs_constants" --api_key_env "HS_API_KEY" --custom-object '["name1", "name2"]'
```
or in poetry shell:
```bash
    hsdiscover --output_directory "./hs_constants" --api_key_env "HS_API_KEY" --custom-object '["name1", "name2"]'
```
In this example:

- The generated files will be saved in the `./hs_constants` directory.
- The HubSpot API key is expected to be stored in the environment variable `HS_API_KEY`.
- The analysis will include two custom objects, `"name1"` and `"name2"`, in addition to the standard objects.

## **HubSpotDiscover Generated Files Overview**

- Overview :

    The `hsdiscover` tool generates a structured directory containing Python files with constants representing various aspects of HubSpot objects. This documentation explains the structure of the generated files.

- Generated Directory Structure :

    When running `hsdiscover`, the tool creates a directory for each HubSpot object type and populates it with specific files. The structure looks like this:

        ```bash
        output_directory/ 
        │── ObjectName/ 
        │ ├── associations.py
        │ ├── properties.py 
        │ ├── pipelines.py 
        │ ├── stages/ 
        │ │ ├── pipeline_name.py 
        │ ├── select/ 
        │ │ ├── property_name.py 
        │── associations.py 
        │── pipelines.py 
        │── stages.py
        ```
    - Associations (`associations.py`)

        Each `associations.py` file contains constants that define the **associations between objects** in HubSpot. These associations represent relationships between different entities, such as **Deals to Quotes** or **Deals to Payment Links**.

    
        Each association is defined by (the ASID_ prefix means association id):

        - A **unique association ID** (`ASID_<Object1>To<Object2>`)
        - The **originating object type ID** (`ASID_<Object1>To<Object2>_fromObjectTypeId`)
        - The **target object type ID** (`ASID_<Object1>To<Object2>_toObjectTypeId`)

    
        For the `Deal` object, the generated file might look like this:

        
        

        ```python
        # Associations for Deal
        ASID_QuoteToDeal = "64"
        ASID_QuoteToDeal_fromObjectTypeId = "0-14"
        ASID_QuoteToDeal_toObjectTypeId = "0-3"
        ASID_DealToPaymentLink = "474"
        ASID_DealToPaymentLink_fromObjectTypeId = "0-3"
        ASID_DealToPaymentLink_toObjectTypeId = "0-118"
        ```
    - Pipelines (`pipelines.py`)

        Each `pipelines.py` file contains constants that define the **pipelines associated with a HubSpot object**. Pipelines represent different workflows or sales processes that an **object** progresses through.

        Each pipeline is defined by (the `PID_` prefix means **Pipeline ID**):

        - **A set of pipeline ID constants (`PID_<object>_<PipelineName>`)**, mapping each **pipeline's unique identifier** to a HubSpot pipeline.
        - **A dictionary (`PID_<object>`)**, mapping each pipeline's ID to its label.

        For the `Deal` object, the generated file might look like this:

        ```python
        # GENERATED FILE DON'T UPDATE

        # Pipeline id for Deal
        PID_Deal_Pipeline1 = "default"
        PID_Deal_Pipeline2 = "175324523"
        PID_Deal_Pipeline3 = "175324523"
        # Pipelines labels for Deal
        PID_Deal = {
            "default": "Pipeline 1",
            "175324523": "Pipeline 2",
            "175324524": "Pipeline 3",
        }
        ```


    - Stages (`object/stages/pipeline_name.py`)

        Each file inside the `stages/` directory corresponds to a specific **pipeline** for an object. These files contain constants that define the **stages associated with a pipeline** in HubSpot.

        Each stage is defined by (the `PSID_` prefix means **Pipeline Stage ID**):

        - **A set of stage ID constants (`PSID_Contact_<pipeline>_<stage>`)**, mapping each **stage's unique identifier** to a constant.
        - **A dictionary (`PSID_<pipeline>_<stage>`)**, mapping each stage's identifier to its label.

        For the `Contact` object, the generated file for **Lifecycle Stage Pipeline** might look like this:

        ```python
        # GENERATED FILE - DO NOT UPDATE

        # Pipelines Contact/Lifecycle Stage Pipeline
        PSID_Contact_LifecycleStagePipeline_Subscriber = "subscriber"
        PSID_Contact_LifecycleStagePipeline_Lead = "lead"
        PSID_Contact_LifecycleStagePipeline_MarketingQualifiedLead = "marketingqualifiedlead"

        # Stages labels for Contact/Lifecycle Stage Pipeline
        PSID_Contact_LifecycleStagePipeline = {
            "subscriber": "Subscriber",
            "lead": "Lead",
            "marketingqualifiedlead": "Marketing Qualified Lead",
        }
        ```


    - Properties (`properties.py`)

        Each `properties.py` file contains constants that define the **properties associated with a HubSpot object**. These properties represent specific attributes of an object (such as a Deal's amount, age, or currency).

        Each property is defined by (the `FID_` prefix means **Field ID**):

        - **A set of property ID constants (`FID_<object>_<property>`)**, mapping each **property's internal name** to a constant.
        - **A dictionary (`FID_<object>`)**, mapping each property’s internal name to its label.

        For the `Deal` object, the generated file might look like this:

        ```python
        # GENERATED FILE - DO NOT UPDATE

        # Properties name for Deal
        FID_Deal_DealAge = "DealAge"
        FID_Deal_Amount = "amount"
        FID_Deal_AmountInCompanyCurrency = "amount_in_home_currency"

        # Properties labels for Deal
        FID_Deal = {
            "deal_age": "Deal age",
            "amount": "Amount",
            "amount_in_home_currency": "Amount in company currency"
        }
        ```


    - Select Field Values (`object/select/property_name.py`)

        Each file inside the `select/` directory corresponds to a **specific property** that has predefined selectable values (e.g., dropdown fields in HubSpot). These files contain constants that define the **valid options available for that property**.

        Each select field is defined by (the `SFID_` prefix means **Select Field ID**):

        - **A set of select value ID constants (`SFID_<object>_<property_name>_<value_name>`)**, mapping each **option's internal identifier** to a constant.
        - **A dictionary (`SFID_<object>_<property_name>`)**, mapping each option’s identifier to its label.

        For the `Deal` object, the generated file for **hs_manual_forecast_category** might look like this:

        ```python
        # GENERATED FILE - DO NOT UPDATE

        # Select field values for Deal / hs_manual_forecast_category
        SFID_Deal_ForecastCategory_NotForecasted = "OMIT"
        SFID_Deal_ForecastCategory_Pipeline = "PIPELINE"
        SFID_Deal_ForecastCategory_BestCase = "BEST_CASE"
        SFID_Deal_ForecastCategory_Commit = "COMMIT"
        SFID_Deal_ForecastCategory_ClosedWon = "CLOSED"

        # Select field labels for Deal / hs_manual_forecast_category
        SFID_Deal_HsManualForecastCategory = {
            "OMIT": "Not forecasted",
            "PIPELINE": "Pipeline",
            "BEST_CASE": "Best case",
            "COMMIT": "Commit",
            "CLOSED": "Closed won",
        }
        ```

    - Global

        In addition to object-specific associations / pipelines / stages files :
        - a global associations.py file is generated at the root level. This file contains a dictionary mapping association IDs to their labels for all objects.
        - a global pipelines.py file is generated at the root level. This file contains a dictionary mapping pipeline IDs to their labels for all objects.
        - a global stages.py file is generated at the root level. This file contains a dictionary mapping stage IDs to their labels for all objects.




## **Project structure**

- `discover.py`, contains functions that:
    - Extract property schemas and associations.
    - Extract pipeline schemas and stages.
    - Generate constant files with the retrieved data.
- `hubspot.py`, provides functions to query the HubSpot API:
    - getSchema(): Retrieves the schema (properties and associations) for a given object type.
    - getPipelines(): Retrieves pipelines and stages for a given object type.
- `cli.py` : implements the command-line interface, parsing arguments and triggering the discovery process.
- `pyproject.toml` : Configuration file for Poetry, defining project metadata, dependencies, and the CLI script entry point.

Additional utility modules (for file handling, string manipulation, API requests, and constants) are located within the hubspot_discover/hubspot_discover/tools package.


## License

MIT License

Copyright (c) [2025] [David BRAHIM]

---

## Contact

Open an issue to get help or suggest improvements.