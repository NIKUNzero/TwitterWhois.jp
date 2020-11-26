import conf
import tweepy
import subprocess
import platform
import random, string
import time
import whois11

auth = tweepy.OAuthHandler(conf.CA, conf.CS)
auth.set_access_token(conf.AT, conf.AS)
api = tweepy.API(auth)


def random_domain(int):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(int)]
   return ''.join(randlst)

def main():
    while True:
        number = [1,2,3,4,5,6,7,8,9,10,11,12]
        count = random.choice(number)
        try:
            domain = (random_domain(count) + ".jp")
            param = '-n' if platform.system().lower()=='windows' else '-c'
            command = ['ping', param, '1', domain]
            print(domain)
            print(subprocess.call(command) == 0)
            if True == (subprocess.call(command) == 0):
                print("ドメインが発見されました")
                try:
                    api.update_status("発見されたJPドメイン: 【" + domain.lower() + "】\n" + whois11.whois(domain)[398:580] + "(以下略")
                    print("ツイートに成功しました")
                except Exception as e:
                    print("ツイートに失敗しました")
                time.sleep(1500)
        except Exception as e:
            time.sleep(1)

main()