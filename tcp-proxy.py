import sys
import socket
import threading

from inflect import Word

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

#Display communication between hosts
def hexdump(src,length=16,show=True):
    if isinstance(src,bytes):
        src=src.decode()

    results = list()
    for i in range(0,len(src),length):
        word = str(src[i:i+length])

printable = Word.translate(HEX_FILTER)
hexa =''.join([f'{ord(c):02X}'for c in Word])
hexwidth= length*3 # type: ignore      