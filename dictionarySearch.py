# -*- coding: utf-8 -*-

def search_key(key, tree):
    """Function that search a key in a dictionary or json

    :param tree: Dict to be searched

    :param key: Key to search

    :return: True if the key is finded, False if not"""
    if isinstance(tree,(list,tuple)):
        aux = False
        for subItem in tree:
            aux = search_key(key, subItem)
            if aux:
                break
        return aux
    elif isinstance(tree,dict):
        for nodeName in tree.keys():
            subTree = tree[nodeName]
            if nodeName == key:
                aux = True
                break
            else:
                aux = search_key(key, subTree)
                if aux:
                    break
        return aux

def search_value_key(key, tree, value):
    """Function that search a value of a key in a dictionary or json

    :param tree: Dict to be searched

    :param key: Key to search

    :param value: Key to search

    :return: True if the value is finded, False if not"""
    if isinstance(tree,(list,tuple)):
        aux = False
        for subItem in tree:
            aux = search_key(key, subItem)
            if aux:
                break
        return aux
    elif isinstance(tree,dict):
        aux = False
        for nodeName in tree.keys():
            subTree = tree[nodeName]
            if nodeName == key:
                if tree[key] == value:
                    aux = True
                break
            else:
                aux = search_key(key, subTree)
                if aux:
                    break
        return aux