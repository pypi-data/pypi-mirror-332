# Copyright 2025 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from beeai_framework.errors import FrameworkError


class ResourceError(FrameworkError):
    """Base class for memory-related exceptions."""

    def __init__(
        self,
        message: str = "Memory error",
        *,
        is_fatal: bool = False,
        is_retryable: bool = False,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, is_fatal=is_fatal, is_retryable=is_retryable, cause=cause)


class ResourceFatalError(ResourceError):
    """Fatal memory errors that cannot be recovered from."""

    def __init__(self, message: str = "Memory error - fatal", *, cause: Exception | None = None) -> None:
        super().__init__(message, is_fatal=True, is_retryable=False, cause=cause)


class SerializerError(FrameworkError):
    """Raised for errors caused by serializer."""

    def __init__(self, message: str = "Serializer error", *, cause: Exception | None = None) -> None:
        super().__init__(message, is_fatal=True, is_retryable=False, cause=cause)
