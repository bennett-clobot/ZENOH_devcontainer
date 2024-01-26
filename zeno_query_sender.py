#
# Copyright (c) 2022 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#

import sys
import time
import argparse
import json
import zenoh
from zenoh import config, QueryTarget


key = 'key/expression'
#selector.set_parameters()
# Zenoh code  --- --- --- --- --- --- --- --- --- --- ---
def query_send():
    # initiate logging
    #zenoh.init_logger()
    
    print("Opening session...")
    session = zenoh.open({"mode":"peer"})
    print("Sending Query '{}'...".format(key))
    replies = session.get(selector=key, handler=zenoh.Queue(), value={'test':'request'}, 
        consolidation=zenoh.QueryConsolidation.NONE(),target=zenoh.QueryTarget.ALL_COMPLETE())
    for reply in replies.receiver:
        try:
            print(">> Received ('{}': '{}')"
                .format(reply.ok.key_expr, reply.ok.payload.decode("utf-8")))
        except:
            print(">> Received (ERROR: '{}')"
                .format(reply.err.payload.decode("utf-8")))
    session.close()

if __name__ == '__main__':
    query_send()