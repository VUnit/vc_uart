# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

from os import environ
from os.path import join, dirname, abspath
from vunit import VUnit


root = dirname(__file__)
src_path = join(root, "src")

ui = VUnit.from_argv()
ui.add_osvvm()

wh = ui.add_verification_components()

try:
    if environ['CI']:
        wh['AXI']['path'] = abspath(join(root, '..', '..', 'vc_axi'))
except KeyError as err:
    print('Could not retrieve envvar', err)

wh['UART']['path'] = abspath(join(root, '..', '..'))
ui.use_verification_components(wh, ['UART'])

ui.add_library("uart_lib").add_source_files(join(src_path, "*.vhd"))
ui.add_library("tb_uart_lib").add_source_files(join(src_path, "test", "*.vhd"))

ui.main()
