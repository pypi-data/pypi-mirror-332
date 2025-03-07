"""
 Input reader exceptions.
"""

#  Copyright (c) 2023-2024. ECCO Sneaks & Data
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from esd_services_api_client.nexus.exceptions._nexus_error import (
    FatalNexusError,
    TransientNexusError,
)


class FatalInputReaderError(FatalNexusError):
    """
    Input reader exception that shuts down the Nexus.
    """

    def __init__(self, failed_reader: str, underlying: BaseException):
        super().__init__()
        self.with_traceback(underlying.__traceback__)
        self._failed_reader = failed_reader

    def __str__(self) -> str:
        return f"Reader for alias '{self._failed_reader}' failed to fetch the data and this operation cannot be retried. Review traceback for more information"


class TransientInputReaderError(TransientNexusError):
    """
    Input reader exception that will initiate a retry in Crystal.
    """

    def __init__(self, failed_reader: str, underlying: BaseException):
        super().__init__()
        self.with_traceback(underlying.__traceback__)
        self._failed_reader = failed_reader

    def __str__(self) -> str:
        return f"Reader for alias '{self._failed_reader}' failed to fetch the data. This error can be resolved by retrying the operation"
