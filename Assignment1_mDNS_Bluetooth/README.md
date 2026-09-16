# Automation QA Assignment: Bluetooth Services & mDNS Discovery

Duration: 1-2 hours
Experience: 0-2 years

## Scenario
A Wi‑Fi connected audio device advertises itself via mDNS so that a mobile application can discover it on the local network. Customers occasionally report that the product is connected and functioning but does not appear in the mobile app.

## Objectives
Evaluate:
- Test design and quality engineering mindset
- Python automation (pytest)
- Networking fundamentals
- Troubleshooting and root-cause analysis
- System-level thinking
- Communication skills

## Part 1 – Test Design & Risk Analysis (30-40 min)

Describe your assumptions, test scenarios, risks, and edge cases for validating mDNS device discovery.

Cover:
- Device boot and initial mDNS advertisement
- Wi-Fi disconnect and reconnect
- Device power cycle
- Multiple devices on the same network
- IP address changes (DHCP renewal)
- Router reboot
- Duplicate hostnames or service conflicts

Identify:
- Key assumptions
- Highest-risk scenarios
- Which scenarios you would automate first and why

Deliverable: markdown

## Part 2 – Python Automation (45-60 min)
Use discovery_results.json as mocked output.
Implement pytest tests to verify:
1. Device is discoverable
2. Correct service type is advertised
3. IP addresses are valid
4. Additional test(s) of your choice

Feel free to add additional fields to the file, if needed, to cover additional tests.

## Part 3 – Troubleshooting (10-15 min)
Review logs/device_logs.txt and answer:
- Most likely root cause
- Additional information to collect
- Regression test(s) to prevent recurrence

## Part 4 – System Thinking (10 min)
Explain how you would automate mDNS validation in CI using:
- Linux systems
- Hardware test equipment
- GitHub Actions
- Network infrastructure

## Submission
Return the following:
- Answers document
- Python solution
- pytest output (optional)
