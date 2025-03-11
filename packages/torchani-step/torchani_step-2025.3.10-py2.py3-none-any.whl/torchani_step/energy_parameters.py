# -*- coding: utf-8 -*-
"""
Control parameters for the Energy step in a SEAMM flowchart
"""

import logging
import seamm
import pprint  # noqa: F401

logger = logging.getLogger(__name__)


class EnergyParameters(seamm.Parameters):
    """
    The control parameters for Energy.

    You need to replace the "time" entry in dictionary below these comments with the
    definitions of parameters to control this step. The keys are parameters for the
    current plugin,the values are dictionaries as outlined below.

    Examples
    --------
    ::

        parameters = {
            "time": {
                "default": 100.0,
                "kind": "float",
                "default_units": "ps",
                "enumeration": tuple(),
                "format_string": ".1f",
                "description": "Simulation time:",
                "help_text": ("The time to simulate in the dynamics run.")
            },
        }

    parameters : {str: {str: str}}
        A dictionary containing the parameters for the current step.
        Each key of the dictionary is a dictionary that contains the
        the following keys:

    parameters["default"] :
        The default value of the parameter, used to reset it.

    parameters["kind"] : enum()
        Specifies the kind of a variable. One of  "integer", "float", "string",
        "boolean", or "enum"

        While the "kind" of a variable might be a numeric value, it may still have
        enumerated custom values meaningful to the user. For instance, if the parameter
        is a convergence criterion for an optimizer, custom values like "normal",
        "precise", etc, might be adequate. In addition, any parameter can be set to a
        variable of expression, indicated by having "$" as the first character in the
        field. For example, $OPTIMIZER_CONV.

    parameters["default_units"] : str
        The default units, used for resetting the value.

    parameters["enumeration"]: tuple
        A tuple of enumerated values.

    parameters["format_string"]: str
        A format string for "pretty" output.

    parameters["description"]: str
        A short string used as a prompt in the GUI.

    parameters["help_text"]: str
        A longer string to display as help for the user.

    See Also
    --------
    Energy, TkEnergy, Energy EnergyParameters, EnergyStep
    """

    parameters = {
        "model": {
            "default": "ANI-2x",
            "kind": "enum",
            "default_units": "",
            "enumeration": ("ANI-1x", "ANI-1ccx", "ANI-2x"),
            "format_string": "",
            "description": "ANI Model:",
            "help_text": "Which of the ANI machine-learning models to use.",
        },
        "submodel": {
            "default": "all",
            "kind": "string",
            "default_units": "",
            "enumeration": ("all",),
            "format_string": "",
            "description": "Submodels:",
            "help_text": (
                "Which of the submodels to use, averaging over the set.\n"
                " May be 'all', a single integer 1-8, or a list with ranges, e.g."
                " '1, 3, 5-8'."
            ),
        },
        "gradients": {
            "default": "yes",
            "kind": "boolean",
            "default_units": "",
            "enumeration": ("yes", "no"),
            "format_string": "",
            "description": "Calculate gradients:",
            "help_text": "Whether to calculate and return the gradients",
        },
        # Results handling ... uncomment if needed
        "results": {
            "default": {},
            "kind": "dictionary",
            "default_units": "",
            "enumeration": tuple(),
            "format_string": "",
            "description": "results",
            "help_text": "The results to save to variables or in tables.",
        },
    }

    def __init__(self, defaults={}, data=None):
        """
        Initialize the parameters, by default with the parameters defined above

        Parameters
        ----------
        defaults: dict
            A dictionary of parameters to initialize. The parameters
            above are used first and any given will override/add to them.
        data: dict
            A dictionary of keys and a subdictionary with value and units
            for updating the current, default values.

        Returns
        -------
        None
        """

        logger.debug("EnergyParameters.__init__")

        super().__init__(
            defaults={**EnergyParameters.parameters, **defaults}, data=data
        )
