from inspect import signature
import importlib

global_aliases = {}


def alias_information(name):
    if name in global_aliases:
        print("Alias Name: ", name)
        print("Alias Functions: ", end='\n')
        for index, item in enumerate(global_aliases[name][0]):
            print(index, " Function: ", item, " #, of Parameters: ", global_aliases[name][1][index])
    else:
        print("There is no alias by that name...!")


def call_alias(name, data_storage=None):
    results = None
    if name in global_aliases:
        for index, item in enumerate(global_aliases[name][0]):
            mod_name, func_name = item.rsplit('.', 1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            if data_storage:
                if len(data_storage) == 0:
                    results = func()
                else:
                    if isinstance(data_storage[index], (list,)):
                        if 'results' in data_storage[index]:
                            for iterator, piece in enumerate(data_storage[index]):
                                if piece == 'results':
                                    data_storage[index][iterator] = results
                                    break
                        results = func(*data_storage[index])
                    elif isinstance(data_storage[index], (dict,)):
                        if 'results' in data_storage[index].values():
                            for key, value in data_storage[index].items():
                                if value == 'results':
                                    data_storage[index][key] = results
                                    break
                        results = func(**data_storage[index])
            else:
                results = func()
    else:
        print("There is no alias by that name...!")

    return results


def create_alias(name, functions):
    if name not in global_aliases:
        if isinstance(functions, (list,)):
            list_of_parameters = list()
            number_of_parameters = 0
            for item in functions:
                mod_name, func_name = item.rsplit('.', 1)
                mod = importlib.import_module(mod_name)
                func = getattr(mod, func_name)
                sig = signature(func)
                list_of_parameters.append(len(sig.parameters))
                number_of_parameters += len(sig.parameters)
            global_aliases[name] = (functions, list_of_parameters)
        else:
            sig = signature(functions)
            global_aliases[name] = (functions, len(sig.parameters), len(sig.parameters))
    else:
        print("There is an alias by that name already...!")


def delete_alias(name):
    try:
        del global_aliases[name]
        return 1
    except KeyError:
        print("No alias by that name in the system...!")
        return 0


def load_aliases(file_path):
    pass

def save_aliases():
    pass