from typing import List, Dict, Any, Optional

try:
    from bliss import current_session
except ImportError:
    scan_meta = None
    current_session = None
    user_print = print

import os
from ewoksjob.client import submit
from ..utils import directories
from ..utils import trigger

from ..persistent.parameters import (
    WithPersistentParameters,
    ParameterInfo,
)

_DEFAULT_USER_PARS: Dict[str, Any] = {
    "flip_ud": False,
    "flip_lr": True,
    "wavelength": 0.1,
    "distance": 100,
    "beam": [1000, 1100],
    "polarization": 0.99,
    "kappa": 0,
    "alpha": 50,
    "theta": 0,
    "phi": 0,
    "omega": "",
    "rotation": 180,
    "dummy": -1,
    "offset": 1,
    "dry_run": False,
    "calc_mask": False,
}

_DEFAULT_SCAN_PARS: Dict[str, Any] = {
    "images": "",
    "output": "",
}


class Id15bEiger2Crysalis(
    WithPersistentParameters,
    parameters=[
        ParameterInfo("queue", category="workflows", deprecated_names=["worker"]),
        ParameterInfo("workflow", category="workflows"),
        ParameterInfo(
            "lima_name",
            category="Eiger2Crysalis",
            doc="Lima name of the camera: (i.e. eiger)",
        ),
        ParameterInfo(
            "scan_parameters",
            category="Eiger2Crysalis",
            doc="Derived from scan and motors",
        ),
        ParameterInfo(
            "user_parameters", category="Eiger2Crysalis", doc="Specify explicitly"
        ),
        ParameterInfo(
            "frameset_copy",
            category="Eiger2Crysalis",
            doc="frame.set path that will be copied automatically inside the output folder",
        ),
        ParameterInfo("_enabled"),
    ],
):
    def __init__(self, **defaults: Any) -> None:
        if current_session is None:
            raise ImportError("bliss")
        defaults.setdefault("_enabled", False)
        defaults.setdefault("workflow", "")
        defaults.setdefault("user_parameters", _DEFAULT_USER_PARS)
        defaults.setdefault("scan_parameters", _DEFAULT_SCAN_PARS)
        defaults.setdefault("frameset_copy", "")
        super().__init__(**defaults)

        if self._enabled:
            self._register_workflow_trigger()
        else:
            self._unregister_workflow_trigger()

    def _info_categories(self) -> Dict[str, dict]:
        self.update_scan_parameters()
        return super()._info_categories()

    def update_scan_parameters(self, scan: Any = None) -> None:
        scan_parameters = dict()
        if scan:
            scan_parameters["images"] = self.get_lima_filenames(scan)
            scan_parameters["output"] = self.get_output_path(scan)
        self.scan_parameters.update(scan_parameters)
        return scan_parameters

    def get_filename(self, scan) -> str:
        filename = scan.scan_info.get("filename")
        if filename:
            return filename
        return current_session.scan_saving.filename

    def get_output_path(self, scan: Any) -> str:
        scan_nb = scan.scan_info["scan_nb"]
        dataset_processed_dir = get_dataset_processed_dir(self.get_filename(scan))
        scan_processed_dir = os.path.join(dataset_processed_dir, f"scan{scan_nb:04d}")
        output = os.path.join(scan_processed_dir, "frame_1_{index}.esperanto")
        return output

    def get_lima_filenames(self, scan: Any) -> List[str]:
        scan_number = scan.scan_number
        lima_files = [
            f"{scan.scan_saving.images_path.format(scan_number=scan_number,img_acq_device=self.lima_name)}0000.h5"
        ]
        return lima_files

    def get_omega(self, scan: Any) -> str:
        """
        Calculate the omega parameter as a formatted string based on scan info.

        The scan is assumed to be centered around zero. This function computes the
        symmetric starting position relative to the center and formats it with a
        leading minus sign.
        """
        # Extract scan parameters.
        start = scan.scan_info["start_pos"]
        step = scan.scan_info["step_size"]
        npoints = scan.scan_info["npoints"]

        # Calculate the end position of the scan.
        end = start + npoints * step

        # Compute the center of the scan.
        center = start + (end - start) / 2

        # Compute the symmetric starting offset relative to the center.
        symmetric_start = start - center

        # Return the omega parameter formatted with a leading minus sign.
        return f"-{symmetric_start}-index*{step}"

    def get_scan_parameters(self, scan: Any) -> Dict[str, Any]:
        scan_parameters = dict()
        scan_parameters["omega"] = self.get_omega(scan)
        scan_parameters["exposure_time"] = scan.scan_info["exposure_time"]
        return scan_parameters

    def get_inputs(self, scan) -> List[Dict[str, Any]]:
        parameters = self.user_parameters.to_dict()
        parameters.update(self.update_scan_parameters(scan))

        inputs = []
        for key, value in parameters.items():
            inputs.append(
                {
                    "task_identifier": "Eiger2Crysalis",
                    "name": key,
                    "value": value,
                }
            )
        inputs += [
            {
                "task_identifier": "Eiger2Crysalis",
                "name": "custom_frame_set_path",
                "value": self.frameset_copy,
            },
        ]
        return inputs

    def get_submit_arguments(self, scan) -> Dict[str, Any]:
        return {
            "inputs": self.get_inputs(scan),
            "outputs": [{"all": "False"}],
        }

    def run_conversion(self, scan: Optional[Any]) -> None:
        """Executes on given scan"""
        kwargs = self.get_submit_arguments(scan)
        submit(args=(self.workflow,), kwargs=kwargs, queue=self.queue)

    def enable(self):
        self._enabled = True
        self._register_workflow_trigger()

    def disable(self):
        self._enabled = False
        self._unregister_workflow_trigger()

    def _register_workflow_trigger(self):
        workflows_category = trigger.register_workflow_category(timing="END")
        workflows_category.set("processing", self.run_conversion)

    def _unregister_workflow_trigger(self):
        trigger.unregister_workflow_category()


def get_dataset_processed_dir(
    dataset_filename: str,
) -> str:  # Temporary, waiting for !173 to be merged
    root = directories.get_processed_dir(dataset_filename)
    collection = os.path.basename(directories.get_collection_dir(dataset_filename))
    dataset = os.path.basename(directories.get_dataset_dir(dataset_filename))
    return os.path.join(root, collection, dataset)
