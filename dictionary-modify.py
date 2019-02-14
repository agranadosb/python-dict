# -*- coding: utf-8 -*-

class ChangesDicts():
    def change_dict(self, dicti, key, value): 
        """ Function that changes the value of a key given
            :param dicti: Dict to change
            :param key: Key of the value to change
            :param value: Value to be changed
            :return: Dictionary with the value changed, if the key isn't on the dictionary,
                     the dictionary won't be changed """
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