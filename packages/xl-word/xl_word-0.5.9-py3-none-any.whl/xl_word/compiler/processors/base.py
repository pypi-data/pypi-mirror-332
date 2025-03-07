import re
from typing import Dict, List, Optional


class BaseProcessor:
    """XML处理器基类"""
    def process(self, xml: str) -> str:
        raise NotImplementedError

    def _process_tag(self, xml: str, pattern: str, process_func) -> str:
        """通用标签处理方法"""
        matches = list(re.finditer(pattern, xml, re.DOTALL))
        for match in reversed(matches):
            replacement = process_func(match)
            xml = xml[:match.start()] + replacement + xml[match.end():]
        return xml

    def _extract_attrs(self, attrs_str: str, attr_names: List[str]) -> Dict[str, Optional[str]]:
        """提取属性值"""
        result = {}
        for name in attr_names:
            match = re.search(f'{name}="([^"]*)"', attrs_str)
            result[name] = match.group(1) if match else None
        return result

    def _build_props(self, props: List[str], indent: str = '') -> str:
        """构建属性字符串"""
        if not props:
            return ''
        return f'\n{indent}' + f'\n{indent}'.join(props) + f'\n{indent}'
