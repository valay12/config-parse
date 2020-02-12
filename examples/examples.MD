KEY:
<required dynamic if previous keyword>
[optional]
{ option1 | option2 }

channel-group <channel-id> [ mode { active | passive | on } ]
Examples:
channel-group 100		VALID
channel-group 100 mode active	VALID
channel-group			INVALID
channel-group 100 mode		INVALID
channel-group 100 mode off	INVALID

'(channel-group) (\d+)': {'channel-id': channel-id, 'mode': DEFAULT, 'enabled': True}
'(channel-group) (\d+) (mode) (active|passive|on)': {'channel-id': 2, 'mode': 4, 'enabled': True}

Global-Commands:

'(feature) (interface-vlan|ssh|udld|tacacs\+|vtp)': {1: {2: True}}
'(no) (feature) (telnet)': {2: {3: False}}
'(no) (vlan) (\d+): {2: {3: False}}
'(vtp) (domain) (.+$)': {1: {2: 3}}
'(vtp) (mode) (transparent)': {1: {2: 3}}
'(udld) (message-time) (\d+)': {1: {2: 3}}
'(spanning-tree) (mode) (rapid-pvst)': {1: {2: 3}}
'(spanning-tree) (loopguard) (default)': {1: {2: 3}}
'(spanning-tree) (port type edge) (default)': {1: {2: 3}}
'(spanning-tree) (port type edge) (bpduguard) (default)': {1: {2: {3: 4}}}
'(ip route) (\w+) (\w+) (\w+)': {1: {(2,3): 4}}

