# m=8
# a=lambda x,y : (x * m) /y
# print(a(2,3))

import requests
r = requests.get("https://analytics.usa.gov/data/live/ie.json")
print(r.json())
print(r.json()['totals']['ie_version']['6.0'])
print(r.json()['totals']['ie_version']['9.10'])


# map=7
#
# def func():
#  return map
#
#
# print(func())

# class A(object):
#  def __repr__(self):
#   return 'instance of a'
#
#
# a=A()
# b=a
# del a
# print(b)
#
# class A:
#  pass
# class B:
#  pass
#
#
# a=A()
# b=B()
#
# print(type(a))
# print(type(a) == type(b), type(a), type(b))
