# from mss.linux import MSS as mss
from mss import mss


with mss() as sct:
    sct.shot()

# with mss(display=":0.0") as sct:
#     for filename in sct.save():
#         print(filename)