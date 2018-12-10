#
# Wordless: Initialization of Global Settings
#
# Copyright (C) 2018 Ye Lei (叶磊) <blkserene@gmail.com>
#
# License: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#

import nltk

from wordless_measures import *

def init_settings_global(main):
    main.settings_global = {
        'langs': {
            main.tr('Afrikaans'): 'afr',
            main.tr('Armenian'): 'hye',
            main.tr('Asturian'): 'ast',
            main.tr('Albanian'): 'sqi',
            main.tr('Arabic'): 'ara',
            main.tr('Azerbaijani'): 'aze',
            main.tr('Basque'): 'eus',
            main.tr('Belarusian'): 'bel',
            main.tr('Bengali'): 'ben',
            main.tr('Breton'): 'bre',
            main.tr('Bulgarian'): 'bul',
            main.tr('Catalan'): 'cat',
            main.tr('Chinese (Simplified)'): 'zho_CN',
            main.tr('Chinese (Traditional)'): 'zho_TW',
            main.tr('Croatian'): 'hrv',
            main.tr('Czech'): 'ces',
            main.tr('Danish'): 'dan',
            main.tr('Dutch'): 'nld',
            main.tr('English'): 'eng',
            main.tr('Esperanto'): 'epo',
            main.tr('Estonian'): 'est',
            main.tr('Finnish'): 'fin',
            main.tr('French'): 'fra',
            main.tr('Galician'): 'glg',
            main.tr('German'): 'deu',
            main.tr('Greek'): 'ell',
            main.tr('Gujarati'): 'guj',
            main.tr('Hausa'): 'hau',
            main.tr('Hebrew'): 'heb',
            main.tr('Hindi'): 'hin',
            main.tr('Hungarian'): 'hun',
            main.tr('Indonesian'): 'ind',
            main.tr('Irish'): 'gle',
            main.tr('Islandic'): 'isl',
            main.tr('Italian'): 'ita',
            main.tr('Japanese'): 'jpn',
            main.tr('Kannada'): 'kan',
            main.tr('Kazakh'): 'kaz',
            main.tr('Korean'): 'kor',
            main.tr('Kurdish'): 'kur',
            main.tr('Latin'): 'lat',
            main.tr('Latvian'): 'lav',
            main.tr('Lithuanian'): 'lit',
            main.tr('Macedonian'): 'mkd',
            main.tr('Malay'): 'msa',
            main.tr('Malayalam'): 'mal',
            main.tr('Maltese'): 'mlt',
            main.tr('Manx'): 'glv',
            main.tr('Marathi'): 'mar',
            main.tr('Nepali'): 'nep',
            main.tr('Norwegian'): 'nor',
            main.tr('Punjabi'): 'pan',
            main.tr('Persian'): 'fas',
            main.tr('Polish'): 'pol',
            main.tr('Portuguese'): 'por',
            main.tr('Romanian'): 'ron',
            main.tr('Russian'): 'rus',
            main.tr('Scottish Gaelic'): 'gla',
            main.tr('Serbian'): 'srp',
            main.tr('Slovak'): 'slk',
            main.tr('Slovene'): 'slv',
            main.tr('Sotho, Southern'): 'sot',
            main.tr('Somali'): 'som',
            main.tr('Spanish'): 'spa',
            main.tr('Swahili'): 'swa',
            main.tr('Swedish'): 'swe',
            main.tr('Tagalog'): 'tgl',
            main.tr('Tajik'): 'tgk',
            main.tr('Tamil'): 'tam',
            main.tr('Telugu'): 'tel',
            main.tr('Thai'): 'tha',
            main.tr('Turkish'): 'tur',
            main.tr('Ukrainian'): 'ukr',
            main.tr('Urdu'): 'urd',
            main.tr('Vietnamese'): 'vie',
            main.tr('Welsh'): 'cym',
            main.tr('Yoruba'): 'yor',
            main.tr('Zulu'): 'zul',

            main.tr('Other Languages'): 'other'
        },

        'lang_codes': {
            'afr': 'af',
            'hye': 'hy',
            'ast': 'ast',
            'sqi': 'sq',
            'ara': 'ar',
            'aze': 'az',
            'eus': 'eu',
            'bel': 'be',
            'ben': 'bn',
            'bre': 'br',
            'bul': 'bg',
            'cat': 'ca',
            'zho_CN': 'zh_CN',
            'zho_TW': 'zh_TW',
            'hrv': 'hr',
            'ces': 'cs',
            'dan': 'da',
            'nld': 'nl',
            'eng': 'en',
            'epo': 'eo',
            'est': 'et',
            'fin': 'fi',
            'fra': 'fr',
            'glg': 'gl',
            'deu': 'de',
            'ell': 'el',
            'guj': 'gu',
            'hau': 'ha',
            'heb': 'he',
            'hin': 'hi',
            'hun': 'hu',
            'ind': 'id',
            'gle': 'ga',
            'isl': 'is',
            'ita': 'it',
            'jpn': 'ja',
            'kan': 'kn',
            'kaz': 'kk',
            'kor': 'ko',
            'kur': 'ku',
            'lat': 'la',
            'lav': 'lv',
            'lit': 'lt',
            'mkd': 'mk',
            'msa': 'ms',
            'mal': 'ml',
            'mlt': 'mt',
            'glv': 'gv',
            'mar': 'mr',
            'nep': 'ne',
            'nor': 'no',
            'pan': 'pa',
            'fas': 'fa',
            'pol': 'pl',
            'por': 'pt',
            'ron': 'ro',
            'rus': 'ru',
            'gla': 'gd',
            'srp': 'sr',
            'slk': 'sk',
            'slv': 'sl',
            'sot': 'st',
            'som': 'so',
            'spa': 'es',
            'swa': 'sw',
            'swe': 'sv',
            'tgl': 'tl',
            'tgk': 'tg',
            'tam': 'ta',
            'tel': 'te',
            'tha': 'th',
            'tur': 'tr',
            'ukr': 'uk',
            'urd': 'ur',
            'vie': 'vi',
            'cym': 'cy',
            'yor': 'yo',
            'zul': 'zu',

            'other': 'other',
        },

        'file_exts': {
            '.txt': main.tr('Text File (*.txt)'),
            '.htm': main.tr('HTML Page (*.htm; *.html)'),
            '.html': main.tr('HTML Page (*.htm; *.html)')
        },

        'file_types': {
            'export_tables': [
                main.tr('Excel Workbook (*.xlsx)'),
                main.tr('CSV (Comma Delimited) (*.csv)')
            ]
        },

        'file_encodings': {
            main.tr('All Languages (UTF-8 Without BOM)'): 'utf_8',
            main.tr('All Languages (UTF-8 with BOM)'): 'utf_8_sig',
            main.tr('All Languages (UTF-16 with BOM)'): 'utf_16',
            main.tr('All Languages (UTF-16 Big Endian Without BOM)'): 'utf_16_be',
            main.tr('All Languages (UTF-16 Little Endian Without BOM)'): 'utf_16_le',
            main.tr('All Languages (UTF-32 with BOM)'): 'utf_32',
            main.tr('All Languages (UTF-32 Big Endian Without BOM)'): 'utf_32_be',
            main.tr('All Languages (UTF-32 Little Endian Without BOM)'): 'utf_32_le',
            main.tr('All Languages (UTF-7)'): 'utf_7',
            main.tr('All Languages (CP65001)'): 'cp65001',

            main.tr('Baltic Languages (CP775)'): 'cp775',
            main.tr('Baltic Languages (Windows-1257)'): 'cp1257',
            main.tr('Baltic Languages (ISO-8859-4)'): 'iso8859_4',
            main.tr('Baltic Languages (ISO-8859-13)'): 'iso8859_13',

            main.tr('Celtic Languages (ISO-8859-14)'): 'iso8859_14',

            main.tr('Nordic Languages (ISO-8859-10)'): 'iso8859_10',

            main.tr('Europe (HP Roman-8)'): 'hp_roman8',

            main.tr('Central Europe (Mac OS Central European)'): 'mac_centeuro',
            main.tr('Central Europe (Mac OS Latin 2)'): 'mac_latin2',

            main.tr('Central and Eastern Europe (CP852)'): 'cp852',
            main.tr('Central and Eastern Europe (Windows-1250)'): 'cp1250',
            main.tr('Central and Eastern Europe (ISO-8859-2)'): 'iso8859_2',
            main.tr('Central and Eastern Europe (Mac Latin)'): 'mac_latin2',

            main.tr('South-Eastern Europe (ISO-8859-16)'): 'iso8859_16',

            main.tr('Western Europe (EBCDIC 500)'): 'cp500',
            main.tr('Western Europe (CP850)'): 'cp850',
            main.tr('Western Europe (CP858)'): 'cp858',
            main.tr('Western Europe (CP1140)'): 'cp1140',
            main.tr('Western Europe (Windows-1252)'): 'windows_1252',
            main.tr('Western Europe (ISO-2022-JP-2)'): 'iso2022_jp_2',
            main.tr('Western Europe (ISO-8859-1)'): 'iso_8859_1',
            main.tr('Western Europe (ISO-8859-15)'): 'iso_8859_15',
            main.tr('Western Europe (Mac OS Roman)'): 'mac_roman',

            main.tr('Arabic (CP720)'): 'cp720',
            main.tr('Arabic (CP864)'): 'cp864',
            main.tr('Arabic (Windows-1256)'): 'cp1256',
            main.tr('Arabic (ISO-8859-6)'): 'iso_8859_6',
            main.tr('Arabic (Mac OS Arabic)'): 'mac_arabic',

            main.tr('Bulgarian (IBM855)'): 'cp855',
            main.tr('Bulgarian (Windows-1251)'): 'windows_1251',
            main.tr('Bulgarian (ISO-8859-5)'): 'iso_8859_5',
            main.tr('Bulgarian (Mac OS Cyrillic)'): 'mac_cyrillic',

            main.tr('Belarusian (IBM855)'): 'cp855',
            main.tr('Belarusian (Windows-1251)'): 'cp1251',
            main.tr('Belarusian (ISO-8859-5)'): 'iso_8859_5',
            main.tr('Belarusian (Mac OS Cyrillic)'): 'mac_cyrillic',

            main.tr('Canadian French (CP863)'): 'cp863',

            main.tr('Simplified Chinese (GB2312)'): 'gb2312',
            main.tr('Simplified Chinese (HZ)'): 'hz_gb_2312',
            main.tr('Simplified Chinese (ISO-2022-JP-2)'): 'iso2022_jp_2',

            main.tr('Traditional Chinese (Big-5)'): 'big5',
            main.tr('Traditional Chinese (Big5-HKSCS)'): 'big5hkscs',
            main.tr('Traditional Chinese (CP950)'): 'cp950',

            main.tr('Unified Chinese (GBK)'): 'gbk',
            main.tr('Unified Chinese (GB18030)'): 'gb18030',

            main.tr('Croatian (Mac OS Croatian)'): 'mac_croatian',

            main.tr('Danish (CP865)'): 'cp865',

            main.tr('English (ASCII)'): 'ascii',
            main.tr('English (EBCDIC 037)'): 'cp037',
            main.tr('English (CP437)'): 'cp437',

            main.tr('Esperanto (ISO-8859-3)'): 'iso_8859_3',

            main.tr('German (EBCDIC 273)'): 'cp273',

            main.tr('Greek (CP737)'): 'cp737',
            main.tr('Greek (CP869)'): 'cp869',
            main.tr('Greek (CP875)'): 'cp875',
            main.tr('Greek (Windows-1253)'): 'windows_1253',
            main.tr('Greek (ISO-2022-JP-2)'): 'iso2022_jp_2',
            main.tr('Greek (ISO-8859-7)'): 'iso_8859_7',
            main.tr('Greek (Mac OS Greek)'): 'mac_greek',

            main.tr('Hebrew (EBCDIC 424)'): 'cp424',
            main.tr('Hebrew (CP856)'): 'cp856',
            main.tr('Hebrew (CP862)'): 'cp862',
            main.tr('Hebrew (Windows-1255)'): 'windows_1255',
            main.tr('Hebrew (ISO-8859-8)'): 'iso_8859_8',

            main.tr('Icelandic (CP861)'): 'cp861',
            main.tr('Icelandic (Mac OS Icelandic)'): 'mac_iceland',

            main.tr('Japanese (CP932)'): 'cp932',
            main.tr('Japanese (EUC-JP)'): 'euc_jp',
            main.tr('Japanese (EUC-JIS-2004)'): 'euc_jis_2004',
            main.tr('Japanese (EUC-JISx0213)'): 'euc_jisx0213',
            main.tr('Japanese (ISO-2022-JP)'): 'iso_2022_jp',
            main.tr('Japanese (ISO-2022-JP-1)'): 'iso2022_jp_1',
            main.tr('Japanese (ISO-2022-JP-2)'): 'iso2022_jp_2',
            main.tr('Japanese (ISO-2022-JP-2)'): 'iso2022_jp_2004',
            main.tr('Japanese (ISO-2022-JP-3)'): 'iso2022_jp_3',
            main.tr('Japanese (ISO-2022-JP-EXT)'): 'iso2022_jp_ext',
            main.tr('Japanese (Shift_JIS)'): 'shift_jis',
            main.tr('Japanese (Shift_JIS-2004)'): 'shift_jis_2004',
            main.tr('Japanese (Shift_JISx0213)'): 'shift_jisx0213',

            main.tr('Kazakh (KZ-1048)'): 'kz1048',
            main.tr('Kazakh (PTCP154)'): 'ptcp154',

            main.tr('Korean (Windows-949)'): 'cp949',
            main.tr('Korean (EUC-KR)'): 'euc_kr',
            main.tr('Korean (ISO-2022-JP-2)'): 'iso2022_jp_2',
            main.tr('Korean (ISO-2022-KR)'): 'iso_2022_kr',
            main.tr('Korean (JOHAB)'): 'johab',

            main.tr('Macedonian (IBM855)'): 'cp855',
            main.tr('Macedonian (Windows-1251)'): 'cp1251',
            main.tr('Macedonian (ISO-8859-5)'): 'iso_8859_5',
            main.tr('Macedonian (Mac OS Cyrillic)'): 'maccyrillic',

            main.tr('Maltese (ISO-8859-3)'): 'iso_8859_3',

            main.tr('Norwegian (CP865)'): 'cp865',

            main.tr('Persian (Mac OS Farsi)'): 'mac_farsi',

            main.tr('Portuguese (CP860)'): 'cp860',

            main.tr('Romanian (Mac OS Romanian)'): 'mac_romanian',

            main.tr('Russian (IBM855)'): 'ibm855',
            main.tr('Russian (IBM866)'): 'ibm866',
            main.tr('Russian (Windows-1251)'): 'windows_1251',
            main.tr('Russian (ISO-8859-5)'): 'iso_8859_5',
            main.tr('Russian (KOI8-R)'): 'koi8_r',
            main.tr('Russian (Mac OS Cyrillic)'): 'maccyrillic',

            main.tr('Serbian (IBM855)'): 'cp855',
            main.tr('Serbian (Windows-1251)'): 'cp1251',
            main.tr('Serbian (ISO-8859-5)'): 'iso8859_5',
            main.tr('Serbian (Mac OS Cyrillic)'): 'maccyrillic',

            main.tr('Tajik (KOI8-T)'): 'koi8_t',

            main.tr('Thai (CP874)'): 'cp874',
            main.tr('Thai (ISO-8859-11)'): 'iso8859_11',
            main.tr('Thai (TIS-620)'): 'tis_620',

            main.tr('Turkish (CP857)'): 'cp857',
            main.tr('Turkish (EBCDIC 1026)'): 'cp1026',
            main.tr('Turkish (Windows-1254)'): 'cp1254',
            main.tr('Turkish (ISO-8859-9)'): 'iso_8859_9',
            main.tr('Turkish (Mac OS Turkish)'): 'mac_turkish',

            main.tr('Ukrainian (CP1125)'): 'cp1125',
            main.tr('Ukrainian (KOI8-U)'): 'koi8_u',

            main.tr('Urdu (CP1006)'): 'cp1006',
            main.tr('Urdu (Mac OS Farsi)'): 'mac_farsi',

            main.tr('Vietnamese (CP1258)'): 'cp1258'
        },

        'sentence_tokenizers': {
            'zho_CN': [
                main.tr('Wordless - Chinese Sentence Tokenizer'),
                main.tr('HanLP - Sentence Segmenter'),
            ],
            'zho_TW': [
                main.tr('Wordless - Chinese Sentence Tokenizer'),
                main.tr('HanLP - Sentence Segmenter'),
            ],
            'ces': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'dan': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'nld': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'eng': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'est': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'fin': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'fra': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'deu': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'ell': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'ita': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'nor': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'pol': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'por': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'slv': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'spa': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'swe': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],
            'tur': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],

            'other': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ]
        },

        'word_tokenizers': {
            'zho_CN': [
                main.tr('jieba - With HMM'),
                main.tr('jieba - Without HMM'),
                main.tr('HanLP - Standard Tokenizer'),
                main.tr('HanLP - Basic Tokenizer'),
                main.tr('HanLP - High-speed Tokenizer'),
                main.tr('HanLP - URL Tokenizer'),
                main.tr('HanLP - CRF Lexical Analyzer'),
                main.tr('HanLP - Perceptron Lexical Analyzer'),
                main.tr('HanLP - Dijkstra Segmenter'),
                main.tr('HanLP - N-shortest Path Segmenter'),
                main.tr('HanLP - Viterbi Segmenter'),
                main.tr('Wordless - Single Character Splitter')
            ],
            'zho_TW': [
                main.tr('jieba - With HMM'),
                main.tr('jieba - Without HMM'),
                main.tr('HanLP - Standard Tokenizer'),
                main.tr('HanLP - Basic Tokenizer'),
                main.tr('HanLP - High-speed Tokenizer'),
                main.tr('HanLP - Traditional Chinese Tokenizer'),
                main.tr('HanLP - URL Tokenizer'),
                main.tr('HanLP - CRF Lexical Analyzer'),
                main.tr('HanLP - Perceptron Lexical Analyzer'),
                main.tr('HanLP - Dijkstra Segmenter'),
                main.tr('HanLP - N-shortest Path Segmenter'),
                main.tr('HanLP - Viterbi Segmenter'),
                main.tr('Wordless - Single Character Splitter')
            ],
            'ces': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'dan': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'nld': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'eng': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'est': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'fin': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'fra': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'deu': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'ell': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'ita': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'nor': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'pol': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'por': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'slv': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'spa': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'swe': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],
            'tur': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ],

            'other': [
                main.tr('NLTK - Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NIST Tokenizer (International Mode)'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Word Punctuation Tokenizer'),
                main.tr('PyDelphin - Repp Tokenizer'),
            ]
        },

        'word_detokenizers': {
            'zho_CN': [
                main.tr('Wordless - Chinese Word Detokenizer')
            ],

            'zho_TW': [
                main.tr('Wordless - Chinese Word Detokenizer')
            ],

            'eng': [
                main.tr('NLTK - Moses Detokenizer')
            ],

            'other': [
                main.tr('NLTK - Moses Detokenizer')
            ]
        },

        'pos_taggers': {
            'zho_CN': {
                main.tr('jieba'): 'jieba',
                main.tr('HanLP - CRF Lexical Analyzer'): 'HanLP',
                main.tr('HanLP - Perceptron Lexical Analyzer'): 'HanLP'
            },
            'zho_TW': {
                main.tr('jieba'): 'jieba',
                main.tr('HanLP - CRF Lexical Analyzer'): 'HanLP',
                main.tr('HanLP - Perceptron Lexical Analyzer'): 'HanLP'
            },
            'eng': {
                main.tr('NLTK - Perceptron POS Tagger'): 'Penn Treebank'
            },
            'rus': {
                main.tr('NLTK - Perceptron POS Tagger'): 'Russian National Corpus'
            }
        },

        'tagsets': {
            # Chinese
            'jieba': 'zho_jieba',
            'HanLP': 'zho_hanlp',
            # English
            'Penn Treebank': 'en-ptb',
            # Russian
            'Russian National Corpus': 'rus_russian_national_corpus'
        },

        'lemmatizers': {
            'ast': [
                'Lemmatization Lists'
            ],
            'bul': [
                'Lemmatization Lists'
            ],
            'cat': [
                'Lemmatization Lists'
            ],
            'ces': [
                'Lemmatization Lists'
            ],
            'eng': [
                'NLTK',
                'e_lemma.txt',
                'Lemmatization Lists'
            ],
            'est': [
                'Lemmatization Lists'
            ],
            'fra': [
                'Lemmatization Lists'
            ],
            'glg': [
                'Lemmatization Lists'
            ],
            'deu': [
                'Lemmatization Lists'
            ],
            'hun': [
                'Lemmatization Lists'
            ],
            'gle': [
                'Lemmatization Lists'
            ],
            'ita': [
                'Lemmatization Lists'
            ],
            'glv': [
                'Lemmatization Lists'
            ],
            'fas': [
                'Lemmatization Lists'
            ],
            'por': [
                'Lemmatization Lists'
            ],
            'ron': [
                'Lemmatization Lists'
            ],
            'gla': [
                'Lemmatization Lists'
            ],
            'slk': [
                'Lemmatization Lists'
            ],
            'slv': [
                'Lemmatization Lists'
            ],
            'spa': [
                'Lemmatization Lists'
            ],
            'swe': [
                'Lemmatization Lists'
            ],
            'ukr': [
                'Lemmatization Lists'
            ],
            'cym': [
                'Lemmatization Lists'
            ]
        },

        'stop_words': {
            'afr': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ara': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'hye': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'aze': [
                'NLTK'
            ],
            'eus': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ben': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'bre': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'bul': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'cat': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'zho_CN': [
                'HanLP',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'zho_TW': [
                'HanLP',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'hrv': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ces': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'dan': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'nld': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'eng': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'epo': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'est': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'fin': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'fra': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'glg': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'deu': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ell': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'hau': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'heb': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'hin': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'hun': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ind': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'gle': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ita': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'jpn': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'kaz': [
                'NLTK'
            ],
            'kor': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'kur': [
                'Stopwords ISO'
            ],
            'lat': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'lav': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'mar': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'msa': [
                'Stopwords ISO'
            ],
            'nep': [
                'NLTK'
            ],
            'nor': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'fas': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'pol': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'por': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ron': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'rus': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'slk': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'slv': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'sot': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'som': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'spa': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'swa': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'swe': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'tgl': [
                'Stopwords ISO'
            ],
            'tha': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'tur': [
                'NLTK',
                'Stopwords ISO',
                'stopwords-json'
            ],
            'ukr': [
                'Stopwords ISO'
            ],
            'urd': [
                'Stopwords ISO'
            ],
            'vie': [
                'Stopwords ISO'
            ],
            'yor': [
                'Stopwords ISO',
                'stopwords-json'
            ],
            'zul': [
                'Stopwords ISO',
                'stopwords-json'
            ]
        },

        'measures_dispersion': {
            main.tr('Juilland\'s D'): {
                'col': main.tr('Juilland\'s D'),
                'func': measures_dispersion.juillands_d
            },

            main.tr('Carroll\'s D₂'): {
                'col': main.tr('Carroll\'s D₂'),
                'func': measures_dispersion.carrolls_d2
            },

            main.tr('Lyne\'s D₃'): {
                'col': main.tr('Lyne\'s D₃'),
                'func': measures_dispersion.lynes_d3
            },

            main.tr('Rosengren\'s S'): {
                'col': main.tr('Rosengren\'s S'),
                'func': measures_dispersion.rosengrens_s
            },

            main.tr('Distributional Consistency'): {
                'col': main.tr('Distributional Consistency'),
                'func': measures_dispersion.distributional_consistency
            }
        },

        'measures_adjusted_freq': {
            main.tr('Juilland\'s U'): {
                'col': main.tr('Juilland\'s U'),
                'func': measures_adjusted_freq.juillands_u
            },

            main.tr('Carroll\'s Uₘ'): {
                'col': main.tr('Carroll\'s Uₘ'),
                'func': measures_adjusted_freq.carrolls_um
            },

            main.tr('Rosengren\'s KF'): {
                'col': main.tr('Rosengren\'s KF'),
                'func': measures_adjusted_freq.rosengrens_kf
            },

            main.tr('Engvall\'s Measure'): {
                'col': main.tr('Engvall\'s Measure'),
                'func': measures_adjusted_freq.engvalls_measure
            },

            main.tr('Kromer\'s Uᵣ'): {
                'col': main.tr('Kromer\'s Uᵣ'),
                'func': measures_adjusted_freq.kromers_ur
            }
        },

        'tests_significance': {
            'collocation': {
                main.tr('z-score'): {
                    'cols': [
                        main.tr('z-score'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.z_score
                },

                main.tr('Student\'s t-test (One-sample)'): {
                    'cols': [
                        main.tr('t-statistic'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.students_t_test_one_sample
                },

                main.tr('Pearson\'s Chi-squared Test'): {
                    'cols': [
                        main.tr('χ2'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.pearsons_chi_squared_test
                },

                main.tr('Log-likelihood Ratio Test'): {
                    'cols': [
                        main.tr('Log-likelihood Ratio'),
                        main.tr('p-value'),
                        main.tr('Bayes Factor')
                    ],

                    'func': measures_statistical_significance.log_likehood_ratio_test
                },

                main.tr('Fisher\'s Exact Test'): {
                    'cols': [
                        None,
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.fishers_exact_test
                }
            },

            'keywords': {
                main.tr('Student\'s t-test (Two-sample)'): {
                    'cols': [
                        main.tr('t-statistic'),
                        main.tr('p-value'),
                        main.tr('Bayes Factor')
                    ],

                    'func': measures_statistical_significance.students_t_test_two_sample
                },

                main.tr('Pearson\'s Chi-squared Test'): {
                    'cols': [
                        main.tr('χ2'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.pearsons_chi_squared_test
                },


                main.tr('Fisher\'s Exact Test'): {
                    'cols': [
                        None,
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.fishers_exact_test
                },

                main.tr('Log-likelihood Ratio Test'): {
                    'cols': [
                        main.tr('Log-likelihood Ratio'),
                        main.tr('p-value'),
                        main.tr('Bayes Factor')
                    ],

                    'func': measures_statistical_significance.log_likehood_ratio_test
                },

                main.tr('Mann-Whitney U Test'): {
                    'cols': [
                        main.tr('U Statistic'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': measures_statistical_significance.mann_whitney_u_test
                }
            }
        },

        'measures_effect_size': {
            'collocation': {
                main.tr('Pointwise Mutual Information'): {
                    'col': main.tr('PMI'),
                    'func': measures_effect_size.pmi
                },

                main.tr('Mutual Dependency'): {
                    'col': main.tr('MD'),
                    'func': measures_effect_size.mutual_dependency
                },

                main.tr('Log-Frequency Biased MD'): {
                    'col': main.tr('LFMD'),
                    'func': measures_effect_size.log_freq_biased_md
                },

                main.tr('Cubic Association Ratio'): {
                    'col': main.tr('Cubic Association Ratio'),
                    'func': measures_effect_size.cubic_association_ratio
                },

                main.tr('MI.log-f'): {
                    'col': main.tr('MI.log-f'),
                    'func': measures_effect_size.mi_lof_f
                },

                main.tr('Mutual Information'): {
                    'col': main.tr('MI'),
                    'func': measures_effect_size.mi
                },

                main.tr('Squared Phi Coefficient'): {
                    'col': main.tr('φ2'),
                    'func': measures_effect_size.squared_phi_coeff
                },

                main.tr('Dice\'s Coefficient'): {
                    'col': main.tr('Dice\'s Coefficient'),
                    'func': measures_effect_size.dices_coeff
                },

                main.tr('logDice'): {
                    'col': main.tr('logDice'),
                    'func': measures_effect_size.log_dice
                },

                main.tr('Mutual Expectation'): {
                    'col': main.tr('Mutual Expectation'),
                    'func': measures_effect_size.mutual_expectation
                },

                main.tr('Jaccard Index'): {
                    'col': main.tr('Jaccard Index'),
                    'func': measures_effect_size.jaccard_index
                },

                main.tr('Minimum Sensitivity'): {
                    'col': main.tr('Minimum Sensitivity'),
                    'func': measures_effect_size.min_sensitivity
                }
            },

            'keywords': {
                main.tr('Kilgarriff\'s Ratio'): {
                    'col': main.tr('Kilgarriff\'s Ratio'),
                    'func': measures_effect_size.kilgarriffs_ratio
                },

                main.tr('Odds Ratio'): {
                    'col': main.tr('Odds Ratio'),
                    'func': measures_effect_size.odds_ratio
                },

                main.tr('Log Ratio'): {
                    'col': main.tr('Log Ratio'),
                    'func': measures_effect_size.log_ratio
                },

                main.tr('Difference Coefficient'): {
                    'col': main.tr('Difference Coefficient'),
                    'func': measures_effect_size.diff_coeff
                },

                main.tr('%DIFF'): {
                    'col': main.tr('%DIFF'),
                    'func': measures_effect_size.pct_diff
                }
            }
        },

        'assoc_measures': {
            main.tr('Frequency'): nltk.collocations.BigramAssocMeasures().raw_freq,
            main.tr('Student\'s T-test'): nltk.collocations.BigramAssocMeasures().student_t,
            main.tr('Pearson\'s Chi-squared Test'): nltk.collocations.BigramAssocMeasures().chi_sq,
            main.tr('Phi Coefficient'): nltk.collocations.BigramAssocMeasures().phi_sq,
            main.tr('Pointwise Mutual Information'): nltk.collocations.BigramAssocMeasures().pmi,
            main.tr('Likelihood Ratio'): nltk.collocations.BigramAssocMeasures().likelihood_ratio,
            main.tr('Poisson-Stirling'): nltk.collocations.BigramAssocMeasures().poisson_stirling,
            main.tr('Jaccard Index'): nltk.collocations.BigramAssocMeasures().jaccard,
            main.tr('Fisher\'s Exact Test'): nltk.collocations.BigramAssocMeasures().fisher,
            main.tr('Dice\'s Coefficient'): nltk.collocations.BigramAssocMeasures().dice
        },

        'style_dialog': '''
            <head>
                <style>
                    * {
                        margin: 0;
                        border: 0;
                        padding: 0;

                        line-height: 1.2;
                        text-align: justify;
                    }

                    h1 {
                        margin-bottom: 10px;
                        font-size: 16px;
                        font-weight: bold;
                    }

                    p {
                        margin-bottom: 5px;
                    }
                </style>
            </head>
        ''',

        'styles': {
            'style_hints': '''
                <head>
                    <style>
                        * {
                            margin: 0;
                            border: 0;
                            padding: 0;

                            line-height: 1.2;
                            text-align: justify;

                            color: #777;
                        }
                    </style>
                </head>
            '''
        }
    }
