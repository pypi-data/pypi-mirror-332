from typing import Any, List, Optional, Union

import numpy as np


class ValueUtils:
    @staticmethod
    def to_value(text: str, data_type: Optional[type] = None) -> Optional[Any]:
        """
        将文本转换为数值
        :param text: 文本
        :param data_type: 数据类型
        """
        if text is None or not isinstance(text, str):
            return None

        text = text.strip()
        if data_type == int:
            try:
                return int(text)
            except ValueError:
                return None
        elif data_type == float:
            try:
                if text.endswith('%'):
                    return float(text[:-1]) / 100

                return float(text)
            except ValueError:
                return None
        elif data_type == bool:
            text = text.lower()
            return text in ['true', 'yes', 't', 'y', '1']
        elif data_type == list:
            return eval(text)
        elif data_type == dict:
            return eval(text)
        else:
            return text

    @staticmethod
    def to_values(text: str, data_type: Optional[type] = None, sep: str = ' ') -> List[Any]:
        if text is None or not isinstance(text, str):
            return []

        text = text.strip()
        items = text.split(sep)
        return [ValueUtils.to_value(item, data_type) for item in items]

    @staticmethod
    def to_string(value: Optional[Union[int, float, bool, str]],
                  decimal_places: int=6,
                  decimal_places_of_zero: int=1,
                  scientific: bool = False,
                  none_default: str = None) -> str:
        """
        将给定的值转换为字符串表示
        :param value: 要转换的值，支持 int, float, bool, 和 str 类型
        :param decimal_places: 指定浮点数保留的最大小数位数，默认为 6
        :param decimal_places_of_zero: 当浮点数的值为整数或接近整数时，最少保留的小数位数，默认为 1
        :param scientific: 是否强制使用科学记数法格式，默认为 False
        :param none_default: 当数据(int或float)为None时对应的缺省字符串
        :return: 转换为字符串的值，格式根据参数动态调整
        详细说明:
        1. 整数、布尔值、字符串类型: 直接转换为字符串。

        2. 根据数值范围决定是否使用科学记数法:
            - 如果值的绝对值大于等于 1e8 或 (不为零并且绝对值小于 1e-3)，默认使用科学记数法。
            - 整数类型始终不使用科学记数法，除非显式指定使用科学计数法

        3. 浮点数的常规格式:
            - 如果浮点数为整数（即小数部分全为零），按 `decimal_places_of_zero` 指定的小数位数格式化。
            - 如果浮点数有小数部分，则按 `decimal_places` 指定的小数位数格式化。
            - 格式化后的小数部分会移除多余的零，但确保至少保留 `decimal_places_of_zero` 个小数位。
        """
        if value is None:
            return none_default

        if isinstance(value, str) or isinstance(value, bool):
            return str(value)
        else:
            if abs(value) >= 1e8 or (value != 0 and abs(value) < 1e-3):
                scientific = True
            elif isinstance(value, int):
                scientific = False

            if scientific:
                return ValueUtils.number_to_scientific(value, decimal_places)

            if isinstance(value, float):
                if value.is_integer():
                    return f"{value:.{decimal_places_of_zero}f}"
                else:
                    formatted_value = f"{value:.{decimal_places}f}"
                    # 确保小数位末尾的零的个数符合要求
                    if '.' in formatted_value:
                        integer_part, decimal_part = formatted_value.split('.')
                        decimal_part = decimal_part.rstrip('0')
                        if len(decimal_part) < decimal_places_of_zero:
                            decimal_part += '0' * (decimal_places_of_zero - len(decimal_part))
                        formatted_value = f"{integer_part}.{decimal_part}"
                    return formatted_value
            elif isinstance(value, bool):
                return str(value)
            elif isinstance(value, int):
                return f"{round(value)}"

    @staticmethod
    def to_native(value: Any) -> Any:
        """
        将值转换为原生类型，如果可能
        :param value: 原始值
        :return: 转换后的原生类型值
        """
        if isinstance(value, (np.integer, int)):
            return int(value)  # 转换为 Python 的 int 类型
        elif isinstance(value, (np.floating, float)):
            return float(value)  # 转换为 Python 的 float 类型
        elif isinstance(value, (np.bool_, bool)):
            return bool(value)  # 转换为 Python 的 bool 类型
        else:
            return str(value)  # 保留为字符串

    @staticmethod
    def number_to_scientific(value: Union[int,float], decimal_places: int = 6) -> str:
        """
        将 float 数字转换为科学计数法表示的字符串。

        参数：
        :param value: float 数字
        :param decimal_places: 小数位数，默认为 6
        :return: 科学计数法表示的字符串
        """
        exponent = int(f"{value:e}".split('e')[1])
        coefficient = f"{value / (10 ** exponent):.{decimal_places}f}".rstrip('0').rstrip('.')
        if '.' in coefficient:
            integer_part, decimal_part = coefficient.split('.')
            if len(decimal_part) < decimal_places:
                decimal_part += '0' * (decimal_places - len(decimal_part))
            coefficient = f"{integer_part}.{decimal_part}"
        else:
            coefficient += '.' + '0' * decimal_places
        return f"{coefficient}e{exponent}"

    @staticmethod
    def get_type(value: Any) -> Optional[type]:
        """
        判断输入值的数据类型

        参数:
        value: 要判断的数据

        返回:
        str: 数据类型
        """
        if isinstance(value, int):
            return int
        elif isinstance(value, float):
            return float
        elif isinstance(value, complex):
            return complex
        elif isinstance(value, bool):
            return bool
        elif isinstance(value, str):
            return str
        else:
            return None