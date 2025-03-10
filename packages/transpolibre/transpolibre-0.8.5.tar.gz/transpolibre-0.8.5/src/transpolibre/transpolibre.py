import argparse
import gettext
import logging
import os
import polib
import re
from dotenv import load_dotenv
from libretranslatepy import LibreTranslateAPI
from pycountry import languages
from transpolibre._version import __version__
from typing import Any, Dict, List, Optional

load_dotenv()

LOCALE_DIR = "locale"
LANGUAGE = os.getenv("LANG", "en")

gettext.bindtextdomain("transpolibre", LOCALE_DIR)
gettext.textdomain("transpolibre")
_ = gettext.gettext


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=_("Translate PO files with LibreTranslate")
    )
    parser.add_argument(
        "-a",
        "--api-key",
        help=_("LibreTranslate API key"),
        type=str,
        default=os.getenv("LT_API_KEY"),
    )

    parser.add_argument(
        "-d",
        "--debug",
        help=_("Debugging"),
        action="store_true",
    )

    parser.add_argument(
        "-f",
        "--file",
        help=_("PO file to translate"),
        type=str,
    )

    parser.add_argument(
        "-l",
        "--list",
        help=_("List available languages"),
        action="store_true",
    )

    parser.add_argument(
        "-o",
        "--overwrite",
        help=_("Overwrite existing translations"),
        action="store_true",
    )

    parser.add_argument(
        "-s",
        "--source-lang",
        help=_("Source Language ISO 639 code (Default en)"),
        default="en",
        type=str,
    )

    parser.add_argument(
        "-t",
        "--target-lang",
        help=_("Target Language ISO 639 code (Default es)"),
        default="es",
        type=str,
    )

    parser.add_argument(
        "-u",
        "--url",
        help=_("LibreTranslate URL (Default http://127.0.0.1:8000)"),
        default=os.getenv("LT_URL", "http://127.0.0.1:8000"),
        type=str,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help=_("Increase output verbosity"),
        action="count",
        default=0,
    )

    parser.add_argument(
        "-V",
        "--version",
        help=_("Show version"),
        action="version",
        version=f"{__version__}",
    )

    return parser.parse_args()


def get_lang_name(iso_code: str) -> str:
    try:
        if len(iso_code) == 2:
            lang = languages.get(alpha_2=iso_code)
        elif len(iso_code) == 3:
            lang = languages.get(alpha_3=iso_code)
        else:
            raise KeyError
        return lang.name
    except (KeyError, TypeError):
        print(_(f"Error: unknown language code: " + iso_code))
        exit(1)


def trans_pofile(
    SRCISO: str, TARGETISO: str, URL: str, APIKEY: str, POFILE: str, OVERWRITE: bool
) -> None:
    if not os.path.isfile(POFILE):
        raise FileNotFoundError(
            _(f"The specified PO file does not exist or is not a file: " + POFILE)
        )

    logging.debug(_("Read PO file: ") + POFILE)

    pofile = polib.pofile(POFILE, encoding="utf-8")

    for entry in pofile:
        pomsgid = entry.msgid
        pomsgstr = entry.msgstr
        pomsg = f"msgid: {pomsgid}\nmsgstr: {pomsgstr}\n"

        if not pomsgstr or OVERWRITE:
            trans_str = trans_msg(pomsgid, SRCISO, TARGETISO, URL, APIKEY)
            logging.debug(pomsg)
            logging.info(_(f"Original:    ") + pomsgid)
            logging.info(_(f"Translation: ") + trans_str + ("\n"))

            update_pofile(POFILE, pomsgid, trans_str)


def update_pofile(POFILE: str, pomsgid: str, trans_str: str) -> None:
    pofile = polib.pofile(POFILE, encoding="utf-8")

    for entry in pofile:
        if entry.msgid == pomsgid:
            entry.msgstr = trans_str
            break

    with open(POFILE, "w", encoding="utf-8") as f:
        pofile.save()


def trans_msg(msg: str, SRCISO: str, TARGETISO: str, URL: str, APIKEY: str) -> str:
    # Regular expressions to find strings with web URLs or email addresses
    url_pattern = r"`([^`]+) <(https?://[^\s>]+)>`_"
    email_pattern = r"<([\w\.-]+@[\w\.-]+\.\w+)>"

    lt = LibreTranslateAPI(URL, APIKEY)

    # Find all links in the message and replace them with placeholders
    def translate_link(match: re.Match[str]) -> str:
        text, url = match.groups()
        logging.debug(_(f"Translating link text: ") + text + ("with URL: ") + url)
        translated_text = lt.translate(text, SRCISO, TARGETISO)

        # Reconstruct the link with the translated text
        return f"`{translated_text} <{url}>`_"

    if re.search(url_pattern, msg) or re.search(email_pattern, msg):
        if re.search(url_pattern, msg):
            logging.debug(_("URL detected"))
            trans_str = re.sub(url_pattern, translate_link, msg)

        if re.search(email_pattern, msg):
            logging.debug(_("Email detected"))
            trans_str = msg

    else:
        logging.debug(_("No URL or Email detected"))
        trans_str = lt.translate(msg, SRCISO, TARGETISO)

    logging.debug(_("LibreTranslate URL: ") + URL)
    logging.debug(_("API Key: ") + (str(APIKEY) if APIKEY is not None else _("None")))
    logging.debug(_("Translating: ") + msg)
    logging.debug(_("Source ISO 639: ") + SRCISO)
    logging.debug(_("Target ISO 639: ") + TARGETISO)
    logging.debug(_("Translation: ") + trans_str)

    return trans_str


def trans_list(URL: str, APIKEY: Optional[str]) -> None:
    lt = LibreTranslateAPI(URL, APIKEY)
    languages = lt.languages()
    for language in languages:
        code = language.get("code", "N/A")
        name = language.get("name", "N/A")
        targets = ", ".join(language.get("targets", []))

        print(_("Language: ") + name)
        print(_("Code: ") + code)
        print(_("Targets: ") + targets)
        print()
    exit(0)


def main() -> None:
    args = parse_arguments()

    SRCISO = args.source_lang
    TARGETISO = args.target_lang
    URL = args.url
    APIKEY = args.api_key
    POFILE = args.file
    LIST = args.list
    DEBUG = args.debug
    VERBOSE = args.verbose
    OVERWRITE = args.overwrite

    if DEBUG:
        log_level = logging.DEBUG
    elif VERBOSE > 0:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING

    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    SRCLANG = get_lang_name(SRCISO)
    TARGETLANG = get_lang_name(TARGETISO)

    if LIST:
        trans_list(URL, APIKEY)
    else:
        if not POFILE:
            print(_("Error: file is required."))
            exit(1)
        try:
            trans_pofile(SRCISO, TARGETISO, URL, APIKEY, POFILE, OVERWRITE)
        except FileNotFoundError as e:
            print(e)


if __name__ == "__main__":
    main()
