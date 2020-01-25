import vk, time, os , os.path
TOKEN = 0
savetoken = 'n'
debug = False
print("Whats your OS?")
type = int(input("Windows(1) or Linux/Termux(2): "))
if type < 2 or type > 1 : os.system("exit")
checkupdates = input("Do you want to check updates?(y/n)")
if checkupdates == 'y' : 
 os.system("php upd.php")
 if type == 1 : os.system("cls")
 elif type == 2: os.system("clear")
 print("Start again!(python start.py)")
 os.system("exit")

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
elif type == 2 and os.path.isfile('token'): 
  loadtoken = input("Load last token?(y/n): ")
  if loadtoken == 'y' : 
    tokenfile1 = open("token.txt")
    TOKEN = tokenfile1.read()
else : loadtoken = 'n'
if loadtoken == 'n' :
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
 tokenfile = open('token', 'w')
 tokenfile.write(TOKEN)
 tokenfile.close()
 
time.sleep(1)
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
post_coment = 0
postID = 0
link = input(str('Link to post:'))
linktype = int(input('Post(1) | Photo(2) :' ))
time.sleep(1)
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
mess = input('Comment:')
time.sleep(1)
if type == 1 : os.system("cls")
elif type == 2: os.system("clear")
fromgroupmess = int(input("Group ID(0 if you want post with your page):"))


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
if linktype == 1 :
 linksplitany = link.rsplit('wall')[1]
 linksplit2 = linksplitany.rsplit('_')[0]
 linksplit3 = linksplitany.rsplit('_')[1]
 post_coment = linksplit2
 postID = linksplit3
 if debug == True :
  print('list any is:' + linksplitany)
  print('list 1 is:' + linksplit2)
  print(' ')
  print('list 2 is:' + str(linksplit3))
  print(' ')
  print('Group ID is:' + str(fromgroupmess))
elif linktype == 2 :
 linksplitany = link.rsplit('photo')[1]
 linksplit2 = linksplitany.rsplit('_')[0]
 linksplit3 = linksplitany.rsplit('_')[1]
 linksplit4 = linksplit3.rsplit('%')[0]
 post_coment = linksplit2
 postID = linksplit4
 if debug == True :
  print('list any is:' + linksplitany)
  print('list 1 is:' + linksplit2)
  print(' ')
  print('list 2 is:' + str(linksplit3))
  print(' ')
  print('list 3 is:' + str(linksplit4))
 
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
    if linktype == 1 : 
     for n in range(1,rangeclamp) :
       (api.wall.createComment(owner_id=post_coment,post_id=postID,from_group=fromgroupmess,message=mess))
       counter += 1
    elif linktype == 2 :
     for n in range(1,rangeclamp) :     
        (api.photos.createComment(owner_id=post_coment,photo_id=postID,from_group=fromgroupmess,message=mess))
        counter += 1
    
    if type == 1 : os.system("cls")
    elif type == 2: os.system("clear")
    print("       •Comment++•")
    print("Already sent:" + str(counter))
    print("Message:" + str(mess))
    print("Mess in wave:" + str(typem))
    print("Powered by Termux-Lab")
    print("by aFro(Ivan Vakushin)")
    
    time.sleep(int(coldown))
