#!/bin/bash
crontab -l > cron.backup
crontab < ./crontab.txt