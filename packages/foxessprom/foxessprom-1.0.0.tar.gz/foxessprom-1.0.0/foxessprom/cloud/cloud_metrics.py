# foxessprom
# Copyright (C) 2025 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import threading
import time
from typing import Dict, Tuple, Union

from .cloud_device_metrics import CloudDeviceMetrics
from ..custom_metrics import CustomMetrics
from .devices import Devices
from ..utils import capture_errors


class CloudMetrics:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.devices = Devices(args)
        self._lock = threading.Lock()

        if args.mqtt is not None:
            threading.Thread(target=capture_errors(self._update_loop)).start()

    def get_metrics(self) -> Dict[str, Union[Tuple[CloudDeviceMetrics,
                                             CustomMetrics], None]]:
        with self._lock:
            metrics: Dict[str, Union[Tuple[CloudDeviceMetrics,
                                     CustomMetrics], None]] = {}
            for device in self.devices:
                metrics[device.deviceSN] = device.get_metrics(block=True)
            return metrics

    def _update_loop(self) -> None:
        while True:
            time.sleep(self.args.cloud_update_freq)
