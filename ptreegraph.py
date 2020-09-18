import requests
from graphviz import Digraph


class JSONImport:

    @classmethod
    def get_json(cls, package_name):
        url = 'https://pypi.org/pypi/' + package_name + '/json'
        try:
            content = requests.get(url).json()
            return content
        except Exception as e:
            print(e)


def get_requires(pkg_name):
    try:
        r_json = JSONImport.get_json(pkg_name)['info']['requires_dist']
        req = []

        if r_json is not None:
            for i in r_json:
                if not ('extra' in i):
                    req.append(i.split(' ', 1)[0])
            req.sort(key=str.casefold)
        return req
    except TypeError:
        print('JSON is None')


def get_all_requires(pkg_name):
    req = {}
    list_r = get_requires(pkg_name)
    if list_r:
        for i in list_r:
            req[i] = get_all_requires(i)
    else:
        return

    return req


def dict_to_graphviz(pkg_name, dic, d):
    if dic:
        for key, value in dic.items():
            d.edge(pkg_name, key)
            if value is not None:
                dict_to_graphviz(key, value, d)


def main():
    pkg_n = input()
    d = Digraph(name='dependencies')
    requires = get_all_requires(pkg_n)
    dict_to_graphviz(pkg_n, requires, d)
    if requires:
        print(d.source)


main()
