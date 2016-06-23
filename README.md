python-health
=============

A tiny library of tools for verifying the health of critical server components.

Examples
------
```shell
# deploy a script to all hosts in an inventory group
ansible all -m script -a "check_stale.py /var/log/messages"
```
