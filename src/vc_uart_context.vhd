-- This Source Code Form is subject to the terms of the Mozilla Public
-- License, v. 2.0. If a copy of the MPL was not distributed with this file,
-- You can obtain one at http://mozilla.org/MPL/2.0/.
--
-- Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

context vc_uart_context is
  library vunit_lib;
  context vunit_lib.vc_axi_context;
  use vunit_lib.uart_pkg.all;
end context;
