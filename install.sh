#!/bin/bash

SERVICE="python"

if pgrep -x "$SERVICE" >/dev/null
then
    echo "$SERVICE is running. I won't replace th crontab right now. Kill python processes first!"
else
    export backup_date=`date +20%y%m%d-%H%M%S`
    echo 'Backing up old crontab into $backup_date'
    crontab -l > cron.backup.${backup_date}
    echo "Installing new crontab"
    crontab < ./crontab.txt
fi