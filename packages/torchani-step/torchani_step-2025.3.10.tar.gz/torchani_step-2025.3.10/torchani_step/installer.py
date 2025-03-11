# -*- coding: utf-8 -*-

"""Installer for the TorchANI plug-in.

This handles any further installation needed after installing the Python
package `torchani-step`.
"""

import logging
from pathlib import Path
import pkg_resources
import subprocess

import seamm_installer

logger = logging.getLogger(__name__)


class Installer(seamm_installer.InstallerBase):
    """Handle further installation needed after installing torchani-step.

    The Python package `torchani-step` should already be installed, using `pip`,
    `conda`, or similar. This plug-in-specific installer then checks for the
    TorchANI script, installing it if needed, and registers its
    location in seamm.ini.

    1. The correct executables are already available.
        1. If they are already registered in `seamm.ini` there is nothing else
           to do.
        2. They may be in the current path, in which case they need to be added
           to `seamm.ini`.
        3. If a module system is in use, a module may need to be loaded to give
           access to Dftbplus.
        4. They cannot be found automatically, so the user needs to locate the
           executables for the installer.

    2. TorchANI is not installed on the machine. In this case they can be
       installed in a Conda environment. There is one choice:

        1. They can be installed in a separate environment, `seamm-torchani` by
           default.
    """

    def __init__(self, logger=logger):
        # Call the base class initialization, which sets up the commandline
        # parser, amongst other things.
        super().__init__(logger=logger)

        logger.debug("Initializing the TorchANI installer object.")

        self.environment = "seamm-dftbplus"
        self.section = "torchani-step"
        self.path_name = "torchani-path"
        self.executables = ["SEAMM_TorchANI.py"]
        self.resource_path = Path(pkg_resources.resource_filename(__name__, "data/"))

        # What Conda environment is the default?
        data = self.configuration.get_values(self.section)
        if "conda-environment" in data and data["conda-environment"] != "":
            self.environment = data["conda-environment"]
        else:
            self.environment = "seamm-torchani"

        # The environment.yaml file for Conda installations.
        path = Path(pkg_resources.resource_filename(__name__, "data/"))
        logger.debug(f"data directory: {path}")
        self.environment_file = path / "seamm-torchani.yml"

    def install(self):
        """Install then conda environment and the Python executable."""
        super().install()

        bin_path = self.conda.path(self.environment) / "bin"
        path = bin_path / "python"
        local_path = self.resource_path

        # Copy the python file, adjusting the python path
        lines = (local_path / "SEAMM_TorchANI.py_template").read_text().splitlines()
        lines[0] = f"#!{path}"

        new_path = bin_path / "SEAMM_TorchANI.py"
        new_path.write_text("\n".join(lines))
        new_path.chmod(0o755)

    def exe_version(self, path):
        """Get the version of the TorchANI executable.

        Parameters
        ----------
        path : pathlib.Path
            Path to the executable.

        Returns
        -------
        str
            The version reported by the executable, or 'unknown'.
        """
        try:
            result = subprocess.run(
                [str(path), "--version"],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
            )
        except Exception:
            version = "unknown"
        else:
            version = "unknown"
            tmp = result.stdout.splitlines()[0].split()
            version = tmp[-1]

        return version
