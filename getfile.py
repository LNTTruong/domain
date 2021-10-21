
import os
import shutil
from deploy import Deploy_Data
import time
from datetime import date


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
                print("oj_files", oj_files)
                first_key = list(oj_files.items())[0][0]
                file_deploy = oj_files[first_key]['pathfile']
                run = Deploy_Data(file_deploy)
                run.deploy_log(file_deploy)
                oj_files.pop(first_key)
                print(oj_files)
                shutil.move(folder_path + "/" + first_key, folder_path + "/file_used/")


if __name__ == '__main__':

    PATH = "D:/workspace/domain/"
    today = date.today()
    # YY/mm/dd
    name_folder = today.strftime("%Y-%m-%d")
    print(name_folder)
    folder_path = PATH + name_folder

    folder_use_path = folder_path + "/file_used/"
    if not os.path.isdir(folder_use_path):
        os.mkdir(folder_use_path)
    while True:
        deploydata = Getfile(folder_path)
        deploydata.deploy_file(folder_path)
        time.sleep(3)





