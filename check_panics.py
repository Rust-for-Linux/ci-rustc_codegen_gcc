#!/usr/bin/env python3

import re
import sys

PATTERNS = {
    b"No such file or directory": [],
    rb"\bpanic\b": [],
    rb"\bpanics\b": [],
    rb"\boops\b": [],
    rb"\boopses\b": [],
    rb"\btaint\b": [],
    rb"\btaints\b": [
        b"rust_out_of_tree: loading out-of-tree module taints kernel."
    ],
    rb"\bfault\b": [],
    rb"\bfaults\b": [],
    rb"\bcorrupted\b": [],
    rb"\btrace\b": [
        b"] RCU Tasks Trace:",
        b"] trace event string verifier disabled",
        b".pcie: probe with driver pci-host-generic failed with error -16"
    ],
    rb"\btraces\b": [],
    rb"\bbug\b": [
        b" and report a bug"
    ],
    rb"\bbugs\b": [],
    rb"\berror\b": [
        b"message (level 3)",
        b"regulatory.db",
        b".pcie: probe with driver pci-host-generic failed with error -16",
        b"rust/kernel/error.rs",
    ],
    rb"\berrors\b": [],
    rb"\bwarning\b": [
        b"message (level 4)"
    ],
    rb"\bwarnings\b": [],
}

def main():
    ok = True
    with open(sys.argv[1], "rb") as file:
        for line in file:
            for pattern in PATTERNS:
                if re.search(pattern, line):
                    for allowed_string in PATTERNS[pattern]:
                        if allowed_string in line:
                            break
                    else:
                        ok = False
                        print("Bad line found in log:")
                        print(f"    Line:    {line}")
                        print(f"    Pattern: {pattern}")
                        print(f"    Allowed: {PATTERNS[pattern]}")
                        print()

    if not ok:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
