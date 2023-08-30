# -- Bring to you by Vihaan Mody
# -- Enjoy the script!

from pyfiglet import figlet_format
from clint.textui import colored
from pathlib import Path
from yagmail import SMTP

def Send_Email(Sender, Password, Body, Receiver, Subject, Attachments=""):
	if Path(Attachments).is_file():
		pass
	elif Attachments == "":
		pass
	elif Path(Attachments).is_dir():
		print(f"{colored.red('Caution:')} {colored.yellow('Sending Directories Are Not Supported.')}")
		Confirm = input(f"{colored.yellow('?')} Do You Want To Send Email Without Directory(Y/N): ").lower()
		if Confirm == "y" or Confirm == "yes":
			Attachments = ""
		else:
			exit(colored.red("# Email Cancelled #"))
	else:
		print(f"{colored.red('Caution:')} {colored.yellow('This File Was Not Found On Your System.')}")
		Confirm = input(f"{colored.yellow('? ')} Do You Want To Send Email Without Attachment(Y/N): ").lower()
		if Confirm == "y" or Confirm == "yes":
			Attachments = ""
		else:
			exit(colored.red("# Email Cancelled #"))

	Yagmail = SMTP(Sender, Password)
	Contents = [Body]
	Yagmail.send(Receiver, Subject, Contents, Attachments)

def Banner():
	print(colored.blue(figlet_format("Email CLI", "slant")), end = "")
	print(colored.yellow("="*50))
	print(colored.green("\nWelcome To Email CLI") + colored.magenta(" 2.0"))

def Data():
	global From, Password, To, Subject, Body
	try:
		From = input(f"{colored.yellow('?')} Email Sender: ")
		Password = input(f"{colored.yellow('?')} Email Password/App Password: ")
		To = input(f"{colored.yellow('?')} Email Receiver: ")
		Subject = input(f"{colored.yellow('?')} Subject: ")
	except KeyboardInterrupt:
		exit()
	print(f"{colored.yellow('?')} Email Body Content(Ctrl-C To Save): ")
	Contents = []
	Body = ""
	while True:
		try:
			Line = input()
		except EOFError:
			break
		except KeyboardInterrupt:
			break
		Contents.append(Line)
	for i in Contents:
		Body += f"{i}\n"
	try:
		global Attachments
		Attach = input(f"{colored.yellow('?')} Do You want To Send Attachments(Y/N): ").lower()
		if Attach == "y" or Attach == "yes":
			Attachments = input(f"{colored.yellow('?')} Enter Full File Path Of Attachment: ").strip('"')
		else:
			Attachments = ""
	except KeyboardInterrupt:
		exit()
if Path(__file__).name == "emailcli.py":
	Banner()
	Data()
	try:
		Send_Email(From, Password, Body, To, Subject, Attachments)
	except Exception as Error:
		exit(colored.red(str(Error)))
	else:
		print(colored.blue("\n# Mail Sent #"))
