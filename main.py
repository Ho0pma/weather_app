from coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import ApiServiceError, CantGetCoordinates


def main():
    try:
        coordinates = get_coordinates()
    except CantGetCoordinates:
        print('Не удалось получить GPS координаты')
        exit(1)
    try:
        weather = get_weather(coordinates)
    except CantGetCoordinates:
        print(f'Не удалось получить сведения о погоде по координатам: {coordinates}')
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    main()

