import json
from urllib.parse import urlparse
from main import Prometheus
import shutil




class Deploy_Data():

    def __init__(self, folder_path):
        self.folder_path = folder_path


    def deploy_log(self, path_file):
        print("filename ===== ", path_file)
        sums = {}
        with open(path_file) as fh:
            for line in fh:

                log_json = json.loads(line)
                common = log_json.get("common")
                _hr = common.get("HR")
                data = log_json.get("data")
                _lcp = data.get("lcp")
                _fcp = data.get("fcp")
                _cls = data.get("cls")
                _ttfb = data.get("ttfb")
                lcp, fcp, cls, ttfb = self.vailidatlog(_lcp, _fcp, _cls, _ttfb)
                hr = urlparse(_hr)
                hr = hr.scheme +"://"+ hr.netloc

                oj_data = {
                    hr:{
                        "lcp": lcp,
                        "fcp": fcp,
                        "cls": cls,
                        "ttfb": ttfb,
                        "ss_lcp": 0,
                        "ss_fcp": 0,
                        "ss_cls": 0,
                        "ss_ttfb": 0,
                    "average_lcp": 0,
                    "average_fcp": 0,
                    "average_cls": 0,
                    "average_ttfb": 0}
                }
                print("oj_data", oj_data)
                if hr not in sums:
                    sums.update(oj_data)
                else:
                    sums[hr]["lcp"] += oj_data[hr]["lcp"]
                    sums[hr]["fcp"] += oj_data[hr]["fcp"]
                    sums[hr]["cls"] += oj_data[hr]["cls"]
                    sums[hr]["ttfb"] += oj_data[hr]["ttfb"]
                    if oj_data[hr]["lcp"] != 0:

                        sums[hr]["ss_lcp"] += 1
                        sums[hr]["average_lcp"] = sums[hr]["lcp"] / sums[hr]["ss_lcp"]

                    if sums[hr]["fcp"] != 0:

                        sums[hr]["ss_fcp"] += 1
                        sums[hr]["average_fcp"] = sums[hr]["fcp"] / sums[hr]["ss_fcp"]

                    if sums[hr]["cls"] != 0:

                        sums[hr]["ss_cls"] += 1
                        sums[hr]["average_cls"] = sums[hr]["cls"] / sums[hr]["ss_cls"]

                    if sums[hr]["ttfb"] != 0:
                        sums[hr]["ss_ttfb"] += 1
                        sums[hr]["average_ttfb"] = sums[hr]["ttfb"] / sums[hr]["ss_ttfb"]
                    sums[hr]["average_lcp"] += oj_data[hr]["average_lcp"]
                    sums[hr]["average_fcp"] += oj_data[hr]["average_fcp"]
                    sums[hr]["average_cls"] += oj_data[hr]["average_cls"]
                    sums[hr]["average_ttfb"] += oj_data[hr]["average_ttfb"]
        # LIST_DATA_PROMETHEUS = []

        # average_lcp=  sums[hr].get("average_lcp")
        # average_fcp= sums[hr].get("average_fcp")
        # average_cls= sums[hr].get("average_cls")
        # average_ttfb= sums[hr].get("average_ttfb")
        # prometheus = Prometheus()
        # while True:


        while len(sums):
            print(sums)
            first_key = list(sums.items())[0][0]
            print(first_key)
            average_lcp = sums[first_key].get("average_lcp")
            average_fcp= sums[first_key].get("average_fcp")
            average_cls= sums[first_key].get("average_cls")
            average_ttfb= sums[first_key].get("average_ttfb")
            # for key_lcp in sums:
            #     print("first_key", key_lcp)
            #     average_lcp = sums[key_lcp]['average_lcp']
            #     prometheus = Prometheus()
            #     prometheus.get_promethus(key_lcp, "average_lcp", average_lcp)
            #     # sums.pop(key_lcp)
            # for key_fcp in sums:
            #     average_fcp = sums[key_fcp]['average_fcp']
            #     prometheus = Prometheus()
            #     prometheus.get_promethus(key_fcp, "average_fcp", average_fcp)
            # for key_cls in sums:
            #     average_cls = sums[key_cls]['average_cls']
            #     prometheus = Prometheus()
            #     prometheus.get_promethus(key_cls, "average_cls", average_cls)
            # for key_ttfb in sums:
            #     average_ttfb = sums[key_ttfb]['average_ttfb']
            #     prometheus = Prometheus()
            #     prometheus.get_promethus(key_ttfb, "average_ttfb", average_ttfb)
        #
            prometheus = Prometheus()
            prometheus.get_promethus(first_key, "average_lcp", average_lcp)
            prometheus.get_promethus(first_key, "average_fcp", average_fcp)
            prometheus.get_promethus(first_key, "average_cls", average_cls)
            prometheus.get_promethus(first_key, "average_ttfb", average_ttfb)
            sums.pop(first_key)
            print("5555555555555555", sums)
        print(sums)


        #     oj_value = {
        #         "domain": i,
        #         "average_lcp":sums[i].get("average_lcp"),
        #         "average_fcp":sums[i].get("average_fcp"),
        #         "average_cls":sums[i].get("average_cls"),
        #         "average_ttfb":sums[i].get("average_ttfb"),
        #     }
        #     LIST_DATA_PROMETHEUS.append(oj_value)
        # print("=====")
        # for dt in LIST_DATA_PROMETHEUS:
        #     domain = dt.get("domain")
        #     average_lcp = dt.get("average_lcp")
        #     average_fcp = dt.get("average_fcp")
        #     average_cls = dt.get("average_cls")
        #     average_ttfb = dt.get("average_ttfb")
        #     print(domain)
        #     while True:
        #         prometheus = Prometheus()
        #         prometheus.get_promethus(domain, "average_lcp", average_lcp)
        #         prometheus.get_promethus(domain, "average_fcp", average_fcp)
        #         prometheus.get_promethus(domain, "average_cls", average_cls)
        #         prometheus.get_promethus(domain, "average_ttfb", average_ttfb)
        #         pass




        # self.a_lcp.labels(sums[hr]).set(sums[hr]["average_lcp"])

    # def vailidat_value(self, hr, sums, oj_data, oj_domain):
    #     sum_ss_lcp = 0
    #     sum_ss_fcp = 0
    #     sum_ss_cls = 0
    #     sum_ss_ttfb = 0
    #     if hr not in sums:
    #         sums.update(oj_data)
    #     else:
    #         sums[hr]["lcp"] += oj_data[hr]["lcp"]
    #         sums[hr]["fcp"] += oj_data[hr]["fcp"]
    #         sums[hr]["cls"] += oj_data[hr]["cls"]
    #         sums[hr]["ttfb"] += oj_data[hr]["ttfb"]
    #     if oj_data[hr]["lcp"] != 0:
    #         sum_ss_lcp += 1
    #     sums[hr]["sum_ss_lcp"] = sum_ss_lcp
    #     if sums[hr]["fcp"] != 0:
    #         sum_ss_fcp += 1
    #     sums[hr]["sum_ss_fcp"] = sum_ss_fcp
    #     if sums[hr]["cls"] != 0:
    #         sum_ss_cls += 1
    #     sums[hr]["sum_ss_cls"] = sum_ss_cls
    #     if sums[hr]["ttfb"] != 0:
    #         sum_ss_ttfb += 1
    #     sums[hr]["sum_ss_ttfb"] = sum_ss_ttfb
    #
    #     print(sums)
    def vailidatlog(self, _lcp, _fcp, _cls, _ttfb):
        lcp = 0
        fcp = 0
        cls = 0
        ttfb = 0
        if _lcp != None and _lcp > 0:
            lcp = _lcp
        if _fcp != None and _fcp > 0:
            fcp = _fcp
        if _cls != None and _cls > 0:
            cls = _cls
        if _ttfb != None and _ttfb > 0:
            ttfb = _ttfb

        return lcp, fcp, cls, ttfb



