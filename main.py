import logging
import math
import sys
from pathlib import Path


# Настройка логирования
logs_dir = Path(__file__).resolve().parent / "Logs"
logs_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | [%(levelname)-7s] | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(logs_dir / "file_txt.log", encoding="utf-8"),
    ],
)

logging.info("Логгер сконфигурирован")


def triangle_info(
    side_a: str,
    side_b: str,
    side_c: str,
) -> tuple[str, list[tuple[int, int]]]:
    """Определяет вид треугольника и координаты его вершин."""

    invalid_coordinates = [(-2, -2)] * 3
    error_coordinates = [(-1, -1)] * 3

    # Преобразуем введённые строки в числа
    try:
        a, b, c = float(side_a), float(side_b), float(side_c)
    except ValueError:
        logging.error("Введены нечисловые данные")
        return "", invalid_coordinates

    # Числа должны быть конечными и положительными
    if not all(math.isfinite(side) and side > 0 for side in (a, b, c)):
        logging.error("Длины сторон должны быть конечными положительными числами")
        return "не треугольник", error_coordinates

    # Проверяем неравенство треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        logging.warning("Из введённых длин нельзя составить треугольник")
        return "не треугольник", error_coordinates

    # Определяем тип треугольника
    if a == b == c:
        triangle_type = "равносторонний"
    elif a == b or a == c or b == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    # Строим вершины:
    # A = (0, 0), B = (c, 0), AC = b, BC = a
    x = (b * b + c * c - a * a) / (2 * c)
    y_squared = b * b - x * x
    y = math.sqrt(max(0.0, y_squared))

    # Масштабируем треугольник, чтобы он поместился в поле 100 × 100
    padding = 5
    available_size = 100 - 2 * padding
    scale = min(available_size / c, available_size / y)

    point_a = (padding, 100 - padding)
    point_b = (round(padding + c * scale), 100 - padding)
    point_c = (
        round(padding + x * scale),
        round(100 - padding - y * scale),
    )

    coordinates = [point_a, point_b, point_c]
    logging.info("Определён тип треугольника: %s", triangle_type)
    logging.debug("Координаты вершин: %s", coordinates)

    return triangle_type, coordinates


def main() -> None:
    logging.info("Приложение запущено")
    print("Введите длины сторон треугольника — по одной на строку:")

    try:
        side_a = input("Сторона A: ")
        side_b = input("Сторона B: ")
        side_c = input("Сторона C: ")
    except EOFError:
        logging.error("Не удалось получить все три значения")
        return

    triangle_type, coordinates = triangle_info(side_a, side_b, side_c)

    print("Тип треугольника:", triangle_type)
    print("Координаты вершин:", coordinates)


if __name__ == "__main__":
    main()
