#!/bin/bash

project_dir=/srv/python_projects/Arduino_Alarm/backup_scripts

python3 $project_dir/mongoExport.py

sleep 15

cp $project_dir/logs/Mongo_Backups/mongo_export_backup.json /var/www/html

echo Job Done.
