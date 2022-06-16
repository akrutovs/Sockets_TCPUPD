from urllib import request

resource = request.urlopen('http://example.com')

print(resource.status)
print(resource.getcode())
print(resource.msg)
print(resource.headers)
print(resource.headers.get('Content-Type'))