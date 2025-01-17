import requests, json
server = '192.168.247.145'

def check_xss(url, param_info, s):
        pattern1 ="'<script>document.write('k13k5d2')</script>"

        # connect test
        res = s.get(url, params=param_info['url_param'], data=json.dumps(param_info['post_param']))
        if res.status_code != 200:
                return False

        # url_param test
        for key in param_info['url_param'].keys():
                temp_param = param_info['url_param']
                temp_param[key] = pattern1

                res = s.post(url, params=temp_param, data=json.dumps(param_info['post_param']))

                if res.text.find(pattern1) != -1:
                        print('the text is found!')
                        return True

        # post_param test

        # cookie_param test
        print('the text is not found')
        return False


with requests.Session() as s:
        # get cookie
        url = 'http://'+server+'/bWAPP/login.php'
        # login
        post_param = {'login':'bee','password':'bug','security_level':'0','form':'submit'}
        res = s.post(url, data=post_param)
        print(s.cookies)
        
        # connect after login
        url = 'http://{}/bWAPP/htmli_get.php'.format(server)
        res = s.post(url)
        print(res)
        print(res.text)
        
        # check xss
        url = 'http://{}/bWAPP/htmli_get.php'.format(server)
        url_param = {'firstname':None, 'lastname':None, 'form':'submit'}
        post_param = {'':''}
        cookie_param = {'':''}
        param_info = {'url_param':url_param, 'post_param':post_param}
        
        check_xss(url, param_info, s)