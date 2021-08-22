#!/bin/bash
export backup_date=`date +20%y%m%d-%H%M%S`
crontab -l > cron.backup.${backup_date}
crontab < ./crontab.txt