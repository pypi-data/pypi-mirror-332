from xl_word.compiler.processors.base import BaseProcessor
import re


class TableProcessor(BaseProcessor):
    """处理表格相关的XML标签"""
    def process(self, xml: str) -> str:
        xml = self._process_xl_table(xml)
        xml = self._process_xl_th(xml)
        xml = self._process_xl_tr(xml)
        xml = self._process_xl_tc(xml)
        return xml
        
    def _process_xl_table(self, xml: str) -> str:
        def process_table(match):
            style_str, content = match.groups()
            content = content.strip()
            styles = dict(pair.split(':') for pair in style_str.split(';') if pair.strip())
            
            tbl_props = []
            if 'align' in styles:
                tbl_props.append(f'<w:jc w:val="{styles["align"]}"/>')
            if styles.get('border') == 'none':
                tbl_props.append('''<w:tblBorders>
                <w:top w:color="auto" w:space="0" w:sz="0" w:val="none"/>
                <w:left w:color="auto" w:space="0" w:sz="0" w:val="none"/>
                <w:bottom w:color="auto" w:space="0" w:sz="0" w:val="none"/>
                <w:right w:color="auto" w:space="0" w:sz="0" w:val="none"/>
                <w:insideH w:color="auto" w:space="0" w:sz="0" w:val="none"/>
                <w:insideV w:color="auto" w:space="0" w:sz="0" w:val="none"/>
            </w:tblBorders>''')
            else:
                tbl_props.append('''<w:tblBorders>
                    <w:top w:color="auto" w:space="0" w:sz="4" w:val="single"/>
                    <w:left w:color="auto" w:space="0" w:sz="4" w:val="single"/>
                    <w:bottom w:color="auto" w:space="0" w:sz="4" w:val="single"/>
                    <w:right w:color="auto" w:space="0" w:sz="4" w:val="single"/>
                    <w:insideH w:color="auto" w:space="0" w:sz="4" w:val="single"/>
                    <w:insideV w:color="auto" w:space="0" w:sz="4" w:val="single"/>
                </w:tblBorders>''')
            
            tbl_props.extend([
                '<w:tblW w:type="auto" w:w="0"/>',
                '<w:tblInd w:type="dxa" w:w="0"/>',
                '''<w:tblCellMar>
                    <w:top w:type="dxa" w:w="0"/>
                    <w:left w:type="dxa" w:w="0"/>
                    <w:bottom w:type="dxa" w:w="0"/>
                    <w:right w:type="dxa" w:w="0"/>
                </w:tblCellMar>'''
            ])
            
            return f'''<w:tbl>
                    <w:tblPr>
                        {chr(10).join(tbl_props)}
                    </w:tblPr>{content}</w:tbl>'''
            
        return self._process_tag(xml, r'<xl-table[^>]*?style="([^"]*)"[^>]*>(.*?)</xl-table>', process_table)
    def _process_xl_th(self, xml: str) -> str:
        def process_th(match):
            content = match.group(1)
            # Add font-weight:bold to all xl-p tags inside xl-tc
            def add_bold_style(tc_match):
                tc_attrs, tc_content = tc_match.groups()
                
                def add_bold_to_p(p_match):
                    full_tag = p_match.group(0)
                    if 'style="' in full_tag:
                        haha = re.sub(r'style="([^"]*)"', 
                                    lambda m: f'style="{m.group(1)};font-weight:bold"' if 'font-weight' not in m.group(1) else m.group(0), 
                                    full_tag)
                        return haha
                    else:
                        return full_tag.replace('<xl-p', '<xl-p style="font-weight:bold"')
                
                tc_content = re.sub(r'<xl-p[^>]*>.*?</xl-p>', add_bold_to_p, tc_content, flags=re.DOTALL)
                return f'<xl-tc {tc_attrs}>{tc_content}</xl-tc>'
            
            content = re.sub(r'<xl-tc\s+([^>]+)>(.*?)</xl-tc>', add_bold_style, content, flags=re.DOTALL)
            return f'<xl-tr header="1">{content}</xl-tr>'
            
        return self._process_tag(xml, r'<xl-th>(.*?)</xl-th>', process_th)
    
    def _process_xl_tr(self, xml: str) -> str:
        def process_tr(match):
            attrs, content = match.groups()
            tr_props = []
            
            # Handle special properties
            if 'header' in attrs:
                tr_props.append('                    <w:tblHeader/>')
            if 'cant-split' in attrs:
                tr_props.append('                    <w:cantSplit/>')
            
            height_match = re.search(r'height="(\d+)"', attrs)
            if height_match:
                height = height_match.group(1)
                tr_props.append(f'                    <w:trHeight w:val="{height}"/>')
            
            # Copy over remaining attributes except header and cant-split
            other_attrs = re.findall(r'(\w+)="([^"]*)"', attrs)
            filtered_attrs = [(k,v) for k,v in other_attrs if k not in ['header', 'cant-split']]
            attrs_str = ' '.join([f'{k}="{v}"' for k,v in filtered_attrs])
            
            tr_props_str = self._build_props(tr_props, '                ') if tr_props else ''
            if tr_props_str:
                tr_props_str = f'\n                <w:trPr>{tr_props_str}</w:trPr>'
            
            return f'<w:tr{" " + attrs_str if attrs_str else ""}>{tr_props_str}{content}</w:tr>'
            
        return self._process_tag(xml, r'<xl-tr([^>]*)>(.*?)</xl-tr>', process_tr)

    def _process_xl_tc(self, xml: str) -> str:
        def process_tc(match):
            attrs, content = match.groups()
            attrs_dict = self._extract_attrs(attrs, ['width', 'span', 'align', 'merge'])
            has_merge_attr = 'merge' in attrs

            if not re.search(r'<[^>]+>', content):
                content = f'<xl-p>{content}</xl-p>'
            tc_props = []
            if attrs_dict['width']:
                tc_props.append(f'<w:tcW w:type="dxa" w:w="{attrs_dict["width"]}"/>')
            if attrs_dict['span']:
                tc_props.append(f'<w:gridSpan w:val="{attrs_dict["span"]}"/>')
            if attrs_dict['align']:
                tc_props.append(f'<w:vAlign w:val="{attrs_dict["align"]}"/>')
            if attrs_dict['merge']=='start':
                tc_props.append('<w:vMerge w:val="restart"/>')
            elif has_merge_attr:
                tc_props.append('<w:vMerge/>')
                
            tc_props_str = self._build_props(tc_props, '                    ')
            return f'<w:tc>\n                    <w:tcPr>{tc_props_str}</w:tcPr>{content}</w:tc>'
            
        data  = self._process_tag(xml, r'<xl-tc\s+([^>]+)>(.*?)</xl-tc>', process_tc)
        return data