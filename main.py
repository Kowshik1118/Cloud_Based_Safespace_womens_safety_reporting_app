import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import json,datetime
BG="#0B1220";CARD="#15223A";TEXT="#F5F8FF";MUTED="#B3C0D6";TEAL="#45D9B9";BLUE="#597FE0";DATA=Path("safespace_reports.json")
def load():
 try:return json.loads(DATA.read_text())
 except:return []
def save(x):DATA.write_text(json.dumps(x,indent=2))
class App(tk.Tk):
 def __init__(self):
  super().__init__();self.title("SafeSpace — Local Safety Report Demo");self.geometry("1040x700");self.minsize(850,570);self.configure(bg=BG);self.reports=load();self.build()
 def L(self,p,t,size=11,c=TEXT,b=False,**k):return tk.Label(p,text=t,bg=p["bg"],fg=c,font=("Segoe UI",size,"bold" if b else "normal"),**k)
 def card(self,p):return tk.Frame(p,bg=CARD,highlightthickness=1,highlightbackground="#2A3C60")
 def build(self):
  h=tk.Frame(self,bg=BG);h.pack(fill="x",padx=34,pady=(23,10));self.L(h,"SAFESPACE",12,TEAL,True).pack(anchor="w");self.L(h,"Private incident-report practice dashboard",25,TEXT,True).pack(anchor="w");self.L(h,"Standalone local demo • no login • no registration • no API • no server • no cloud",10,MUTED).pack(anchor="w",pady=(2,0))
  alert=self.card(self);alert.pack(fill="x",padx=34,pady=(0,12));self.L(alert,"Urgent help: If there is immediate danger in India, call 112. This demo cannot call, alert, locate, or notify anyone.",11,"#FFB7C1",True,wraplength=900).pack(anchor="w",padx=18,pady=12)
  main=tk.Frame(self,bg=BG);main.pack(fill="both",expand=True,padx=34,pady=(0,27));main.columnconfigure(0,weight=3);main.columnconfigure(1,weight=2);main.rowconfigure(0,weight=1);a=self.card(main);a.grid(row=0,column=0,sticky="nsew",padx=(0,8));b=self.card(main);b.grid(row=0,column=1,sticky="nsew",padx=(8,0))
  self.L(a,"NEW PRIVATE REPORT",11,MUTED,True).pack(anchor="w",padx=18,pady=(16,8));self.kind=tk.StringVar(value="Harassment / unsafe situation");tk.OptionMenu(a,self.kind,"Harassment / unsafe situation","Stalking concern","Unsafe transport","Online harassment","Other").pack(anchor="w",padx=18);self.place=tk.Entry(a,bg="#0C182B",fg=TEXT,insertbackground=TEXT,relief="flat",font=("Segoe UI",11));self.place.insert(0,"Location or area (optional)");self.place.pack(fill="x",padx=18,pady=10,ipady=8);self.detail=tk.Text(a,bg="#0C182B",fg=TEXT,insertbackground=TEXT,relief="flat",wrap="word",font=("Segoe UI",11),padx=10,pady=10);self.detail.pack(fill="both",expand=True,padx=18);self.detail.insert("1.0","Describe what happened. Avoid adding information you do not want stored on this computer.");tk.Button(a,text="Save private report locally",command=self.add,bg=TEAL,fg="#06151A",relief="flat",font=("Segoe UI",11,"bold"),pady=10).pack(fill="x",padx=18,pady=15)
  self.L(b,"SAVED ON THIS DEVICE",11,MUTED,True).pack(anchor="w",padx=18,pady=(16,8));self.list=tk.Listbox(b,bg="#0C182B",fg=TEXT,relief="flat",font=("Segoe UI",10));self.list.pack(fill="both",expand=True,padx=18);self.L(b,"Reports remain in safespace_reports.json on this computer. Delete that file to remove saved demo reports.",10,MUTED,wraplength=290,justify="left").pack(anchor="w",padx=18,pady=12);tk.Button(b,text="Clear saved reports",command=self.clear,bg=BLUE,fg="white",relief="flat",font=("Segoe UI",10,"bold"),pady=8).pack(fill="x",padx=18,pady=(0,16));self.refresh()
 def refresh(self):
  self.list.delete(0,"end")
  for r in reversed(self.reports):self.list.insert("end",f"{r['time']} — {r['type']}")
 def add(self):
  x=self.detail.get("1.0","end-1c").strip()
  if len(x)<10:return messagebox.showerror("More detail needed","Write at least 10 characters.")
  self.reports.append({"type":self.kind.get(),"place":self.place.get(),"detail":x,"time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M")});save(self.reports);self.detail.delete("1.0","end");messagebox.showinfo("Saved locally","The report was saved only on this computer. It was not sent anywhere.");self.refresh()
 def clear(self):
  if messagebox.askyesno("Clear reports","Delete all locally saved reports?"):self.reports=[];save(self.reports);self.refresh()
if __name__=="__main__":App().mainloop()
