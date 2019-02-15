# -*- coding: utf-8 -*-

class ChangesDicts():
    def change_dict(self, dicti, key, value): 
        """Function that changes the value of a key given of a dictionary or json

        :param dicti: Dict to change
    
        :param key: Key of the value to change
    
        :param value: Value to be changed
    
        :return: Dictionary with the value changed, if the key isn't on the dictionary, the dictionary won't be changed """
        if isinstance(dicti,(list,tuple)):
            res = []
            for subItem in dicti:
                result = self.change_dict(key, subItem, value)
                res.append(result)
            return result
        elif isinstance(dicti,dict):
            for nodeName in dicti.keys():
                subTree = dicti[nodeName]
                if nodeName == key:
                    dicti[nodeName] = value
                    break
                else:
                    dicti[nodeName] = self.change_dict(key, subTree, value)
            return dicti
        elif isinstance(dicti, str):
            return dicti

    def changes_dict(self, tree, change):
        """Function that changes the values of a json with the keys given

        :param tree: Json to be changed

        :param change: Dictionary with the keys to be changed and the new values: {field1: value1, field2: value2,..., fieldN: valueN}"""
        if isinstance(tree,(list,tuple)):
            res = []
            for subItem in tree:
                result = self.changes_dict(subItem, change)
                res.append(result)
            return result
        elif isinstance(tree,dict):
            for nodeName in tree.keys():
                subTree = tree[nodeName]
                if nodeName in list(change.keys()):
                    tree[nodeName] = {'value': str(change[nodeName])}
                    change.pop(nodeName)
                    if not change:
                        break
                else:
                    tree[nodeName] = self.changes_dict(subTree, change)
            return tree
        elif isinstance(tree, str):
            return tree