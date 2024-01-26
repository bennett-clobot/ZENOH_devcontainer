import zenoh, random, time

random.seed()

def read_temp():
    return random.randint(15, 30)

if __name__ == "__main__":
    session = zenoh.open({"mode":"client","connect":{"endpoints":["tcp/127.0.0.1:7447"]}})
    key = 'tmp'
    pub = session.declare_publisher(key)
    while True:
        t = read_temp()
        buf = f"{t}"
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(buf)
        time.sleep(1)