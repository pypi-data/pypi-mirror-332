"""This module implements an angry expression and a listening expression.
"""
from typing import Dict

from misty2py.basic_skills.expression import expression
from misty2py.robot import Misty
from misty2py.utils.utils import get_misty


def angry_expression(misty: Misty) -> Dict:
    """Misty expresses anger.

    Args:
        misty (Misty): The Misty to perform the expression.

    Returns:
        Dict: The dictionary with `"overall_success"` key (bool) and keys for every action performed (dictionarised Misty2pyResponse).
    """
    return expression(
        misty,
        image="image_anger",
        sound="sound_anger_1",
        colours={"col1": "red_light", "col2": "orange_light", "time": 200},
        colour_type="trans",
        colour_offset=0.5,
        duration=2,
    )


def listening_expression(misty: Misty) -> Dict:
    """Misty expresses that she is listening.

    Args:
        misty (Misty): The Misty to perform the expression.

    Returns:
        Dict: The dictionary with `"overall_success"` key (bool) and keys for every action performed (dictionarised Misty2pyResponse).
    """
    return expression(
        misty,
        colour="azure_light",
        sound="sound_wake",
    )


if __name__ == "__main__":
    print(angry_expression(get_misty()))
    print(listening_expression(get_misty()))
