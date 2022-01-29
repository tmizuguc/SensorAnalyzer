import os
import pandas as pd

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext


def analyze(sensor):
    info = sensor.describe()
    return info


def main(log):
    file = filedialog.askopenfile(initialdir='~/')
    if file:
        try:
            sensor = pd.read_csv(file.name)
            outfile = os.path.splitext(file.name)[0] + "_analyzed.csv"
        except Exception as e:
            print(e)
            log.insert("end", "ファイルが開けません\n")
            return

        try:
            info = analyze(sensor)
            log.insert("end", f"解析完了\n解析ファイル：{outfile}\n")
            info.to_csv(outfile)
        except Exception as e:
            print(e)
            log.insert("end", "ファイルの中身が不正です。センサーファイルを指定してください。\n")

        file.close()


if __name__ == "__main__":
    root = Tk()
    root.title('Sensor Analyzer')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    frame = ttk.Frame(root, padding=10)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.grid(sticky=N + W + S + E)

    # Log
    log = scrolledtext.ScrolledText(frame, height=10)
    log.grid(row=1, column=0, sticky=W)

    # Analyze
    b = ttk.Button(
        frame, text='Analyze Sensor File', width=15,
        command=lambda: main(log))
    b.grid(row=0, column=0, sticky='')

    root.mainloop()
