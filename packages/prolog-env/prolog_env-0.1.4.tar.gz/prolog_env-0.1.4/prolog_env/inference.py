import traceback
import janus_swi as janus
try:
    import transformers
except ImportError:
    import sys
    sys.exit("The 'transformers' is not installed. Please manual install or "
             "run `pip install prolog-env[toolbox]` to enable this feature.")

def prolog_add_rules(id: str, code: str) -> str:
    """Add rules to the prolog database.

    Args:
        id: The id of the rule.
        code: The code of the rule.

    Returns:
        str: The traceback if an error occurred, otherwise None.
    """
    try:
        janus.consult(id, code)
    except:
        return traceback.format_exc()


def prolog_query(code: str) -> str:
    """Query the prolog database.

    Args:
        code: The code to query.

    Returns:
        str: The result of the query, or the traceback if an error occurred.
    """
    try:
        return str(list(janus.query(code)))
    except:
        return traceback.format_exc()


prolog_toolbox = transformers.Toolbox(
    [
        transformers.tool(prolog_add_rules),
        transformers.tool(prolog_query),
    ]
)