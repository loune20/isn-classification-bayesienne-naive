#IMPORTING
import tkinter

#VARIABLE
bla1 = "Morbi quis sem sed eros molestie vulputate a at ligula. Aliquam ut felis lorem. Phasellus consectetur non orci ac consectetur. Fusce convallis nisi felis, nec porttitor justo condimentum ut. Nulla feugiat ex nunc, sit amet vehicula libero finibus id. Nunc porttitor lacus hendrerit pretium molestie. Praesent a condimentum lacus. TESTTESTSTETTETSDTS"
bla2 = "In iaculis tortor nec nibh suscipit, quis tempor nibh gravida. Phasellus vel lobortis nibh. Suspendisse quis lorem eu nisl faucibus dignissim quis a metus. Vestibulum placerat justo urna. Duis sed laoreet justo. Donec eu lectus ultrices, cursus justo nec, auctor elit. Proin in urna sit amet libero mattis efficitur id at orci. Sed quis rutrum mauris, et cursus orci. Vestibulum nec augue sit amet nisl rhoncus ultricies. Praesent rhoncus varius felis, quis consequat orci efficitur eget. Curabitur ut magna aliquam, lacinia nunc sed, rutrum ipsum. Mauris ut sollicitudin lacus, sed iaculis sem."
bla3 = "Nulla fermentum eros sed ipsum tempor, et consectetur purus dapibus. Vivamus vestibulum semper sodales. Phasellus fermentum lectus non lorem fringilla fringilla. Suspendisse pulvinar viverra lacus, vel viverra neque finibus id. Vivamus et elit sed neque pretium cursus non at orci. Nunc tortor odio, tempor porta placerat non, venenatis et nisl. Donec sodales commodo sapien sit amet congue. Pellentesque laoreet tempor mauris, vitae sodales risus interdum at. In rutrum nunc vitae condimentum sodales. Suspendisse consequat pretium leo, sit amet dapibus ante sagittis at. In dui enim, dignissim sit amet pharetra at, vestibulum vitae metus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas porta neque ultricies odio faucibus, non lobortis metus gravida. Mauris ac lacus mollis, accumsan dui at, pulvinar eros. Nam tellus mauris, gravida a bibendum quis, accumsan eget sapien."
popup_content = [bla1, bla2, bla3]

#FUNCTIONS
def populate(frame, text_to_display, row):
    tkinter.Label(frame, text=text_to_display, borderwidth="4", relief="raised", wraplength=500).grid(row=row, column=0)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def createPopupThing():
    global root, canvas, frame, vsb, rmbr_button
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, borderwidth=0, background="#2EF2A2", width=1200, height=800)
    frame = tkinter.Frame(canvas, background="#2EF2A2")
    vsb = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((5,5), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    root.wm_title("Machine learning project : sentinent analysis using Bayes' therorem")

    rmbr_button = tkinter.Button(frame, text="Fermer et se souvenir...", command =(root.destroy))
    rmbr_button.grid(row=11, column=0)
    
#MAIN LOOP
createPopupThing()
onFrameConfigure(canvas)
for x in range(len(popup_content)):
    populate(frame, popup_content[x], x)
root.mainloop()
