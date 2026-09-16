
from typing import Any
import ipaddress


def validate_device(device: dict[str, Any]) -> None:
    required_fields = [
        "name",
        "hostname",
        "ip_address",
        "service",
        "port",
    ]

    for field in required_fields:
        assert field in device, f"Missing field: {field}"

    ipaddress.ip_address(device["ip_address"])

    assert device["hostname"].endswith(".local")
    assert device["service"] == "_speaker._tcp.local"
    assert device["port"] > 0



def filter_devices_by_service(
    devices: list[dict[str, Any]],
    service: str,
) -> list[dict[str, Any]]:
    return [d for d in devices if d["service"] == service]
