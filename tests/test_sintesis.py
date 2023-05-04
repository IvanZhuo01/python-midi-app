from globals import NOTAS
from out.player import Player
from models.utils import Chunker
from models.sintesis import KarplusStrong, Synthesizer
from models.NoteFactory import Note

def static(p):
    chunker = Chunker()
    m = KarplusStrong()

    notes = [ m.transform(Note(frequency=NOTAS["C"], duration=3, note=2)),
             m.transform(Note(frequency=NOTAS["B"], duration=1, note=2))
             ]

    for n in notes:
        for c in chunker.chunkerize(n):
            p.play(c)


def continuos(p):
    i = 0

    while True:
        p.play(m.next())
        i += 1

        if i == 10000:
            print("NOte off")
            m.note_off()
            break

    p.play(m.next())


if __name__ == '__main__':
    m = Synthesizer(NOTAS["C"], 100)

    p = Player()
    p.start()

    static(p)
    p.close()
