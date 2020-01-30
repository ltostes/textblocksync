import re
import json

regexp = "(?:{start}((?:.*?\r?\n?)*){end})+"

regex_specialchar_conversion = {
    r"*" : r"\*",
    r"+" : r"\+",
}

with open('syncblock.json', 'r') as f: 
    config = json.load(f)

for use in config['use_blocks']: 
    for block_name in use['blocks']: 
        
        block_file_path  = config['base_blocks'][block_name]['file']
        block_start = config['base_blocks'][block_name]['block_start']
        block_end = config['base_blocks'][block_name]['block_end']

        print('Start_pre: ',block_start)
        print('End_pre: ',block_start)
        # Fixing regex special chars that might be in the block_begin and block_end
        for special_char, replacement in regex_specialchar_conversion.items():
            block_start = block_start.replace(special_char,replacement)
            block_end = block_end.replace(special_char,replacement)

        print('Start_post: ',block_start)
        print('End_post: ',block_start)

        into_file_path = use['file']

        with open(block_file_path, 'r') as f: 
            block_file = f.read()
        
        with open(into_file_path, 'r') as f: 
            into_file = f.read()
        
        r = re.compile(regexp.format(start=block_start,end=block_end))

        source_block = r.findall(block_file)[0]

        out_file = into_file

        for occurence in r.findall(into_file):
            out_file = out_file.replace(occurence,source_block)
        
        with open(into_file_path, 'w+') as f: 
            f.write(out_file)
        
        print('Placed ', block_name,' from file: ', block_file_path ,' into file: ',into_file_path)