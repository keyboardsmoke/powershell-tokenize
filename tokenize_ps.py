import argparse
import base64
import json
import os
import subprocess, sys

parser = argparse.ArgumentParser(prog='tokenize_ps', description='Use powershell internal parser to tokenize a script')
parser.add_argument('-s', '--script', required=True)
parser.add_argument('-o', '--output', default=None)

args = parser.parse_args()

p = subprocess.Popen(["pwsh", "tokenize_ps.ps1", args.script], stdout=subprocess.PIPE)
out, err = p.communicate()

if err:
    print(err)
    exit()

json_content = json.loads(out)

if len(json_content) > 0:
    if "Message" in json_content[0]:
        if args.output is not None:
            with open(args.output, 'w') as fp:
                fp.write(str(json_content))
        else:
            print("Error: " + json_content[0]['Message'] + " (Line: " + str(json_content[0]['Token']['StartLine']) + ", Column: " + str(json_content[0]['Token']['StartColumn']) + ")")

        sys.exit(1)
    else:
        if args.output is not None:
            with open(args.output, 'w') as fp:
                fp.write(str(json_content))
        else:
            print(json_content)

        sys.exit(0)