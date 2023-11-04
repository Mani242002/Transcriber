from googletrans import Translator
import PyPDF2
from docx import Document
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
def supported_languages(source,dest):
    supported_languages = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi",
    "bn": "Bengali",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
    "tr": "Turkish",
    "el": "Greek",
    "vi": "Vietnamese",
    "th": "Thai",
    "sv": "Swedish",
    "no": "Norwegian",
    "fi": "Finnish",
    "da": "Danish",
    "is": "Icelandic",
    "he": "Hebrew",
    "cs": "Czech",
    "sk": "Slovak",
    "bg": "Bulgarian",
    "uk": "Ukrainian",
    "ro": "Romanian",
    "ms": "Malay",
    "fil": "Filipino",
    "et": "Estonian",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "sl": "Slovenian",
    "sr": "Serbian",
    "hr": "Croatian",
    "bs": "Bosnian",
    "sq": "Albanian",
    "mk": "Macedonian",
    "cy": "Welsh",
    "gl": "Galician",
    "eu": "Basque",
    "hy": "Armenian",
    "ka": "Georgian",
    "az": "Azerbaijani",
    "uz": "Uzbek",
    "kk": "Kazakh",
    "ky": "Kyrgyz",
    "tg": "Tajik",
    "mn": "Mongolian",
    "ne": "Nepali",
    "kn": "Kannada",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ml": "Malayalam",
    "mr": "Marathi",
    "si": "Sinhalese",
    "be": "Belarusian",
    "lmn": "Armenian (Lingua franca Nova)",
    "mt": "Maltese",
    "ga": "Irish",
    "gd": "Scots Gaelic",
    "fy": "Frisian",
    "lb": "Luxembourgish",
    "ht": "Haitian Creole",
    "st": "Sesotho",
    "sn": "Shona",
    "sd": "Sindhi",
    "yi": "Yiddish",
    "eo": "Esperanto",
    "hmn": "Hmong",
    "mi": "Maori",
    "haw": "Hawaiian",
    "la": "Latin",
    "xh": "Xhosa",
    "yo": "Yoruba",
    "zu": "Zulu",
    }
    if source or dest in supported_languages:
        return True
    else:
        return False
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return str(e)

def read_pdf_file(file_path):
    try:
        pdf_content = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_content += page.extractText()
        return pdf_content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return str(e)

def read_word_file(file_path):
    try:
        doc = Document(file_path)
        doc_content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return doc_content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return str(e)

def read_file(file_path):
    if file_path.endswith('.txt'):
        return read_text_file(file_path)
    elif file_path.endswith('.pdf'):
        return read_pdf_file(file_path)
    elif file_path.endswith('.docx'):
        return read_word_file(file_path)
    else:
        return "Unsupported file format"
def available_languages():
    supported_languages = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi",
    "bn": "Bengali",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
    "tr": "Turkish",
    "el": "Greek",
    "vi": "Vietnamese",
    "th": "Thai",
    "sv": "Swedish",
    "no": "Norwegian",
    "fi": "Finnish",
    "da": "Danish",
    "is": "Icelandic",
    "he": "Hebrew",
    "cs": "Czech",
    "sk": "Slovak",
    "bg": "Bulgarian",
    "uk": "Ukrainian",
    "ro": "Romanian",
    "ms": "Malay",
    "fil": "Filipino",
    "et": "Estonian",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "sl": "Slovenian",
    "sr": "Serbian",
    "hr": "Croatian",
    "bs": "Bosnian",
    "sq": "Albanian",
    "mk": "Macedonian",
    "cy": "Welsh",
    "gl": "Galician",
    "eu": "Basque",
    "hy": "Armenian",
    "ka": "Georgian",
    "az": "Azerbaijani",
    "uz": "Uzbek",
    "kk": "Kazakh",
    "ky": "Kyrgyz",
    "tg": "Tajik",
    "mn": "Mongolian",
    "ne": "Nepali",
    "kn": "Kannada",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ml": "Malayalam",
    "mr": "Marathi",
    "si": "Sinhalese",
    "be": "Belarusian",
    "lmn": "Armenian (Lingua franca Nova)",
    "mt": "Maltese",
    "ga": "Irish",
    "gd": "Scots Gaelic",
    "fy": "Frisian",
    "lb": "Luxembourgish",
    "ht": "Haitian Creole",
    "st": "Sesotho",
    "sn": "Shona",
    "sd": "Sindhi",
    "yi": "Yiddish",
    "eo": "Esperanto",
    "hmn": "Hmong",
    "mi": "Maori",
    "haw": "Hawaiian",
    "la": "Latin",
    "xh": "Xhosa",
    "yo": "Yoruba",
    "zu": "Zulu",
    }
    supported_languages = {key: value for key, value in sorted(supported_languages.items(), key=lambda item: item[1])}
    return supported_languages




