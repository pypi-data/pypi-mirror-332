"""Text to morse code sound converter
MIT License

Copyright (c) 2025 Roman Babenko

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
import contextlib
import datetime
import sys
from typing import Optional

from txt2mrs import Txt2Mrs


def get_int(val) -> Optional[int]:
    with contextlib.suppress(Exception):
        return int(val)
    return None


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main() -> int:
    """main function

    Args:
        argv[1]: speed
        argv[2]: tone
    Return:
        EXIT_SUCCESS if no exception was thrown
    """
    error = 1

    speed = get_int(sys.argv[1] if 2 < len(sys.argv) else None) or 100
    tone = get_int(sys.argv[2] if 3 < len(sys.argv) else None) or 500

    txt2mrs = Txt2Mrs(speed, tone)

    if get_int(sys.argv[-1]) and 4 > len(sys.argv):
        try:
            for line in sys.stdin:
                print(f'Input : {line}')
        except KeyboardInterrupt as sigint:
            error = 0
    else:
        message = sys.argv[-1]
        print(f'message : {message}')
        for i in message:
            old = datetime.datetime.now()
            txt2mrs.morse(ord(i))
            print((datetime.datetime.now() - old).total_seconds())
        error = 0

    if 0 != error:
        print("txt2mrs <speed> <tone> [message]")
    return error


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if __name__ == "__main__":
    sys.exit(main())
