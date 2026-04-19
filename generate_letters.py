from gtts import gTTS
import os

# Nom des fichiers -> texte arabe à prononcer
LETTERS = {
    'alif':  'أَلِف',
    'ba':    'بَاء',
    'ta':    'تَاء',
    'tha':   'ثَاء',
    'jim':   'جِيم',
    'ha':    'حَاء',
    'kha':   'خَاء',
    'dal':   'دَال',
    'dhal':  'ذَال',
    'ra':    'رَاء',
    'zay':   'زَاي',
    'sin':   'سِين',
    'shin':  'شِين',
    'sad':   'صَاد',
    'dad':   'ضَاد',
    'tta':   'طَاء',
    'dha':   'ظَاء',
    'ain':   'عَيْن',
    'ghain': 'غَيْن',
    'fa':    'فَاء',
    'qaf':   'قَاف',
    'kaf':   'كَاف',
    'lam':   'لَام',
    'mim':   'مِيم',
    'nun':   'نُون',
    'ha2':   'هَاء',
    'waw':   'وَاو',
    'ya':    'يَاء',
    'hamza': 'هَمْزَة',
}

os.makedirs('audio/letters', exist_ok=True)

for filename, text in LETTERS.items():
    path = f'audio/letters/{filename}.mp3'
    print(f'Generating {path} ({text})...')
    tts = gTTS(text=text, lang='ar', slow=True)
    tts.save(path)

print('\nDone! 29 MP3 files generated in audio/letters/')
