import vk, time, os , os.path

debug = False
print("Whats your OS?")
print("Windows(1) or Linux/Termux(2)")
type = int(input())
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
elif type != 1 and type != 2 : 
    os.system("exit")
debugi = int(input("Debug(1) or Not(Any number besides 1):"))
if debugi == 1 : debug = True
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
if type == 1 and os.path.isfile("C:/token.txt") : 
  loadtoken = input("Load last token?(y/n): ")
  if loadtoken == 'y' : 
    tokenfile1 = open("C:/token.txt")
    TOKEN = tokenfile1.read()
elif type == 2 and os.path.isfile("/../sdcard/android/savetoken/token.txt"): 
  loadtoken = input("Load last token?(y/n): ")
  if loadtoken == 'y' : 
    tokenfile1 = open("/../sdcard/android/savetoken/token.txt")
    TOKEN = tokenfile1.read()
else : loadtoken = 'n'
if loadtoken != 'y' :
 TOKENlink = input('Access token link:')
 TOKEN1 = TOKENlink.rsplit('access_token=')
 TOKEN2 = TOKEN1[1]
 TOKEN3 = TOKEN2.rsplit('&expires_in')
 TOKEN = TOKEN3[0]
 savetoken = input('Save token?(y/n): ')
else :
 print("Access token is:" + str(TOKEN))


if type == 1 and savetoken == 'y' :
 tokenfile = open('C:/token.txt', 'w')
 tokenfile.write(TOKEN)
 tokenfile.close()
elif type == 2 and savetoken == 'y' :
 tokenfile = open('/../sdcard/android/savetoken/token.txt', 'w')
 tokenfile.write(TOKEN)
 tokenfile.close()
 
time.sleep(1)
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
post_coment = 0
postID = 0
link = input(str('Link to post:'))
time.sleep(1)
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
mess = input('Comment:')
time.sleep(1)
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
print("Use Default if you use page access token!")
typem = int(input('Type:Default(1) , Jitter(2) , Custom(3):'))
if typem != 1 and typem != 2 and typem !=3 :
 print("ERROR[Code:2]")
 if type == 1 :
  os.system("pause")
  os.system("exit")
 elif type == 2 :
  os.system("exit")
if typem == 3 : 
 print("Select number of comms in wave")
 print("Write number between 3 and 7:")
 typem = int(input())
 if typem < 3 and typem > 7 : 
  print("ERROR[Code:3]")
  if type == 1 :
   os.system("pause")
   os.system("exit")
  elif type == 2 :
   os.system("exit")
 
 
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
if typem == 1 : print("Selected:Default")
elif typem == 2 : print("Selected:Jitter")
elif typem == 3 : print("Selected:" + str(typem) + " comms in wave")

linksplitany = link.rsplit('wall')[1]
linksplit2 = linksplitany.rsplit('_')[0]
linksplit3 = linksplitany.rsplit('_')[1]
if debug == True :
 print('list 1 is:' + linksplit2)
 print(' ')
 
post_coment = linksplit2


if debug == True :
 print('list 2 is:' + str(linksplit3))
 print(' ')
 
postID = linksplit3
 
session = vk.Session(access_token=TOKEN)
api = vk.API(session ,v='5.92', lang='ru')

if debug == True :
 print('postID is:' + str(postID))
 print('post coment is:' + str(post_coment))
 
print(" ")
print("Time between waves(1-10): ")
coldown = int(input())
if coldown > 10 : coldown = 10
if coldown < 1 : coldown = 1
if coldown != 0 : print("time between comms is:" + str(coldown))
else : 
 print("ERORR[Code:1]") 
 if type == 1 :
  os.system("pause")
  os.system("exit")
 elif type == 2 :
  os.system("exit")
time.sleep(3)
print("Started")
time.sleep(2)
counter = 0
rangeclamp = typem + 1
while counter != 999:
    for n in range(1,rangeclamp) :
     (api.wall.createComment(owner_id=post_coment,post_id=postID,message=mess))
     counter += 1
    
    if type == 1 : os.system("cls")
    elif type == 2: os.system("clear")
    print("       •Comment++•")
    print("Already sent:" + str(counter))
    print("Powered by Termux-Lab")
    print("by aFro(Ivan Vakushin)")
    
    time.sleep(int(coldown))
