"""Text to morse code sound converter
MIT License

Copyright (c) 2024 Roman Babenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import array
import math
import re
import time

import simpleaudio as sa


class Txt2Mrs:
    MORSE = {
        # 1
        "-": "Tt",
        ".": "Ee",
        # 2
        "..": "Ii",
        ".-": "Aa",
        "-.": "Nn",
        "--": "Mm",
        # 3
        "...": "Ss",
        "..-": "Uu",
        ".-.": "Rr",
        ".--": "Ww",
        "-..": "Dd",
        "-.-": "Kk",
        "--.": "Gg",
        "---": "Oo",
        # 4
        "....": "Hh",
        "...-": "Vv",
        "..-.": "Ff",
        "..--": "Ü",
        ".-..": "Ll",
        ".-.-": "Ä",
        ".--.": "Pp",
        ".---": "Jj",
        "-...": "Bb",
        "-..-": "Xx",
        "-.-.": "Cc",
        "-.--": "Yy",
        "--..": "Zz",
        "--.-": "Qq",
        "---.": "Ö",
        "----": "ĤĥŠ",
        # 5
        ".....": "5",
        "....-": "4",
        "...-.": "",
        "...--": "3",
        "..-..": "",
        "..-.-": "",
        "..--.": "",
        "..---": "2",
        ".-...": "&",
        ".-..-": "",
        ".-.-.": "+",
        ".-.--": "",
        ".--..": "",
        ".--.-": "",
        ".---.": "",
        ".----": "1",
        "-....": "6",
        "-...-": "=",
        "-..-.": "/",
        "-..--": "",
        "-.-..": "",
        "-.-.-": "",
        "-.--.": "(",
        "-.---": "",
        "--...": "7",
        "--..-": "",
        "--.-.": "",
        "--.--": "",
        "---..": "8",
        "---.-": "",
        "----.": "9",
        "-----": "0",
        # 6
        ".-.-.-": ".",
        "--..--": ",",
        "..--..": "?",
        "-.-.--": "!",
        "-.--.-": ")",
        ".----.": "'",
        "---...": ":",
        "-.-.-.": ";",
        "-....-": "-",
        "..--.-": "_",
        ".--.-.": "@",
        ".-..-.": '"',
    }
    WHITESPACE_PATTERN = re.compile(r"\s")

    def __init__(self, speed: int, frequency: int, sample_rate=44100, amplitude=32767):
        self.signal = None
        self.sample_rate = sample_rate
        self.dot_duration = speed / 1000
        self.space_duration = 7 * speed / 1000
        self.dash_duration = speed / 333
        self.dot_wave = array.array(
            'h',
            (int(amplitude * math.sin(2 * math.pi * frequency * t / sample_rate)) for t in
             range(int(sample_rate * self.dot_duration)))
        )
        self.dot_silence = array.array('h', (0 for _ in range(int(sample_rate * self.dot_duration))))
        self.dash_wave = array.array(
            'h',
            (int(amplitude * math.sin(2 * math.pi * frequency * t / sample_rate)) for t in
             range(int(sample_rate * self.dash_duration)))
        )

        self.code = {}
        for x, y in self.MORSE.items():
            for i in y:
                assert i not in self.code, (x, y)
                self.code[i] = x

    def morse(self, char_ord: int):
        """Play morse cones

        Args:
            char_ord: one char to produce a sound
        """
        sign = chr(char_ord)
        combined_wave = array.array('h', [])

        if self.WHITESPACE_PATTERN.match(sign):
            print('   ',end='',flush=True)
            if self.signal:
                time.sleep(self.space_duration)
            self.signal = False
        elif code := self.code.get(sign):
            print(code, end=' ',flush=True)  # dbg
            for i in code:
                if combined_wave:
                    combined_wave += self.dot_silence
                if '.' == i:
                    combined_wave += self.dot_wave
                elif '-' == i:
                    combined_wave += self.dash_wave
            if self.signal:
                time.sleep(self.dash_duration)
            self.signal = True
            # Play the combined waveform
            sa.play_buffer(combined_wave, num_channels=1, bytes_per_sample=2, sample_rate=self.sample_rate).wait_done()
        else:
            print('\t',end=' ',flush=True)  # dbg
            time.sleep(self.space_duration)
            self.signal = False
        # combined_wave += self.dash_silence
