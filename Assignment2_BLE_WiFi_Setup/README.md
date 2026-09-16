# Automation QA Assignment: BLE & Wi‑Fi Onboarding

Duration: 1-2 hours

## Scenario
A mobile application provisions an audio device over BLE.
The device receives Wi‑Fi credentials, joins the network, then becomes discoverable and manageable.
Customers report intermittent setup failures.

## Objectives
Evaluate:
- Test design and quality engineering mindset
- Python automation (pytest)
- BLE/Wi‑Fi networking fundamentals
- Troubleshooting
- System-level thinking
- Communication skills

## Part 1 – Test Design & Risk Analysis (30-40 min)
Design onboarding test coverage.
Consider:
- First-time setup
- Incorrect password
- Weak signal
- BLE disconnect during provisioning
- SSID changes
- DHCP delays
- Multiple devices onboarding simultaneously
- Device reboot during setup

Identify risks and assumptions.
Deliverable: markdown

## Part 2 – Python Automation (45-60 min)
Use connectivity_status.json
Create pytest tests that verify:
1. BLE connection established
2. Wi‑Fi provisioning successful
3. Device received valid IP address
4. Additional test(s) of your choice

Feel free to add additional fields to the file, if needed, to cover additional tests.

## Part 3 – Troubleshooting (10-15 min)
Review logs/device_logs.txt and answer:
- Probable root cause
- Additional debug data required
- Regression test(s) to prevent recurrence

## Part 4 – System Thinking (10 min)
Describe automation strategy using:
- Linux systems
- Hardware test equipment
- GitHub Actions
- Controlled network infrastructure

## Submission
Return the following:
- Answers document
- Python solution
- pytest output (optional)
