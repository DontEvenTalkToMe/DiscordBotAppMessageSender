import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("Message Input")
root.geometry("400x400")

name_var = tk.StringVar()
not_var = tk.IntVar()

channel_var = tk.StringVar()
bot_token_var = tk.StringVar()

def submit():
    name = name_var.get()
    net = not_var.get()
    channel_id = channel_var.get()
    bot_token = bot_token_var.get()

    if net == 0:
        net = 1
    if channel_id == "":
        channel_id = "DEFAULTCHANNELID" #set default channel id
    if  bot_token == "":
        bot_token = "DEFAULTBOTTOKEN" #set default bot token

    print("The message is: " + name)
    print("The amount is: " + str(net))
    print("The channel ID is: " + channel_id)
    print("The bot token is: " + bot_token)

    name_var.set("")

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json"
    }
    data = {
        "content": name,
    }

    for _ in range(net):
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.status_code, response.text)

name_label = tk.Label(root, text='Message', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 14, 'normal'))

not_label = tk.Label(root, text='Amount (0 is 1)', font=('calibre', 10, 'bold'))
not_entry = tk.Entry(root, textvariable=not_var, font=('calibre', 14, 'normal'))

channel_label = tk.Label(root, text='Channel ID', font=('calibre', 10, 'bold'))
channel_entry = tk.Entry(root, textvariable=channel_var, font=('calibre', 14, 'normal'))

bot_token_label = tk.Label(root, text='Bot Token', font=('calibre', 10, 'bold'))
bot_token_entry = tk.Entry(root, textvariable=bot_token_var, font=('calibre', 14, 'normal'))

sub_btn = tk.Button(root, text='Submit', command=submit)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)


not_label.grid(row=1, column=0)
not_entry.grid(row=1, column=1)

channel_label.grid(row=2, column=0)
channel_entry.grid(row=2, column=1)

bot_token_label.grid(row=3, column=0)
bot_token_entry.grid(row=3, column=1)

sub_btn.grid(row=4, column=0)

root.mainloop()
