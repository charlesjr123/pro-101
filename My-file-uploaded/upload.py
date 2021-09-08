import os 

import dropbox

for root,dirs, files in os.walk(file_from):
    realtive_path=os.path.realpath(local_path,file_from)
    dropbox_path=os.path.join(file_to,realtive_path)


    with open(local_path,'rb') as f:
        dbx.files_upload(f.read(),dropbox_path,mode=WriteModel('overite'))
