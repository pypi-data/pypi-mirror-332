from xl_word.compiler.processors.base import BaseProcessor
import re


class ParagraphProcessor(BaseProcessor):
    """处理段落相关的XML标签"""
    def process(self, xml: str) -> str:
        def process_paragraph(match):
            style_str = match.group(1) or ''
            content = match.group(2).strip()
            
            styles = {}
            if style_str:
                styles = dict(pair.split(':') for pair in style_str.split(';') if pair.strip())

            p_props = ['<w:pPr>']
            if styles.get('align'):
                p_props.append(f'            <w:jc w:val="{styles["align"]}"/>')
                
            # Add spacing if padding-top or padding-bottom exists
            spacing_attrs = []
            if styles.get('padding-top'):
                spacing_attrs.append(f'w:before="{styles["padding-top"]}"')
            if styles.get('padding-bottom'):
                spacing_attrs.append(f'w:after="{styles["padding-bottom"]}"')
            if spacing_attrs:
                p_props.append(f'            <w:spacing {" ".join(spacing_attrs)}/>')
                
            p_props.append('        </w:pPr>')

            r_props = ['            <w:rPr>']
            if styles.get('english') and styles.get('chinese'):
                r_props.append(f'                <w:rFonts w:ascii="{styles["english"]}" w:cs="{styles["chinese"]}" ' + 
                             f'w:eastAsia="{styles["english"]}" w:hAnsi="{styles["english"]}" w:hint="eastAsia"/>')
            if styles.get('font-size'):
                r_props.append(f'                <w:kern w:val="0"/>')
                r_props.append(f'                <w:sz w:val="{styles["font-size"]}"/>')
                r_props.append(f'                <w:szCs w:val="{styles["font-size"]}"/>')
            if styles.get('font-weight') == 'bold':
                r_props.append('                <w:b/>')
            r_props.append('            </w:rPr>')

            # if not re.search(r'<xl-span>(.*?)</xl-span>', content):
            #     content = f'<xl-span>{content}</xl-span>'

            span_match = re.search(r'<xl-span>(.*?)</xl-span>', content)
            text = span_match.group(1) if span_match else content

            p_props_str = '\n'.join(p_props)
            r_props_str = '\n'.join(r_props)
            return f'<w:p>\n{p_props_str}\n        <w:r>\n{r_props_str}\n            <w:t>{text}</w:t>\n        </w:r></w:p>'
            
        data = self._process_tag(xml, r'<xl-p[^>]*?(?:style="([^"]+)")?\s*>(.*?)</xl-p>', process_paragraph)
        return data