"""Automatic pyfai integration for every scan with saving and plotting"""

from typing import Optional
from ..xrpd.processor import XrpdProcessor
from ..persistent.parameters import ParameterInfo

try:
    from bliss import setup_globals
except ImportError:
    setup_globals = None


class BM23XrpdProcessor(
    XrpdProcessor,
    parameters=[
        ParameterInfo("pyfai_config", category="PyFai"),
        ParameterInfo("integration_options", category="PyFai"),
    ],
):
    def __init__(self, **defaults) -> None:
        if setup_globals is None:
            raise ImportError("requires a bliss session")
        defaults.setdefault(
            "integration_options",
            {
                "method": "no_csr_ocl_gpu",
                "nbpt_rad": 4096,
                "unit": "q_nm^-1",
            },
        )
        super().__init__(**defaults)

    def get_config_filename(self, lima_name: str) -> Optional[str]:
        return self.pyfai_config

    def get_integration_options(self, lima_name: str) -> Optional[dict]:
        integration_options = self.integration_options
        if integration_options:
            return integration_options.to_dict()
        return None
