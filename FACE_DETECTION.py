import cv2
import dlib

# Инициализация детектора лиц dlib
face_detector = dlib.get_frontal_face_detector()

# Загрузка изображения
image_path = "C:/Users/tolma/Downloads/6.jpg"
img = cv2.imread(image_path)

# Проверка, что изображение успешно загружено
if img is None:
    print(f"Не удалось загрузить изображение по пути: {image_path}")
    exit()

# Преобразование в оттенки серого для улучшения скорости обработки
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Детекция лиц на кадре
faces = face_detector(gray)

# Отрисовка прямоугольников вокруг обнаруженных лиц
for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Вывод информации о количестве обнаруженных лиц
num_faces = len(faces)
cv2.putText(img, f"Detected Faces: {num_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Отображение результата
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
