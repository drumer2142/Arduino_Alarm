# the script is intented for exporting the specified collection
# for backup and security perposes. It is triggered with a cronjob and can be modified
# to suite the server's setup

import os

Database = "Arduino_Alarm"
Collection = "alarm_data"
export_path = "logs/Mongo_Backups/mongo_export_backup.json"

export_command = "mongoexport --db "+Database+" --collection "+Collection+" --out "+export_path+" --jsonArray"

os.system(export_command)
