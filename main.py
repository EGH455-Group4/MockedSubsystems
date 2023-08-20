from threading import Thread

from sample.handler import Handler as SampleHandler
from image.handler import Handler as ImageHandler
from web_server.handler import Handler as WebServerHandler

def main():
    sample = SampleHandler("9090")
    image = ImageHandler("9091")
    web = WebServerHandler("9092")

    sample_server_thread = Thread(daemon=True, target=sample.Run)

    sample_server_thread.start()

    web_server_thread = Thread(daemon=True, target=web.Run)

    web_server_thread.start()

    image.Run()

if __name__ == "__main__":
    main()
