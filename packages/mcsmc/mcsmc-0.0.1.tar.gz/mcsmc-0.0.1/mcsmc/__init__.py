'''
author: xiaoliang(笔名)
email: 2700858939
updata_time: 2025/03/09
'''
import requests,json
had = {
    "Content-Type":"application/json; charset=utf-8",
    "X-Requested-With":"XMLHttpRequest"
}
class Mcsm_ctrl():
    def __init__(self, url, token):
        '''
        mcsm控制初始化
        url:mcsm地址
        token:mcsm的token
        :param url:
        :param token:
        '''
        self.url = url
        self.token = token
    def q_restart(self, server_id, de_id)->tuple:
        '''
        强制重启
        server_id:实例id
        de_id:节点id
        :param server_id:
        :param de_id:
        :return:->tuple
        '''
        url = self.url + "/api/protected_instance/kill?apikey="+self.token+"&uuid="+server_id+"&daemonId="+de_id
        data = {
            "uuid":server_id,
            "daemonId":de_id
        }
        res = requests.get(url, data=json.dumps(data), headers=had)
        match res.json()["status"]:
            case 200:
                #启动
                #GET /api/protected_instance/open
                url = self.url + "/api/protected_instance/open?apikey="+self.token+"&uuid="+server_id+"&daemonId="+de_id
                data = {
                    "uuid":server_id,
                    "daemonId":de_id
                }
                res = requests.get(url, data=json.dumps(data), headers=had)
                if res.json()["status"] == 200:
                    return (True,res.text)
                else:
                    return (False,res.text)
            case _:
                return (False,res.text)
    def get_err(self, server_id, de_id)->tuple:
        '''
        错误检测(只能检测oom)
        server_id:实例id
        de_id:节点id
        :param server_id:
        :param de_id:
        :return:->tuple
        '''
        url = self.url + "/api/protected_instance/outputlog?apikey="+self.token+"&uuid="+server_id+"&daemonId="+de_id+"&size=100"
        data = {
            "uuid":server_id,
            "daemonId":de_id,
            "size":200
        }
        res = requests.get(url, data=json.dumps(data), headers=had)
        if res.json()["status"] == 200:
            if "OutOfMemory" in res.json()["data"]:
                return (True,res.text)
            else:
                return (False,res.text)
        else:
            return (False,res.text)