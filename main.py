from threading import Thread

from sample.handler import Handler as SampleHandler
from target.handler import Handler as TargetHandler

def main():
    sample = SampleHandler("9090")
    target = TargetHandler("9091")

    sample_server_thread = Thread(daemon=True, target=sample.Run)

    sample_server_thread.start()

    target.Run()

if __name__ == "__main__":
    main()
