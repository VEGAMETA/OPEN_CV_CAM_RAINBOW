import cv2

import asyncio

VIDEO_CAPTURE_SOURCE = 0


async def main():
    cap = cv2.VideoCapture(VIDEO_CAPTURE_SOURCE)
    hue = cap.get(cv2.CAP_PROP_HUE)
    print("Started")
    while True:
        hue += 1
        if hue >= 180:
            hue = -hue
        cap.set(cv2.CAP_PROP_HUE, hue)
        await asyncio.sleep(0.01)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        quit("Exited")
