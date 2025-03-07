from ._id31_utils import ensure_difflab6_id31_flats
from ._streamline_utils import DemoStreamlineScannerMixIn
from ..id31.streamline_scanner import Id31StreamlineScanner

try:
    from bliss import setup_globals
except ImportError:
    setup_globals = None


class DemoStreamlineScanner(DemoStreamlineScannerMixIn, Id31StreamlineScanner):
    def __init__(self, **defaults):
        defaults.setdefault("optimize_exposure_per", "sample")
        defaults.setdefault("default_attenuator", 4)
        defaults.setdefault("energy_name", "energy")

        super().__init__(**defaults)

        self.newflat, self.oldflat = ensure_difflab6_id31_flats()


def mock_shopen(**kwargs):
    arguments = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    print(f"shopen({arguments})")


if setup_globals is None:
    streamline_scanner = None
else:
    streamline_scanner = DemoStreamlineScanner()
    setup_globals.shopen = mock_shopen
    setup_globals.energy.position = 75
