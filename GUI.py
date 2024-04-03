from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Meed\Desktop\Projects\11\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("818x444")
window.configure(bg = "#1A1A1A")


canvas = Canvas(
    window,
    bg = "#1A1A1A",
    height = 444,
    width = 818,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    136.0,
    285.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    409.0,
    32.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    215.0,
    32.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    36.0,
    33.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    538.0,
    101.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    380.0,
    285.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    356.0,
    203.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    366.0,
    129.0,
    image=image_image_8
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    547.5,
    238.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#242121",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=330.0,
    y=215.0,
    width=435.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    547.5,
    164.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#242121",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=330.0,
    y=141.0,
    width=435.0,
    height=44.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    547.5,
    320.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#242121",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=330.0,
    y=297.0,
    width=435.0,
    height=44.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=359.0,
    y=367.0,
    width=181.0,
    height=52.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    781.0,
    32.99998916542455,
    image=image_image_9
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=560.0,
    y=367.0,
    width=178.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()
