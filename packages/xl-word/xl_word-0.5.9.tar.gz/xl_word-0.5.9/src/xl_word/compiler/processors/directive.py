from xl_word.compiler.processors.base import BaseProcessor
import re


class DirectiveProcessor(BaseProcessor):
    """处理Vue指令相关的XML标签"""
    def process(self, xml: str) -> str:
        xml = self._process_v_if(xml)
        xml = self._process_v_for(xml)
        return xml
        
    def _process_v_if(self, xml: str) -> str:
        def process_if(match):
            tag_name, condition, remaining_attrs = match.groups()
            close_tag_pattern = f'</\s*{tag_name}\s*>'
            close_match = re.search(close_tag_pattern, xml[match.end():])
            if close_match:
                content_between = xml[match.end():match.end() + close_match.start()]
                return f'{{% if {condition} %}}<{tag_name}{remaining_attrs}>{content_between}</{tag_name}>{{% endif %}}'
            return match.group(0)
            
        return self._process_tag(xml, r'<([^>]*)\s+v-if="([^"]*)"([^>]*)>', process_if)

    def _process_v_for(self, xml: str) -> str:
        def process_for(match):
            tag_name, loop_expr, remaining_attrs = match.groups()
            item, items = loop_expr.split(' in ')
            item = item.strip()
            items = items.strip()
            
            close_tag_pattern = f'</\s*{tag_name}\s*>'
            close_match = re.search(close_tag_pattern, xml[match.end():])
            if close_match:
                content_between = xml[match.end():match.end() + close_match.start()]
                return f'{{% for {item} in {items} %}}<{tag_name}{remaining_attrs}>{content_between}</{tag_name}>{{% endfor %}}'
            return match.group(0)
            
        return self._process_tag(xml, r'<([^>]*)\s+v-for="([^"]*)"([^>]*)>', process_for)
