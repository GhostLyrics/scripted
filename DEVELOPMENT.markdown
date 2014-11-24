# Developer Notes

## Pylama configuration:

disabled error codes:
D202,W0401,W0614,I0011

detailed reasons:
- D202 "No blank lines allowed \*after\* method docstring": makes things harder
  to read
- W0401 "Wildcard import %s": prevents automatically importing new fabric
  commands
- W0614 "Unused import %s from wildcard import": prevents automatically
  importing new fabric commands
- I0011 "Locally disabling %s": prevents overriding linters for camelCase
  names where they make more sense (e.g. `get_IPs`)
