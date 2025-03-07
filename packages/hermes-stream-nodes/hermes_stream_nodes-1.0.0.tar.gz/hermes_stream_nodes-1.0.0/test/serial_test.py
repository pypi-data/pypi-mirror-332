import time

from hermes_stream_nodes import SerialStream


def main():
    stream = SerialStream(SerialStream.Config(port="COM28", baudrate=115200))
    stream.init()
    bytes_read = 0
    print_timestamp = time.time()

    while True:
        time.sleep(0.1)
        data = stream.read()
        bytes_read += len(data)

        if time.time() - print_timestamp > 1:
            print(f"Data rate: {bytes_read * 8 / 1000:.2f} kbps")
            bytes_read = 0
            print_timestamp = time.time()


if __name__ == "__main__":
    main()
