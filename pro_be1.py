#!/usr/bin/python
# -*- coding: UTF-8 -*-
###############################################
# проверяем синхру на обьектах (с) Shtirlits
###############################################
import subprocess,os
def sync_check(azs_name, azs_ip="127.0.0.1", user_name="root" ):
	print azs_name
	con_string = user_name+"@"+azs_ip
	print con_string
	cmd_string = "grep 'ERR' /var/log/sync.log | tail"
	print cmd_string
	print subprocess.call(["ssh", con_string, cmd_string])

sync_check("azs1")