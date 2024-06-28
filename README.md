# powershell-tokenize

A python script to tokenize powershell scripts, nothing more or less

It can be used on (and was tested on) linux, if you have installed `pwsh`

Example output:
```
python tokenize_ps.py -s test_powershell_scripts/hello_world.ps1
[{'Content': 'Write-Host', 'Type': 1, 'Start': 0, 'Length': 10, 'StartLine': 1, 'StartColumn': 1, 'EndLine': 1, 'EndColumn': 11}, {'Content': 'Hello, World!', 'Type': 5, 'Start': 11, 'Length': 15, 'StartLine': 1, 'StartColumn': 12, 'EndLine': 1, 'EndColumn': 27}]
```