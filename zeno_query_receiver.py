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
from zenoh import config, Sample, Value


key = 'key/expression'
value = 'request ack'
complete = True
def queryable_callback(query):
    print(f">> [Queryable ] Received Query '{query.selector}'"
           + (f" with value: {query.value.payload.decode('utf-8')}" if query.value is not None else ""))
    time.sleep(1)
    query.reply(Sample(key, value))
    print(f"send query reply key : '{key}', value : '{value}'")

def query_receiver():
    # initiate logging
    zenoh.init_logger()

    print("Opening session...")
    session = zenoh.open({"mode":"peer"})

    print("Declaring Queryable on '{}'...".format(key))
    queryable = session.declare_queryable(keyexpr=key, handler=queryable_callback, complete=complete)

    print("Enter 'q' to quit...")
    c = '\0'
    while c != 'q':
        c = sys.stdin.read(1)
#        if c != 'q':
#            print("getting")
#            session.get(key, print, consolidation=zenoh.QueryConsolidation.NONE())
#            time.sleep(1)

    queryable.undeclare()
    session.close()

if __name__ == '__main__':
    query_receiver()