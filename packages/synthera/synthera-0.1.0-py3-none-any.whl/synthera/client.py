import os
import logging
import httpx
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from synthera.fixed_income import FixedIncome

_logger: logging.Logger = logging.getLogger(__name__)

ENV_VAR_PREFIX: str = "SYNTHERA"
USER_AGENT_HEADER: str = "Synthera-Python-Client"
API_KEY_HEADER: str = "X-API-Key"
SYNTHERA_API_HOST: str = "https://api.synthera.ai"
SYNTHERA_API_PORT: int = 443
SYNTHERA_API_VERSION: str = "v1"
SYNTHERA_API_TIMEOUT_SECS: int = 10
SYNTHERA_API_HEALTH_STATUS_ENDPOINT: str = "health/status"


class OutputFormat(Enum):
    TEXT = "text"
    JSON = "json"


class SyntheraClientError(Exception):
    pass


class SyntheraClient:
    host: str = SYNTHERA_API_HOST
    port: int = SYNTHERA_API_PORT
    version: str = SYNTHERA_API_VERSION
    api_key: str = None
    timeout_secs: int = SYNTHERA_API_TIMEOUT_SECS
    _fixed_income: "FixedIncome" = None

    def __init__(
        self,
        api_key: str = None,
        host: str = None,
        port: int = None,
        timeout_secs: int = None,
    ) -> None:
        self.api_key: str = api_key or os.getenv(f"{ENV_VAR_PREFIX}_API_KEY")

        if not self.api_key:
            raise SyntheraClientError("API key is required")

        if host:
            self.host: str = host
        elif os.getenv(f"{ENV_VAR_PREFIX}_API_HOST"):
            self.host: str = os.getenv(f"{ENV_VAR_PREFIX}_API_HOST")

        if port is not None:
            self.port: str = port
        elif os.getenv(f"{ENV_VAR_PREFIX}_API_PORT"):
            self.port: str = os.getenv(f"{ENV_VAR_PREFIX}_API_PORT")

        try:
            self.port = int(self.port)
        except ValueError:
            raise SyntheraClientError("Port must be an integer")

        if self.port < 1 or self.port > 65535:
            raise SyntheraClientError("Port must be between 1 and 65535")

        if timeout_secs is not None:
            self.timeout_secs = timeout_secs
        elif os.getenv(f"{ENV_VAR_PREFIX}_API_TIMEOUT_SECS"):
            self.timeout_secs = os.getenv(f"{ENV_VAR_PREFIX}_API_TIMEOUT_SECS")

        try:
            self.timeout_secs = int(self.timeout_secs)
        except ValueError:
            raise SyntheraClientError("Timeout must be an integer")

        if self.timeout_secs < 1:
            raise SyntheraClientError("Timeout must be greater than 0")

        self.base_url: str = f"{self.host}:{self.port}"
        self.api_url: str = f"{self.base_url}/{self.version}"

        self.headers: dict[str, str] = {
            "User-Agent": USER_AGENT_HEADER,
            API_KEY_HEADER: self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        _logger.info(f"Initialized Synthera Client with base url: {self.base_url}")

    @property
    def fixed_income(self) -> "FixedIncome":
        """Initialization of FixedIncome instance."""
        if self._fixed_income is None:
            from synthera.fixed_income import FixedIncome

            self._fixed_income = FixedIncome(self)
        return self._fixed_income

    def make_get_request(
        self,
        endpoint: str,
        output_format: OutputFormat = OutputFormat.TEXT,
    ) -> dict | str:
        """Centralized method to make HTTP GET requests."""
        url: str = f"{self.base_url}/{endpoint}"

        _logger.debug(f"Making GET request to {url}")

        try:
            response: httpx.Response = httpx.get(
                url, headers=self.headers, timeout=self.timeout_secs
            )
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            if output_format == OutputFormat.TEXT:
                return response.text
            elif output_format == OutputFormat.JSON:
                return response.json()
        except httpx.TimeoutException:
            _logger.error(f"Request timed out after {self.timeout_secs} seconds")
            raise SyntheraClientError(
                f"Request timed out after {self.timeout_secs} seconds"
            )
        except httpx.RequestError as e:
            _logger.error(f"An error occurred while making the request: {e}")
            raise SyntheraClientError(
                f"An error occurred while making the request: {e}"
            )
        except httpx.HTTPStatusError as e:
            _logger.error(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
            raise SyntheraClientError(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
        except Exception as err:
            _logger.error(f"An error occurred: {err}")
            raise SyntheraClientError(f"An error occurred: {err}")

    def make_post_request(
        self,
        endpoint: str,
        payload: dict,
    ) -> dict:
        """Centralized method to make HTTP POST requests."""
        url: str = f"{self.api_url}/{endpoint}"

        _logger.debug(f"Making POST request to {url} with payload: {payload}")

        try:
            response: httpx.Response = httpx.post(
                url, json=payload, headers=self.headers, timeout=self.timeout_secs
            )
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            return response.json()
        except httpx.TimeoutException:
            _logger.error(f"Request timed out after {self.timeout_secs} seconds")
            raise SyntheraClientError(
                f"Request timed out after {self.timeout_secs} seconds"
            )
        except httpx.RequestError as e:
            _logger.error(f"An error occurred while making the request: {e}")
            raise SyntheraClientError(
                f"An error occurred while making the request: {e}"
            )
        except httpx.HTTPStatusError as e:
            _logger.error(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
            raise SyntheraClientError(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
        except Exception as err:
            _logger.error(f"An error occurred: {err}")
            raise SyntheraClientError(f"An error occurred: {err}")

    def healthy(self) -> bool:
        """Check if the Synthera API is healthy."""
        endpoint: str = SYNTHERA_API_HEALTH_STATUS_ENDPOINT
        response = self.make_get_request(
            endpoint=endpoint,
            output_format=OutputFormat.TEXT,
        )

        if response == "ok":
            _logger.info("Synthera API is healthy")
            return True
        else:
            _logger.info("Synthera API is not healthy")
            return False
