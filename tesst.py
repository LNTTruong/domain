# p = ["taf.tt", "aff.tt", "rthrdfh.t"]
# n = ["taf.tt"]
# x = len(p) - len(n)
# print(p[-x:])

folder = os.listdir(path_folder)
        for file in folder:
            if file in LIST_FILE:
                print("error duplicate")

            else:
                LIST_FILE.append(file)
        for f in LIST_FILE:

            if f in LIST_FILE_USED:
                print("File đã xử lí")
            else:

# {'https://m.afamily.vn': {'lcp': 329334.75600000034, 'fcp': 258690.20000060793, 'cls': 42.69434732569639, 'ttfb': 235444, 'sum_ss_lcp': 461, 'sum_ss_fcp': 808, 'sum_ss_cls': 811, 'sum_ss_ttfb': 815}, 'https://m.autopro.com.vn': {'lcp': 46008.393000000004, 'fcp': 38984.00000014901, 'cls': 1.9148085415549947, 'ttfb': 20441, 'sum_ss_lcp': 463, 'sum_ss_fcp': 810, 'sum_ss_cls': 813, 'sum_ss_ttfb': 817}, 'https://afamily.vn': {'lcp': 92027.10400000002, 'fcp': 72731.45499015955, 'cls': 6.619395013772748, 'ttfb': 42753, 'sum_ss_lcp': 459, 'sum_ss_fcp': 806, 'sum_ss_cls': 809, 'sum_ss_ttfb': 813}, 'https://autopro.com.vn': {'lcp': 2827.596000000001, 'fcp': 2386.799999907613, 'cls': 0.4420983460374966, 'ttfb': 552, 'sum_ss_lcp': 206, 'sum_ss_fcp': 352, 'sum_ss_cls': 358, 'sum_ss_ttfb': 359}, 'http://bu244.9s63k.xyz': {'lcp': 0, 'fcp': 300, 'cls': 0, 'ttfb': 18, 'sum_ss_lcp': 434, 'sum_ss_fcp': 767, 'sum_ss_cls': 770, 'sum_ss_ttfb': 774}}
# filename =====  D:/data/data/2021-10-18/kh-1632503631630.dat
# {'https://m.afamily.vn': {'lcp': 366947.39499999955, 'fcp': 324649.00000123907, 'cls': 34.99227087764009, 'ttfb': 204787, 'sum_ss_lcp': 391, 'sum_ss_fcp': 744, 'sum_ss_cls': 718, 'sum_ss_ttfb': 746}, 'https://afamily.vn': {'lcp': 118854.70499999993, 'fcp': 31358.629999539815, 'cls': 0.5164435498673863, 'ttfb': 8655, 'sum_ss_lcp': 385, 'sum_ss_fcp': 731, 'sum_ss_cls': 705, 'sum_ss_ttfb': 733}, 'https://m.autopro.com.vn': {'lcp': 47293.78400000002, 'fcp': 35135.00000102818, 'cls': 2.251265713945672, 'ttfb': 23736, 'sum_ss_lcp': 386, 'sum_ss_fcp': 735, 'sum_ss_cls': 709, 'sum_ss_ttfb': 737}, 'https://autopro.com.vn': {'lcp': 13715.294999999998, 'fcp': 11703.099999904633, 'cls': 1.3707512312753913, 'ttfb': 3122, 'sum_ss_lcp': 351, 'sum_ss_fcp': 656, 'sum_ss_cls': 630, 'sum_ss_ttfb': 658}}
# filename =====  D:/data/data/2021-10-18/kh-1632503636848.dat
# {'https://m.afamily.vn': {'lcp': 352596.1750000001, 'fcp': 304038.69999923836, 'cls': 22.973930747052478, 'ttfb': 181459, 'sum_ss_lcp': 376, 'sum_ss_fcp': 706, 'sum_ss_cls': 710, 'sum_ss_ttfb': 719}, 'https://m.autopro.com.vn': {'lcp': 33362.986, 'fcp': 27022.300000458956, 'cls': 1.1332859461558502, 'ttfb': 26876, 'sum_ss_lcp': 365, 'sum_ss_fcp': 674, 'sum_ss_cls': 678, 'sum_ss_ttfb': 687}, 'https://afamily.vn': {'lcp': 45015.81799999999, 'fcp': 30321.36000380898, 'cls': 0.6744165828363928, 'ttfb': 17066, 'sum_ss_lcp': 372, 'sum_ss_fcp': 699, 'sum_ss_cls': 703, 'sum_ss_ttfb': 712}, 'https://autopro.com.vn': {'lcp': 1465, 'fcp': 1260.3999999463558, 'cls': 0.15804433968431864, 'ttfb': 1491, 'sum_ss_lcp': 291, 'sum_ss_fcp': 536, 'sum_ss_cls': 540, 'sum_ss_ttfb': 549}}
# if oj_data[hr]["lcp"] != 0:
#     sum_ss_lcp += 1
#
# if sums[hr]["fcp"] != 0:
#     sum_ss_fcp += 1
#
# if sums[hr]["cls"] != 0:
#     sum_ss_cls += 1
#
# if sums[hr]["ttfb"] != 0:
#     sum_ss_ttfb += 1
# sums[hr]["sum_ss_lcp"] = sum_ss_lcp
#
# sums[hr]["sum_ss_fcp"] = sum_ss_fcp
#
# sums[hr]["sum_ss_cls"] = sum_ss_cls
#
# sums[hr]["sum_ss_ttfb"] = sum_ss_ttfb
# sums[hr]["average_lcp"] = sums[hr]["lcp"] / sum_ss_lcp
# sums[hr]["average_fcp"] = sums[hr]["fcp"] / sum_ss_fcp
# sums[hr]["average_cls"] = sums[hr]["cls"] / sum_ss_cls
# sums[hr]["average_ttfb"] = sums[hr]["ttfb"] / sum_ss_ttfb
# oj_domain1 = {
#     sums[hr]: {
#         "average_lcp": sums[hr]["average_lcp"],
#         "average_fcp": sums[hr]["average_fcp"],
#         "average_cls": sums[hr]["average_cls"],
#         "average_ttfb": sums[hr]["average_ttfb"]}
#
# }
# print(sums)
# oj_domain.update(oj_domain1)
#
# ----------------------
# import json
# import os
# from urllib.parse import urlparse
# from prometheus_client import start_http_server, Summary
# from prometheus_client import Gauge
# import random
# import time
#
#
# class Getfile():
#
#
# class Deploy_Data():
#
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         # start_http_server(8000)
#         # self.g = Gauge('sensor_data', 'Value gathered by sensor', ['hostname', 'timeDom', 'timeConnect', 'timeResponse', 'ttfb'])
#         # self.file_user = self.write_namefile_used()
#
#     def deploy_log(self, folder_path):
#         folder = os.listdir(folder_path)
#         for file in folder:
#
#             path_file = self.folder_path + '/' + file
#             print("filename ===== ", path_file)
#             sums = {}
#             with open(path_file) as fh:
#                 for line in fh:
#                     log_json = json.loads(line)
#                     common = log_json.get("common")
#                     _hr = common.get("HR")
#                     data = log_json.get("data")
#                     _lcp = data.get("lcp")
#                     _fcp = data.get("fcp")
#                     _cls = data.get("cls")
#                     _ttfb = data.get("ttfb")
#                     lcp, fcp, cls, ttfb = self.vailidatlog(_lcp, _fcp, _cls, _ttfb)
#                     hr = urlparse(_hr)
#                     hr = hr.scheme + "://" + hr.netloc
#
#                     oj_data = {
#                         hr: {
#                             "lcp": lcp,
#                             "fcp": fcp,
#                             "cls": cls,
#                             "ttfb": ttfb}
#                     }
#                     # self.vailidat_value(sums, oj_data)
#                     if hr not in sums:
#                         sums.update(oj_data)
#                     else:
#                         sums[hr]["lcp"] += oj_data[hr]["lcp"]
#                         sums[hr]["fcp"] += oj_data[hr]["fcp"]
#                         sums[hr]["cls"] += oj_data[hr]["cls"]
#                         sums[hr]["ttfb"] += oj_data[hr]["ttfb"]
#
#     # def vailidat_value(self, hr, sums, oj_data, oj_domain):
#     #     sum_ss_lcp = 0
#     #     sum_ss_fcp = 0
#     #     sum_ss_cls = 0
#     #     sum_ss_ttfb = 0
#     #     if hr not in sums:
#     #         sums.update(oj_data)
#     #     else:
#     #         sums[hr]["lcp"] += oj_data[hr]["lcp"]
#     #         sums[hr]["fcp"] += oj_data[hr]["fcp"]
#     #         sums[hr]["cls"] += oj_data[hr]["cls"]
#     #         sums[hr]["ttfb"] += oj_data[hr]["ttfb"]
#     #     if oj_data[hr]["lcp"] != 0:
#     #         sum_ss_lcp += 1
#     #     sums[hr]["sum_ss_lcp"] = sum_ss_lcp
#     #     if sums[hr]["fcp"] != 0:
#     #         sum_ss_fcp += 1
#     #     sums[hr]["sum_ss_fcp"] = sum_ss_fcp
#     #     if sums[hr]["cls"] != 0:
#     #         sum_ss_cls += 1
#     #     sums[hr]["sum_ss_cls"] = sum_ss_cls
#     #     if sums[hr]["ttfb"] != 0:
#     #         sum_ss_ttfb += 1
#     #     sums[hr]["sum_ss_ttfb"] = sum_ss_ttfb
#     #
#     #     print(sums)
#     def vailidatlog(self, _lcp, _fcp, _cls, _ttfb):
#         lcp = 0
#         fcp = 0
#         cls = 0
#         ttfb = 0
#         if _lcp != None and _lcp > 0:
#             lcp = _lcp
#         if _fcp != None and _fcp > 0:
#             fcp = _fcp
#         if _cls != None and _cls > 0:
#             cls = _cls
#         if _ttfb != None and _ttfb > 0:
#             ttfb = _ttfb
#
#         return lcp, fcp, cls, ttfb
#
#
# PATH = "D:/data/data/2021-10-18"
# while True:
#     deploydata = Deploy_Data(PATH)
#     deploydata.deploy_log(PATH)
-----

class Producer(threading.Thread):
	"""
    Producers random integers to a list
    """

    def __init__(self, integers, condition):
    	threading.thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
    	"""
        Append random integers to integers list at random time.
        """
        while True:
        	integer = random.randint(0, 256)
            self.condition.acquire()
            print('condition acquired by {}'.format(self.name))
            self.integers.append(integer)
            print('{} appended to list by {}'.format(integer, self.name))

            print('condition notified by {}'.self.name)
            self.condition.notify()

            print('condition released by {}'.format(self.name))
            self.condition.release()
            time.sleep(1)


class Consumer(threading.Thread):
	"""
    consumes random integers for a list
    """
    def __init__(self, integers, condition):
    	threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
    	"""
        Consumes integers from shared list
        """
        while True:
        	self.condition.acquire()
            print('condition acquired by {}'.format(self.name))
            while True:
            	if self.integers:
                	integer = self.integers.pop()
                    print('{} popped from list by {}'.format(integer, self.name))
                    break
				print('conditon wait by {}'.format(self.name))
                self.condition.wait()

            print('condition released by {}'.format(self.name))
            self.condition.release()

def main():
	integers = []
    condition = threading.Condition()
    producer = Producer(integers, condition)
    consumer = Consumer(integers, condition)
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
