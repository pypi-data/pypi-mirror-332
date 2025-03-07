from typing import Optional

from ..exafs import scan_utils
from ..exafs.processor import ExafsProcessor


class Id24ExafsProcessor(ExafsProcessor):
    def __init__(self, **defaults) -> None:
        defaults.setdefault("workflow", "/users/opid24/ewoks/online.ows")
        defaults.setdefault("_scan_type", "escan")
        counters = defaults.setdefault("_counters", dict())
        counters.setdefault(
            "escan",
            {
                "mu_name": "mu_trans",
                "energy_name": "energy_enc",
                "energy_unit": "keV",
            },
        )
        super().__init__(**defaults)

    def _scan_type_from_scan(
        self, scan: scan_utils.TrigScanCustomRunnerType
    ) -> Optional[str]:
        return "escan"

    def _multi_xas_scan(self, scan: scan_utils.TrigScanCustomRunnerType) -> bool:
        return scan_utils.is_multi_xas_scan(scan)

    def _multi_xas_subscan_size(self, scan: scan_utils.TrigScanCustomRunnerType) -> int:
        return scan_utils.multi_xas_subscan_size(scan)
