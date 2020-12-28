import json
import requests

wps_sid = 'V02SOFZMeD7lI82BztucygmN5D3qLTI00adb9cca003d8ac75f'

cookie = {
    'wps_sid': wps_sid
}

s = requests.session()

qs = ['1', '2', '3', '4', '1|2|3', '2|3|4', '1|2', '1|3', '1|4', '2|3', '2|4', '3|4', '1|2|3|4']

for k in ('PC_task_knowledge', 'pc_task_konwMembers'):
    questionbank = []
    for j in range(11):
        for i in qs:
            verify_q = 'https://vip.wps.cn/questionbank/verify'
            data ={
                'task_tag': k,
                'position': k,
                'answers[%s]'%j: i
            }
            r = s.post(verify_q, cookies=cookie, data = data)
            isOK = json.loads(r.text)['result']
            if isOK == 'ok':
                questionbank.append('%s:%s'%(j,i))
                break
    print(k)
    print(questionbank)
