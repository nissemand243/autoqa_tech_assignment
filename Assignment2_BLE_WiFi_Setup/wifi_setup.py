"""
Setup file to read product information.

This file has been created for use in Bang & Olufsen A/S
"""
from typing import Any
import ipaddress


def validate_setup(data: dict[str, Any]) -> None:
    required_fields = [
        "device_id",
        "ble_connected",
        "wifi_provisioned",
        "ssid",
        "ip_address",
        "mac_address",
        "status",
    ]

    for field in required_fields:
        assert field in data, f"Missing field: {field}"

    ipaddress.ip_address(data["ip_address"])

    assert data["ble_connected"] is True
    assert data["wifi_provisioned"] is True
    assert data["status"] == "online"


def is_wifi_setup_successful(data: dict[str, Any]) -> bool:
    return (
        data["ble_connected"]
        and data["wifi_provisioned"]
        and data["status"] == "online"
    )
