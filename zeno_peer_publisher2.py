import zenoh, random, time

random.seed()

def read_temp():
    return random.randint(15, 30)

if __name__ == "__main__":
    session = zenoh.open({"mode":"peer"})
    key = 'myhome/kitchen/temp2'
    pub = session.declare_publisher(key)
    while True:
        t = read_temp()
        buf = t
        print(f"Putting Data ('{key}': {buf})...")
        pub.put(buf)
        time.sleep(1)