This project is to parse show run output for Cisco Nexus

Starting from interface parsing.

Target state:
- Device configuration consists of two types of variables: base and operational. 
- There should be standards for base variables (ssh is enabled, cdp is disabled globally, etc.) which are easy to follow and enforce with minimal variables.
- Operational variables are variables that might need changes after deployment (vlans, interfaces, etc)
- Target state is device configuration existing as a yaml file for base variables, another for operational variables.
- base.yml for prod devices cannot be updated by engineers, device.yml can be updated by engineers.
- Engineer edits device.yml file, <something> detects the changes, CR is created, updated with change plan, change is implemented.
