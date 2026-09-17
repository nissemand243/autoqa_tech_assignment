# mDNS_Bluetooth part 1

## Device boot and initial mDNS advertisement

### TS 1

Key assumption: The device is the only one on the network
Key assumption: The app was not browsing during the device announcement window.
Key assumption: The app is launched without cached records for this device.  

Scenario:  
The app starts -> Nothing is shown -> Record T0 -> App queries on local network for the device ->  The device answers the queries -> Record T1 -> Response arrive within a second of query sent and record resolve consistently.

Risk:  
HIGH  
If the device only announces, but never listens for a query, it depends on timing. Missing the window, means rebooting the device, while making sure the app is open and browsing for the device.
Though, the more likely issue to reach production would be intermittently missing queries, exposing flakiness to the user.

### TS 2

Key assumption: The device is the only one on the network
Key assumption: The app is launched with cold-cache.
Key assumption: The app is browsing for "_speaker._tcp.local", before device boot

Scenario:  
The device boots -> Device push announcement -> app receives announcement within ~10 seconds of boot complete, as per device_logs.txt -> App caches and renders

Risk:  
MEDIUM  
If the device only answer queries, but never announces, it depends on client asking at the right moment. The device appears eventually within the unknown re-query interval, but not promptly. Will show as unreliable

### TS 3

Key assumption: That the app is browsing for "_speaker._tcp.local" before device boot

Scenario:  
Device boot -> record T0 at boot complete -> record T1 when device becomes visible to a mDNS browser -> record T2 when TCP successfully connects to the advertised port -> assert T2 <= T1

Risk:  
MEDIUM  
Device advertise before its service is ready. This leads to device being visible, but non-functional in the app.


## Wi-Fi disconnect and reconnect

### TS 1

Key assumption: The device's mDNS stack is notified on link-down / link-up events  
Key assumption: The device has a DHCP reserved pinning to the MAC address

Scenario:  
App browsing for "_speaker._tcp.local" -> Drop Wi-Fi link -> restore Wi-Fi link -> device reassociates with the reserved address

Assert:  
The device instance appears in the browse results within 1-3s(derived from RFC 6762) of link-up
The app resolves the local name to the reserved address  
port 80 accepts connection  
no duplicate instance appears

Risk:  
LOW  
The device fails to re-announce on link-up OR the re-announcement is lost. As the device keeps the address, the user will not notice this error.

### TS 2

Key assumption: The device's mDNS stack is notified on link-down / link-up events  

Scenario:  
App browsing for "_speaker._tcp.local" -> Drop Wi-Fi link -> Clear routers lease table -> restore Wi-Fi link -> device reassociates and recieves a new address

Measure:  
Time from link-up to first successful resolution  

Assert:  
Starting at link-up, every 2s for 60s, browse "_speaker._tcp.local" and resolve "Beosound-Balance-12345678.local".  
The instance remains present in the browse results throughout  
Every successful resolution returns the new address. None return the pre-disconnect address.  

Risk:  
MEDIUM-HIGH  
A missing cache-flush bit results in 2 A records for the same hostname coexisting in the cache, until the TTL expires, ~120s or a correctly flagged announcement arrives.. The resolution may return either record. Device would be reachable on some attemps, while unreachable on others.

## Key assumptions

This chapter extends as areas are covered in detail.

----- FILL IN WITH GENERAL ASSUMPTIONS FROM ABOVE! ---- Keep assumptions, that are test scenario tailored


## Highest-risk scenarios

This chapter extends as areas are covered in detail.
--- PULL IN FROM SCENARIOS ABOVE!!!! ----

## Automation priority

This chapter extends as areas are covered in detail.

The priority order of automation, differs from risk order, as risk ranks by consequence, where automation ranks by frequency x cost x diagnostic value.

- Multiple devices on the same network
- - Multiple devices on the same network means parallel trafic for advertisement and querrying. Important to test, this is handled gracefully.
- Power cycles + IP address changes
- - Making sure that the new addresses are resolved correctly for all devices. Making sure devices are visible in app as well as reachable through the app
- Reconnect with address change
- - Testing with singular device, to assert whether the new address is always used as expected
- Duplicate hostnames or service conflicts
- - Make sure duplicate hostnames are handled gracefully (for example Beosound-Balance-12345678.local + Beosound-Balance-12345678-2.local)
- Push vs Pull discovery
- Sequence check of device advertisement and service ready
