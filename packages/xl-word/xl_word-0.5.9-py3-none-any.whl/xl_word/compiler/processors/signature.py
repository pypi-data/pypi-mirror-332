from xl_word.compiler.processors.base import BaseProcessor


class SignatureProcessor(BaseProcessor):
    """处理签名相关的XML标签"""
    def process(self, xml: str) -> str:
        def process_signature(match):
            data_var, height = match.groups()
            height = height.replace('px', '')
            
            return f'''<w:r>
                       <w:pict>
                           <v:shape style="height:{height}px;width:{{{{ {height}*{data_var}['width']/{data_var}['height'] }}}}px">
                               <v:imagedata r:id="{{{{%s['rid']}}}}"/>
                           </v:shape>
                       </w:pict> 
                    </w:r>''' % data_var
                    
        data = self._process_tag(xml, r'<xl-signature\s+:data="([^"]+)"\s+:height="([^"]+)"\s*/>', process_signature)
        return data