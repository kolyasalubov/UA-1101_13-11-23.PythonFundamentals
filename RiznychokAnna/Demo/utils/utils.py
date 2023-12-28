import logging


def format_str(text: str) -> str:
    """
    Replace necessary characters with '//' and original character. Return text that appropriate to Telegram Bot API requirements.
    :param text: Original text to format
    :return: Formatted text
    """
    return (text.replace(",", "\\,").replace(".", "\\.").replace("-", "\\-")
            .replace("`", "\\`").replace("(", "\\(").replace(")", "\\)")
            .replace(":", "\\:").replace("_", "\\_"))


def setup_logs():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s [%(levelname)s]:  %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
