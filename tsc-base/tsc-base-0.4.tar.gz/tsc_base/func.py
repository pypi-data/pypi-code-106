from pprint import pprint
import inspect
import heapq
from typing import Dict, Any
import random


def get_func_para(func, del_para=None, add_para: dict = None):
    """提取函数的参数和默认值, 没有默认值设为 None
    比如可以用于设定 TaskDB.result 的例子

    Args:
        func (list, function): 单/多个函数组成的列表, 后面函数出现一样的参数会覆盖前面的默认值
        del_para (set, list, optional): 删除不想看到返回的参数
        add_para (dict, optional): 增加想补充的参数和值, 会覆盖原始值, 不会被 del_para 删除

    Returns:
        dict: 所有函数修剪后的参数和默认值
    """
    paras = {}
    func = func if isinstance(func, list) else [func]
    del_para = set(del_para) if del_para else set()
    add_para = add_para if add_para else {}
    for f in func:
        fullargspec = inspect.getfullargspec(f)
        defaults = fullargspec.defaults if fullargspec.defaults else []
        defaults = [None] * (len(fullargspec.args) - len(defaults)) + list(defaults)
        paras.update({k: v for k, v in zip(fullargspec.args, defaults) if k not in del_para})
    paras.update(add_para)
    return paras


def cover_dict(new_para: dict, default_para: dict):
    """使用 new_para 中的健值对递归覆盖 default_para 中的值, 遇到非 dict 就不再递归而直接覆盖, 出现类型不一样也会直接覆盖
    比如可以用于新参数覆盖旧参数 (注意因为失误导致的参数覆盖)

    Args:
        new_para (dict): 不能出现 default_para 中没有的 key
        default_para (dict): 被覆盖的

    Returns:
        dict: default_para
    """
    for k, v in new_para.items():
        assert k in default_para, f'构建了默认参数中没有的参数: {k} not in {set(default_para)}'
        if isinstance(v, dict) and isinstance(default_para[k], dict):
            cover_dict(v, default_para[k])
        else:
            default_para[k] = v
    return default_para


def get(key, obj, default=None):
    """
    递归从dict/list/tuple中取值, 以list的形式，以避免中括号取值数量不灵活的问题
    :param key: list/tuple/int/str; list表示递归取值
    :param obj: dict/list/tuple
    :param default: 寻找不到后返回的默认值
    :return:
    """
    key = key if isinstance(key, list) else [key]
    if len(key) == 0:
        return default
    for i in key:
        try:
            obj = obj[i]
        except:
            obj = default
            break
    return obj


def arg_extreme_dict(d: Dict[Any, Dict], dv_key=None, dv_reverse=True, allow_type=None, ban_type=None, traverse_d=None,
                     result=None, root=None):
    """给d中的每个v排序, v中递归的每个元素都排序(只取最大值或最小值), 排序结果的极值用d的k表示

    Args:
        d (Dict[Any, Dict]): 双层字典, 第二层的每个字典构造格式保持一致, 只允许值不一样
        dv_key (dict, function, optional): d中v的每个值使用的排序function, 输入是 (d的k,递归后v值) 对, 输出可排序值
            输入 function 类型就是统一针对所有v的方法
        dv_reverse (dict, bool, optional): d中v的每个值取最大值还是最小值, 默认都是True最大值, 使用dict可针对每个v值选择顺序(不在dict中的还是默认值)
        allow_type (set, list, optional): d中v中的值允许排序的类型, 默认见代码
        ban_type (set, list, optional): d中v中的值不允许排序的类型, 使用这个 allow_type 会失效. 使用时建议加入 dict
        traverse_d (dict, optional): 默认是d中第一个v中的值, 用于确定排序对象有哪些k
        result (dict, optional): 用于递归存储结果, 不可以赋值
        root (list, optional): 用于递归存储路径, 不可以赋值

    Returns:
        dict: result
    """
    allow_type = {int, float} if allow_type is None else set(allow_type)
    ban_type = {} if ban_type is None else set(ban_type)
    result = {} if result is None else result
    root = [] if root is None else root
    if traverse_d is None:  # 默认排序对象
        for v in d.values():
            traverse_d = v
            break
    for k, v in traverse_d.items():
        result[k] = {}
        type_v = type(v)
        if (len(ban_type) == 0 and type_v not in allow_type) or (len(ban_type) > 0 and type_v in ban_type):  # 不是允许的类型
            if type_v is dict:  # 是dict就递归
                arg_extreme_dict(d, dv_key=dv_key, dv_reverse=dv_reverse, allow_type=allow_type, ban_type=ban_type,
                                 traverse_d=traverse_d[k], result=result[k], root=root + [k])
        else:
            root_ = root + [k]
            key = dv_key if inspect.isfunction(dv_key) else get(root_, dv_key, lambda t: t[1])  # 排序方式
            reverse = dv_reverse if isinstance(dv_reverse, bool) else get(root_, dv_reverse, True)  # 最大还是最小值排序
            sort_ = heapq.nlargest if reverse else heapq.nsmallest
            result[k] = sort_(1, [(k1, get(root_, v1, v1)) for k1, v1 in d.items()], key=key)[0][0]
    return result


if __name__ == '__main__':
    class c:
        def __init__(self) -> None:
            pass

        @staticmethod
        def f(a, b=2, c=3, **kw):
            pass
    # get_func_para
    print('=' * 10, 'get_func_para')
    print(get_func_para(c), get_func_para(c.f))

    # cover_dict
    print('=' * 10, 'cover_dict')
    new_para = {'a': [1, 2, {'bb': 2}], 'b': {'c': (1, 2), 'd': 2}}
    default_para = {'a': [4, 2, {'b': 21}], 'b': {'c': (1, 1), 'd': 22, 'e': None}}
    pprint(cover_dict(new_para, default_para))

    # arg_extreme_dict
    print('=' * 10, 'arg_extreme_dict')
    epoch = {
        str(i): {
            i2: {
                i3: random.randint(1, 100) for i3 in ['P', 'R', 'F1']
            } for i2 in ['train', 'dev', 'test']
        } for i in range(5)
    }
    print('原始值:')
    pprint(epoch)
    print('极值:')
    pprint(arg_extreme_dict(epoch, dv_reverse=True, ban_type=[dict], dv_key=lambda t: -t[1]))
