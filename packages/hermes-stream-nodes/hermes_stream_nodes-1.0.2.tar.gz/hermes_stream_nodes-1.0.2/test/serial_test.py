import time

from hermes_stream_nodes import SerialStream


def main():
    stream = SerialStream(SerialStream.Config(port="COM28", baudrate=4000000))
    stream.init()

    assert stream.statistics is not None

    print_timestamp = time.time()

    while True:
        time.sleep(0.05)
        last_transmission = stream.read()

        if time.time() - print_timestamp > 1:
            print_timestamp = time.time()
            stats = stream.statistics.get_rates()

            print(f"Data rate: {stats.rx_rate / 1000:.2f} kbps")
            print(list(last_transmission.split(b"\0")[1]))
            

if __name__ == "__main__":
    main()
