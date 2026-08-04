from config import APP_NAME, VERSION

from engine.logger import setup_logger
from engine.utils import create_folders


def main():
    create_folders()

    logger = setup_logger()

    logger.info("Программа запущена")

    print(f"{APP_NAME} v{VERSION}")
    print("Все системы готовы")


if __name__ == "__main__":
    main()
