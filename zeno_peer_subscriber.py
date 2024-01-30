import zenoh, time

def listener(sample):
    print(f"Received {sample.kind} ('{sample.key_expr}': {sample.payload.decode('utf-8')})")

if __name__ == "__main__":
    session = zenoh.open({"mode":"peer"})
    print(session)
    sub = session.declare_subscriber('myhome/kitchen/*', listener)
    #sub1 = session.declare_subscriber('myhome/kitchen/temp2', listener)
    time.sleep(1)