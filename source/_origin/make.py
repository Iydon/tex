#!/usr/bin/env python
from macro_parser import parse_macro_in

from utils import config, sh


parse_macro_in(config.macros_file, cache=True)
parse_macro_in(config.info_file, cache=True)

for file in sh.recursive_folder(ignores=config.ignore_dirs):
	content = parse_macro_in(file, cache=True)
	target = sh.join_path(config.target_path, file)
	sh.write_file(target, content)
