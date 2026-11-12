import cv2
import time

# Source video dan ukuran window
VIDEO_SOURCE = "assets/test_video.mp4"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

def main():
    # Ambil dan buka video dari sumber
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        print("ERROR: Gagal membuka video dari sumber!")
        return
    
    prev_time = 0
    print("INFO: Tekan [q] pada tab video untuk keluar")

    while True:
        # Ambil gambar dan simpan ke frame sebagai matriks piksel gambar
        # ret bernilai true jika gambar berhasil diambil
        ret, frame = cap.read()
        if not ret:
            if isinstance(VIDEO_SOURCE, str):
                # Video habis, ulang videonya dari detik 0
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            break

        # Ubah ukuran ke yang sesuai dan buat titik tengah
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        center_x = FRAME_WIDTH // 2 # (double slash agar bentuknya int)
        center_y = FRAME_HEIGHT // 2

        # Hitung FPS dengan rumus 1 / delta_time
        curr_time = time.time()
        delta_time = curr_time - prev_time

        if delta_time > 0.00001:
            fps = 1 / delta_time
        else:
            fps = 0

        prev_time = curr_time

        # Buat garis vertikal dan horizontal tengah, serta lingkaran titik kamera
        cv2.line(frame, (center_x, 0), (center_x, FRAME_HEIGHT), (200, 200, 200), 1)
        cv2.line(frame, (0, center_y), (FRAME_WIDTH, center_y), (200, 200, 200), 1)
        cv2.circle(frame, (center_x, FRAME_HEIGHT - 10), 5, (0, 255, 255), -1)

        # Tampilkan FPS dan Resolusi di window
        cv2.putText(frame, f"FPS: {fps:.1f} | Res: {FRAME_WIDTH}x{FRAME_HEIGHT}",
                    (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Tampilkan window capture
        cv2.imshow("ASV Camera Pipeline", frame)

        # Jeda 33 milidetik agar videonya tidak terlalu cepat
        # Jika user tekan 'q', loop berhenti
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

    # Menutup window secara aman dan bersih
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()