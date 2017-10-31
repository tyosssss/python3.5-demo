# coding=utf-8
def request(url):
    return HttpRequest(url)


class HttpRequest:
    def __init__(self, url):
        self.url = url

    def get_status_code(self):
        if self.url.find('http://') >= 0:
            return 200
        else:
            raise TypeError('The url is invalid.')

    def __enter__(self):
        print('[Enter %s] Allocate resource', self.url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[Exit %s] Free resource', self.url)

        if exc_val is None:
            print('[Exit %s] Exited no exception', self.url)
        else:
            print('[Exit %s] Exited with exception raised', self.url)


# 请求1
with request('http://www.baidu.com') as req:
    print('statusCode : ', req.get_status_code())

# 请求2
with request('www.aa.com') as req:
    print('statusCode : ', req.get_status_code())
