import argparse
import json
from hubspot_discover.hubspot_discover.discover import discover


def main():
    parser = argparse.ArgumentParser(description="Discover all Hubspot objects.")
    parser.add_argument(
        "--output_directory",
        type=str,
        default="./hs_constants",
        help="The directory where processed files will be saved (default: ./hs_constants).",
    )
    parser.add_argument(
        "--api_key_env",
        type=str,
        default="HS_API_KEY",
        help="The maximum depth for analyzing imports in each file (default: HS_API_KEY).",
    )

    parser.add_argument(
        "--custom-object",
        type=str,
        default="[]",
        help='A JSON-formatted list of custom object names (e.g., \'["name_1", "name_2", "name_3"]\').',
    )

    args = parser.parse_args()

    # Convert --custom-object from string to list
    try:
        custom_object = json.loads(args.custom_object)
        custom_object = list(map("p_".__add__, custom_object))

        if not isinstance(custom_object, list):
            raise ValueError(
                "The --custom-object argument must be a JSON-formatted list."
            )
    except json.JSONDecodeError:
        print(
            'Error: --custom-object must be a valid JSON-formatted list (e.g., \'["name1", "name2", "name3"]\').'
        )
        return

    try:
        discover(
            output_directory=args.output_directory,
            custom_object=custom_object,
            api_key_env=args.api_key_env,
        )
    except FileNotFoundError as e:
        # logger.error(e)
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        # logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
