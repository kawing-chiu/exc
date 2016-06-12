import ruamel.yaml

inp = """\
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
"""

inp = """
# test
set1:
  - - '000027 2015-12-01'
    - 'xxx：xxxxxxxxx'

  - - '600570 2016-04-28 10:27~11:23 0.9%,+3%,-0%'
    - 'yyy：yyyyyyyy'
"""

code = ruamel.yaml.load(inp, ruamel.yaml.RoundTripLoader)
#code['name']['given'] = 'Bob'

print(ruamel.yaml.dump(code, Dumper=ruamel.yaml.RoundTripDumper), end='')
