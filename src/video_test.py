import cv2
import time

VIDEO_SOURCE = "assets/test_video.mp4"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

def main():
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        print("ERROR: Gagal membuka video dari sumber!")
        return

    prev_time = 0
    print("INFO: Tekan [q] pada tab video untuk keluar")

    while True:
        ret, frame = cap.read()
        if not ret:
            if isinstance(VIDEO_SOURCE, str):
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            break

        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        center_x = FRAME_WIDTH // 2
        center_y = FRAME_HEIGHT // 2

        curr_time = time.time()
        delta_time = curr_time - prev_time

        if delta_time > 0.00001:
            fps = 1 / delta_time
        else:
            fps = 0

        prev_time = curr_time

        cv2.line(frame, (center_x, 0), (center_x, FRAME_HEIGHT), (200, 200, 200), 1)
        cv2.line(frame, (0, center_y), (FRAME_WIDTH, center_y), (200, 200, 200), 1)
        cv2.circle(frame, (center_x, FRAME_HEIGHT - 10), 5, (0, 255, 255), -1)

        cv2.putText(frame, f"FPS: {fps:.1f} | Res: {FRAME_WIDTH}x{FRAME_HEIGHT}",
                    (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("ASV Camera Pipeline", frame)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()