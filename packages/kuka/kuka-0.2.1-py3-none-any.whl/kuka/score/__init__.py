'''FUNCTIONS THAT RETURN THE PERFORMANCE OF MODELS BY A TABLE/LIST...'''
from .regression import display_score
from .regression import predictions_separate_by_a_variable

from .categorization import classification_metrics

__all__ = [
    #regression:
    'display_score',
    'predictions_separate_by_a_variable',
    #categorization:
    'classification_metrics',
]