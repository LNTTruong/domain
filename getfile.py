
import os
import shutil
from deploy import Deploy_Data
import time

oj_used = {}
class Getfile():
    def __init__(self, folder_path):
        self.folder_path = folder_path
        # start_http_server(8000)
        # self.g = Gauge('sensor_data', 'Value gathered by sensor', ['hostname', 'timeDom', 'timeConnect', 'timeResponse', 'ttfb'])
        # self.file_user = self.write_namefile_used()

    def deploy_file(self, folder_path):

        folder = os.listdir(folder_path)
        oj_files = {}
        for file in folder:
            str_endpoit = ".dat"
            if str_endpoit in file:
                path_file = folder_path + "/" + file
                oj_file = {
                    file:{
                        "pathfile": path_file
                    }
                }
                if file not in oj_files:
                    oj_files.update(oj_file)
        if len(oj_files) > 0:
            # path_file = oj_files[file]["pathfile"]
            while len(oj_files):
                first_key = list(oj_files.items())[0][0]
                file_deploy = oj_files[first_key]['pathfile']
                run = Deploy_Data(file_deploy)
                run.deploy_log(file_deploy)
                oj_files.pop(first_key)
                shutil.move(folder_path + "/" + first_key, folder_path + "/file/")


PATH = "D:/workspace/domain/2021-10-18"
while True:
    deploydata = Getfile(PATH)
    deploydata.deploy_file(PATH)
    time.sleep(3)





