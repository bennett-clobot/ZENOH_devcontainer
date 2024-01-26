import zenoh, time

def listener(sample):
    print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.decode('utf-8')}')")

if __name__ == "__main__":
    session = zenoh.open({"mode":"client","connect":{"endpoints":["tcp/127.0.0.1:7447"]}})
    print(session)
    sub = session.declare_subscriber('tmp', listener)
    #time.sleep(60)
    time.sleep(1)