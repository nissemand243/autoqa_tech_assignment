
import ipaddress
from pathlib import Path
from typing import Any
import json
import pytest

from mdns_discovery import filter_devices_by_service, validate_device


@pytest.fixture
def devices() -> list[dict[str, Any]]:
    return json.loads(Path('discovery_results.json').read_text())


def test_device_is_discoverable(devices: list[dict[str, Any]]) -> None:
    assert devices, "No devices in discovery results"


def test_devices_are_valid(devices: list[dict[str, Any]]) -> None:
    for device in devices:
        validate_device(device)

def test_ip_addresses_are_usable(devices) -> None:
    for device in devices:
        addr = ipaddress.ip_address(device["ip_address"])
        assert not addr.is_unspecified, f"{device['name']}: 0.0.0.0"
        assert not addr.is_link_local, f"{device['name']}: APIPA {addr} — DHCP failed"
        assert not addr.is_loopback, f"{device['name']}: loopback {addr}"
        assert addr.is_private, f"{device['name']}: {addr} is not a local address"

def test_correct_service_advertised(devices: list[dict[str, Any]]) -> None:
    service_types = ["_speaker._tcp.local", "_soundbar._tcp.local"] ## List of service types. Future = JSON file. I am unaware of all service types, hence this solution
    device_counter = 0
    for service in service_types:
        results = filter_devices_by_service(devices, service)
        device_counter = device_counter + len(results)

    assert device_counter == len(devices), (
        f"{len(devices) - device_counter} device(s) advertise an unexpected service type"
    )

def test_no_duplicate_hostnames(devices) -> None:
    hostnames = [d["hostname"] for d in devices]
    assert len(hostnames) == len(set(hostnames))