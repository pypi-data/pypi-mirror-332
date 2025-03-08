import re
import unicodedata
import json


def remove_accents(text: str) -> str:
    """
    Removes accents from the input text using Unicode normalization (NFKD).
    """
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(char for char in normalized if not unicodedata.combining(char))


def build_pseudo_snake_case_identifier(prefix: str, items: list) -> str:
    """
    Builds a (pseudo) snake_case identifier from a prefix and a list of items.


    The items in the list must be strings that comply with Python's variable naming rules.


    :param prefix: The starting string.
    :param items: A list of valid string elements.
    :return: A snake_case formatted string.
    """
    return prefix + "_" + "_".join(items)


def to_camel_case(text: str, custom_replacements: dict = None) -> str:
    """
    Converts a string into a Python variable name in camelCase.


    The function applies the following rules:
      - Accented characters are replaced by their non-accented equivalents.
      - Comparison operators (>=, <=, !=, <>, ==, =, >, <) are replaced with their
        textual equivalents (by default:
        'GreaterThanOrEqual', 'LessThanOrEqual', 'NotEqual', 'NotEqual', 'Equal', 'Equal', 'GreaterThan', 'LessThan').
      - The '@' character is replaced by 'At'.


    The default replacements are always applied. If a custom_replacements dictionary
    is provided, it is merged with the defaults: common keys are overridden by the custom values,
    and new keys are added.


    **Important :** When building the camelCase string, if a token exactly matches one of the
    replacement values, its case is preserved. Otherwise, the token is transformed so that its
    first letter is upper-cased (for non-first tokens) and the rest is lower-cased.


    Example:
        "a < b and c>=d" with a custom replacement for '>=' mapping to 'GreaterOrEqual'
        produces: "aLtBAndCGreaterOrEqualD"
    """
    # Step 1: Remove accents.
    text = remove_accents(text)

    # Step 2: Default replacements.
    default_replacements = {
        ">=": "GreaterThanOrEqual",
        "<=": "LessThanOrEqual",
        "!=": "NotEqual",
        "<>": "NotEqual",
        "==": "Equal",
        "=": "Equal",
        ">": "GreaterThan",
        "<": "LessThan",
        "@": "At",
    }

    # Step 3: Merge custom and default replacements (custom values override default ones).
    if custom_replacements:
        replacements = {**default_replacements, **custom_replacements}
    else:
        replacements = default_replacements

    # To identify tokens resulting from a replacement and preserve their case,
    # we save the replacement values in a set.
    replacement_values = set(replacements.values())

    # Step 4: Apply replacements.
    # On trie les clés par longueur décroissante pour traiter d'abord les séquences multi-caractères.
    for key in sorted(replacements, key=len, reverse=True):
        pattern = re.escape(key)
        # On insère des espaces autour du remplacement afin d'isoler le token.
        replacement_str = f" {replacements[key]} "
        text = re.sub(pattern, replacement_str, text)

    # Step 5: Split the text into words using non-alphanumeric characters as delimiters.
    words = re.split(r"[^A-Za-z0-9]+", text)
    words = [word for word in words if word]  # Remove empty tokens.

    if not words:
        return ""

    # Step 6: Build the camelCase result.
    result_tokens = []
    # The first token is entirely lower-cased.
    # result_tokens.append(words[0].lower())
    # For each subsequent token:
    for token in words:
        # If the token matches one of the replacement values, preserve its casing.
        if token in replacement_values:
            result_tokens.append(token)
        else:
            # Otherwise, capitalize only the first letter and lowercase the rest.
            result_tokens.append(token[0].upper() + token[1:].lower())

    return "".join(result_tokens)


def to_snake_case(text: str, custom_replacements: dict = None) -> str:
    """
    Converts a string into a Python variable name in snake_case.

    The function applies the following rules:
      - Accented characters are replaced by their non-accented equivalents.
      - Comparison operators (>=, <=, !=, <>, ==, =, >, <) are replaced with their
        textual equivalents (by default:
        'GreaterThanOrEqual', 'LessThanOrEqual', 'NotEqual', 'NotEqual', 'Equal', 'Equal', 'GreaterThan', 'LessThan').
      - The '@' character is replaced by 'At'.

    The default replacements are always applied. If a custom_replacements dictionary
    is provided, it is merged with the defaults: common keys are overridden by the custom values,
    and new keys are added.

    **Important:** When building the snake_case string, if a token exactly matches one of the
    replacement values, its case is modified by removing the substring "Or" (if present) and converting
    the result to lower-case. Otherwise, the token is simply converted to lower-case.

    Example:
        "a < b and c>=d" with a custom replacement for '>=' mapping to 'GreaterOrEqual'
        produces: "a_lt_b_and_c_greaterthanequal_d"
    """
    # Step 1: Remove accents.
    text = remove_accents(text)

    # Step 2: Define default replacements.
    default_replacements = {
        ">=": "GreaterThanOrEqual",
        "<=": "LessThanOrEqual",
        "!=": "NotEqual",
        "<>": "NotEqual",
        "==": "Equal",
        "=": "Equal",
        ">": "GreaterThan",
        "<": "LessThan",
        "@": "At",
    }

    # Step 3: Merge custom replacements with defaults (custom values override defaults).
    if custom_replacements:
        replacements = {**default_replacements, **custom_replacements}
    else:
        replacements = default_replacements

    # Save the replacement values to identify tokens that result from a replacement.
    replacement_values = set(replacements.values())

    # Step 4: Apply replacements.
    # Sort keys by descending length to handle multi-character sequences first.
    for key in sorted(replacements, key=len, reverse=True):
        pattern = re.escape(key)
        # Surround the replacement with spaces to isolate the token.
        replacement_str = f" {replacements[key]} "
        text = re.sub(pattern, replacement_str, text)

    # Step 5: Split the text into words using non-alphanumeric characters as delimiters.
    words = re.split(r"[^A-Za-z0-9]+", text)
    words = [word for word in words if word]  # Remove empty tokens.

    if not words:
        return ""

    # Step 6: Build the snake_case result.
    result_tokens = []
    for token in words:
        if token in replacement_values:
            # For replacement tokens, remove the substring "Or" (if present) and convert to lower-case.
            token = token.replace("Or", "").lower()
        else:
            token = token.lower()
        result_tokens.append(token)

    return "_".join(result_tokens)


def build_constant(prefix: str, items: list, value: str, suffix: str = None):
    constant_value = json.dumps(value) if type(value) is dict else f'"{value}"'
    return f'{build_pseudo_snake_case_identifier(prefix=prefix,items=list(map(to_camel_case , items)))}{"_"+suffix if suffix else ""}= {constant_value} '
