from jinja2 import Environment, BaseLoader, TemplateNotFound
from typing import Dict, Any
from xl_word.compiler.processors import BaseProcessor, StyleProcessor, DirectiveProcessor, \
TableProcessor, ParagraphProcessor, SignatureProcessor, PagerProcessor


class ImageProcessor(BaseProcessor):
    """处理图片相关的XML标签"""
    def process(self, xml: str) -> str:
        def process_image(match):
            attrs = self._extract_attrs(match.group(0), ['src', 'width', 'height'])
            rid = attrs['src']
            width = attrs['width']
            height = attrs['height']
            
            return f'''<w:pict>
                            <v:shape style="width:{width}px;height:{height}px">
                                <v:imagedata r:id="{rid}"/>
                            </v:shape>
                        </w:pict>'''
            
        return self._process_tag(xml, r'<xl-img[^>]+/>', process_image)


class XMLTemplateLoader(BaseLoader):
    def __init__(self, template_str: str):
        self.template_str = template_str

    def get_source(self, environment: Environment, template: str) -> tuple:
        if template == 'root':
            return self.template_str, None, lambda: True
        raise TemplateNotFound(template)

class XMLCompiler:
    """XML编译器主类"""
    def __init__(self):
        self.processors = [
            StyleProcessor(),
            DirectiveProcessor(), 
            TableProcessor(),
            SignatureProcessor(),
            ParagraphProcessor(),
            ImageProcessor(),
            PagerProcessor()
        ]
        self.env = Environment(
            loader=XMLTemplateLoader(""),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True
        )

    def _preprocess_template(self, template: str) -> str:
        template = template.replace('xl:tr', 'w:tr')
        template = template.replace('xl:td', 'w:td')
        template = template.replace('xl:th', 'w:th')
        
        for processor in self.processors:
            template = processor.process(template)
            
        return template

    def compile(self, template: str, data: Dict[str, Any]) -> str:
        processed_template = self._preprocess_template(template)
        
        env = Environment(
            loader=XMLTemplateLoader(processed_template),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        template = env.get_template('root')
        result = template.render(**data)
        
        return result
