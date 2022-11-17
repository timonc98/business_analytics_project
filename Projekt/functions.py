
# Information List
athletes = []

# Add Information
def add():
	global athletes
	athletes.append([Name.get(),Number.get(),address.get(1.0, "end-1c")])
	update_book()

# View Information
def view():
	Name.set(athletes[int(select.curselection()[0])][0])
	Number.set(athletes[int(select.curselection()[0])][1])
	address.delete(1.0,"end")
	address.insert(1.0, datas[int(select.curselection()[0])][2])

# Delete Information
def delete():
	del athletes[int(select.curselection()[0])]
	update_book()

def reset():
	Name.set('')
	Number.set('')
	address.delete(1.0,"end")

# Update Information
def update_book():
	select.delete(0,END)
	
	for n,p,a in athletes:
		select.insert(END, n)
