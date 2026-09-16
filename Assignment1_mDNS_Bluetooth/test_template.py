
from pathlib import Path
from typing import Any
import json
import pytest

from mdns_discovery import filter_devices_by_service, validate_device


@pytest.fixture
def devices() -> list[dict[str, Any]]:
    return json.loads(Path('discovery_results.json').read_text())


def test_device_is_discoverable(devices: list[dict[str, Any]]) -> None:
    assert len(devices) > 0


def test_ip_addresses_are_valid(devices: list[dict[str, Any]]) -> None:
    for device in devices:
        validate_device(device)


def test_correct_service_advertised(devices: list[dict[str, Any]]) -> None:
    results = filter_devices_by_service(devices, '_speaker._tcp.local')
    assert len(results) > 0
