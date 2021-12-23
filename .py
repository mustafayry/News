from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Pomodro")

bell = True


def clockize(m, s):
    mstr = str(m)
    sstr = str(s)
    if s < 10:
        mstr = "0" + mstr
    if s <10:
        sstr = "0" + sstr
    return mstr + ":" + sstr   
    
    
def start_25():
    global conting
    global bell
    
    start["state"] = "disabled"
    
    if bell:
        window.bell()
        bell = False
        
    status.config(text="Çalışma zamanı")
    curr = countdown["text"]
    m, s = curr.split(":")
    mint, sint = int(m), int(s)
    if sint > 0:
        sint -= 1
        countdown.config(text=clockize(mint, sint))
    if sint == 0:
        if mint > 0:
            sint = 59
            mint -= 1
            countdown.config(text=clockize(mint, sint))
        else:
            countdown.config(text=clocize(5,0))
            bell = True
            start_10()
            return
    conting = window.after(1000, start_25)
    
    
    
    
    
    
    if bell:
        window.bell()
        bell = False
    status.config(text_"Mola zamanı")
    curr = countdown["text"]
    m, s = curr.split(":")
    mint, sint = int(m), int(s)
    if sint > 0:
        sint -= 1
        countdown.config(text=clockize(mint, sint))
    if sint == 0:
        if mint > 0:
            sint = 59
            mint -= 1
            countdown.config(text=clockize(mint, sint))
        else:
            countdown.config(text=clockize(25,0))
            bell = True
            start_25()
            return
    conting = window.after(1000, start_10)    
    
    
    def wait():
        start["state"] = "active"
        try:
            window.after_cancel(conting)
            status.config(text="Durduruldu")
        except NameError :
            return
        
        
    def reset():
        wait()
        countdown.config(text="25:00")
        status.config(text="Başlatılmadı")
        
  
  status = Label(window, text="Başlamadı", font=("Arial", 15))
  status.pack(pady=10)
  
  countdown = Label(window, text="25:00", font=("Arial", 40))
  countdown.pack(pady=10)
  
  start = Button(window, text="Başla", font=("Arial", 15), command=start_25)
  start.pack(pady=25)
  
  pause = Button(window, text="Dur", font=("Arial", 15), command=wait)
  pause.pack(pady=25)
  
  reset = Button(window, text="Sıfırla", font=("Arial",15), command=reset)
  reset.pack(pady=25)
  
  window.mainloop()
