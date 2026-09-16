"""
Tests to validate WiFi and BLE connectivity.

This file has been created for use in Bang & Olufsen A/S
"""
from pathlib import Path
from typing import Any

import json
import pytest

from wifi_setup import is_wifi_setup_successful, validate_setup


@pytest.fixture
def setup_data() -> dict[str, Any]:
    return json.loads(Path("connectivity_status.json").read_text())


def test_ble_connection_established(setup_data: dict[str, Any]) -> None:
    assert setup_data["ble_connected"] is True


def test_wifi_provisioning_successful(setup_data: dict[str, Any]) -> None:
    assert setup_data["wifi_provisioned"] is True


def test_valid_ip_address(setup_data: dict[str, Any]) -> None:
    validate_setup(setup_data)


def test_device_online(setup_data: dict[str, Any]) -> None:
    assert setup_data["status"] == "online"


def test_wifi_setup_complete(setup_data: dict[str, Any]) -> None:
    assert is_wifi_setup_successful(setup_data)


@pytest.mark.optional
def test_ssid_is_not_empty(setup_data: dict[str, Any]) -> None:
    assert len(setup_data["ssid"]) > 0
