import cv2
import dlib

                                            # Инициализация детектора лиц dlib
detector = dlib.get_frontal_face_detector()

                                            # Загрузка изображения или видеопотока (замените "path/to/your/image.jpg" на путь к вашему файлу)
image_path = "path/to/your/image.jpg"
cap = cv2.VideoCapture(image_path)

                                            # Чтение изображения или видеопотока
while True:
    ret, frame = cap.read()

                                            # Прекращаем цикл, если изображение закончилось
    if not ret:
        break

                                            # Преобразование в оттенки серого для улучшения скорости обработки
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                                            # Детекция лиц на кадре
    faces = detector(gray)

                                            # Отрисовка прямоугольников вокруг обнаруженных лиц
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                                            # Отображение результата
    cv2.imshow("Face Detection", frame)

                                            # Прекращаем выполнение при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

                                            # Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
