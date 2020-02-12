import re

patterns = ['(description) (.*)',
            '(encapsulation) (dot1Q) (.*)',
            '(vrf member) (.*)',
            '(mtu) (.*)',
            '(ip address) (.*)',
            '(ip pim) (.*)',
            '( |no) (ip passive-interface) (eigrp|ospf) (.*)',
            '( |no) (shutdown)',
            '(channel-group) (.*) (mode) (active)']
def int_parse(int_config):
  int_parse = {}
  raw_parse = []
  int_parse['interface'] = int_config.pop(0).split()[1]
#  print 'Intconfig after pop: ' + str(int_config)
  for line in int_config:
    print 'Line: ' + line
    for pattern in patterns:
      print 'Pattern: ' + pattern
      if re.match(pattern,line):
        raw_parse.append(re.match(pattern,line).groups())
  return raw_parse

int_config = ['interface Eth1/56','mtu 989','vrf member DMZ']
print int_parse(int_config)
