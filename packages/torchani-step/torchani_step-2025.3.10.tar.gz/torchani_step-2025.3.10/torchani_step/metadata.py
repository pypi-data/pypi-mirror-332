# -*- coding: utf-8 -*-

"""This file contains metadata describing the results from TorchANI"""

metadata = {}

"""Description of the computational models for TorchANI.

Hamiltonians, approximations, and basis set or parameterizations,
only if appropriate for this code. For example::

    metadata["computational models"] = {
        "Hartree-Fock": {
            "models": {
                "PM7": {
                    "parameterizations": {
                        "PM7": {
                            "elements": "1-60,62-83",
                            "periodic": True,
                            "reactions": True,
                            "optimization": True,
                            "code": "mopac",
                        },
                        "PM7-TS": {
                            "elements": "1-60,62-83",
                            "periodic": True,
                            "reactions": True,
                            "optimization": False,
                            "code": "mopac",
                        },
                    },
                },
            },
        },
    }
"""
metadata["computational models"] = {
    "ML": {
        "models": {
            "ANI": {
                "parameterizations": {
                    "ANI-1x": {
                        "elements": "1,6-8",
                        "periodic": True,
                        "reactions": True,
                        "optimization": True,
                        "code": "torchani",
                    },
                    "ANI-1ccx": {
                        "elements": "1,6-8",
                        "periodic": True,
                        "reactions": True,
                        "optimization": True,
                        "code": "torchani",
                    },
                    "ANI-2x": {
                        "elements": "1,6-9,16-17",
                        "periodic": True,
                        "reactions": True,
                        "optimization": True,
                        "code": "torchani",
                    },
                },
            },
        },
    },
}

"""Description of the TorchANI keywords.

(Only needed if this code uses keywords)

Fields
------
description : str
    A human readable description of the keyword.
takes values : int (optional)
    Number of values the keyword takes. If missing the keyword takes no values.
default : str (optional)
    The default value(s) if the keyword takes values.
format : str (optional)
    How the keyword is formatted in the MOPAC input.

For example::
    metadata["keywords"] = {
        "0SCF": {
            "description": "Read in data, then stop",
        },
        "ALT_A": {
            "description": "In PDB files with alternative atoms, select atoms A",
            "takes values": 1,
            "default": "A",
            "format": "{}={}",
        },
    }
"""
# metadata["keywords"] = {
# }

"""Properties that TorchANI produces.
`metadata["results"]` describes the results that this step can produce. It is a
dictionary where the keys are the internal names of the results within this step, and
the values are a dictionary describing the result. For example::

    metadata["results"] = {
        "total_energy": {
            "calculation": [
                "energy",
                "optimization",
            ],
            "description": "The total energy",
            "dimensionality": "scalar",
            "methods": [
                "ccsd",
                "ccsd(t)",
                "dft",
                "hf",
            ],
            "property": "total energy#Psi4#{model}",
            "type": "float",
            "units": "E_h",
        },
    }

Fields
______

calculation : [str]
    Optional metadata describing what subtype of the step produces this result.
    The subtypes are completely arbitrary, but often they are types of calculations
    which is why this is name `calculation`. To use this, the step or a substep
    define `self._calculation` as a value. That value is used to select only the
    results with that value in this field.

description : str
    A human-readable description of the result.

dimensionality : str
    The dimensions of the data. The value can be "scalar" or an array definition
    of the form "[dim1, dim2,...]". Symmetric tringular matrices are denoted
    "triangular[n,n]". The dimensions can be integers, other scalar
    results, or standard parameters such as `n_atoms`. For example, '[3]',
    [3, n_atoms], or "triangular[n_aos, n_aos]".

methods : str
    Optional metadata like the `calculation` data. `methods` provides a second
    level of filtering, often used for the Hamiltionian for *ab initio* calculations
    where some properties may or may not be calculated depending on the type of
    theory.

property : str
    An optional definition of the property for storing this result. Must be one of
    the standard properties defined either in SEAMM or in this steps property
    metadata in `data/properties.csv`.

type : str
    The type of the data: string, integer, or float.

units : str
    Optional units for the result. If present, the value should be in these units.
"""
metadata["results"] = {
    "energy": {
        "calculation": [
            "energy",
            "optimization",
        ],
        "description": "The total energy",
        "dimensionality": "scalar",
        "property": "energy#TorchANI#{model}",
        "type": "float",
        "units": "E_h",
    },
    "gradients": {
        "calculation": [
            "energy",
            "optimization",
        ],
        "description": "gradients",
        "dimensionality": [3, "natoms"],
        "type": "float",
        "units": "E_h/a0",
        "format": ".6f",
    },
    "model": {
        "description": "The model string",
        "dimensionality": "scalar",
        "type": "string",
    },
    "N steps optimization": {
        "calculation": ["optimization"],
        "description": "number of optimization steps",
        "dimensionality": "scalar",
        "type": "integer",
    },
    "maximum force": {
        "calculation": ["optimization"],
        "description": "Maximum force on an atom",
        "dimensionality": "scalar",
        "type": "float",
        "units": "E_h/Å",
    },
    "RMS force": {
        "calculation": ["optimization"],
        "description": "RMS force on the atoms",
        "dimensionality": "scalar",
        "type": "float",
        "units": "E_h/Å",
    },
    "RMSD": {
        "calculation": ["optimization"],
        "description": "RMSD with H removed",
        "dimensionality": "scalar",
        "type": "float",
        "units": "Å",
    },
    "displaced atom": {
        "calculation": ["optimization"],
        "description": "Atom index with largest displacement",
        "dimensionality": "scalar",
        "type": "int",
        "units": "",
    },
    "maximum displacement": {
        "calculation": ["optimization"],
        "description": "Maximum displacement of an atom",
        "dimensionality": "scalar",
        "type": "float",
        "units": "Å",
    },
    "RMSD with H": {
        "calculation": ["optimization"],
        "description": "RMSD including H atoms",
        "dimensionality": "scalar",
        "type": "float",
        "units": "Å",
    },
    "displaced atom with H": {
        "calculation": ["optimization"],
        "description": "Atom index with largest displacement, including H",
        "dimensionality": "scalar",
        "type": "int",
        "units": "",
    },
    "maximum displacement with H": {
        "calculation": ["optimization"],
        "description": "Maximum displacement of an atom, including H",
        "dimensionality": "scalar",
        "type": "float",
        "units": "Å",
    },
}
