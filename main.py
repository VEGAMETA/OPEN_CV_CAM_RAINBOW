import cv2

import asyncio


async def main():
    cap = cv2.VideoCapture(0)
    hue = cap.get(cv2.CAP_PROP_HUE)
    print("Start hue is ", hue)
    while True:
        try:
            hue += 1
            if hue == 180:
                hue = -hue

            cap.set(cv2.CAP_PROP_HUE, hue)
            await asyncio.sleep(0.01)
        except KeyboardInterrupt:
            quit("exited")


if __name__ == "__main__":
    asyncio.run(main())
