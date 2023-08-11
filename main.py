from threading import Thread

from sample.handler import Handler as SampleHandler
from image.handler import Handler as ImageHandler

def main():
    sample = SampleHandler("9090")
    image = ImageHandler("9091")

    sample_server_thread = Thread(daemon=True, target=sample.Run)

    sample_server_thread.start()

    image.Run()

if __name__ == "__main__":
    main()
