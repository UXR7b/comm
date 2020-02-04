import vk, time, os , os.path ,re
#defines
TOKEN_1 = 0
TOKEN_2 = 0
TOKEN_3 = 0
TOKEN_4 = 0
TOKEN_5 = 0
TOKEN_6 = 0
TOKEN_7 = 0
TOKEN_8 = 0
TOKEN_9 = 0
TOKEN_10 = 0
TOKEN_11 = 0
TOKEN_12 = 0
TOKEN_13 = 0
TOKEN_14 = 0
TOKEN_15 = 0
TOKEN_16 = 0
TOKEN_17 = 0
TOKEN_18 = 0
TOKEN_19 = 0
TOKEN_20 = 0
TOKEN_21 = 0
counter = 0
loadmultitoken = 'n'
savetoken = 'n'
debug = False
multitoken = False
tokenlist = [TOKEN_1,TOKEN_2,TOKEN_3,TOKEN_4,TOKEN_5,TOKEN_6,TOKEN_7,TOKEN_8,TOKEN_9,TOKEN_10,TOKEN_11,TOKEN_12,TOKEN_13,TOKEN_14,TOKEN_15,TOKEN_16,TOKEN_17,TOKEN_18,TOKEN_19,TOKEN_20]


#functions
#--
print("Whats Your System?")
type = int(input("Windows(1) or Termux(2): "))
#--
if type != 2 and type != 1:
 print("ERORR[Code:1]")
 os.system("exit")
#--
def clear():
 if type == 1 : clear1 =os.system("cls")
 elif type == 2: clear1 =os.system("clear")
#--

multitoken1 = int(input("How much tokens?(1-20):"))
if multitoken1 < 1 or multitoken1 > 20 : 
 print("ERROR[Code:1]")
 error()
checkupdates = input("Do you want to check updates?(Y/N)")
if checkupdates != 'y' and checkupdates != 'n' and checkupdates != 'Y' and checkupdates != 'N' :
 print("ERORR[Code:1]")
 error()
if checkupdates == 'y' or checkupdates == 'Y' : 
  os.system("php upd.php")
  clear()
  print("Start again!(python start.py)")
  os.system("exit")
print("Press ENTER if you want to skip.")
debugi = input("Debug(Y)?:")
if multitoken1 > 1:
 multitoken = True
if debugi == 'Y' : 
 debug = True
clear()
n = 1
enl = False
if multitoken1 == 1 : 
 if type == 1 and os.path.isfile("C:/token.txt") : 
   loadtoken = input("Load last token?(y/n): ")
   if loadtoken == 'y' : 
     tokenfile1 = open("C:/token.txt")
     TOKEN_1 = tokenfile1.read()
 elif type == 2 and os.path.isfile('token'): 
   loadtoken = input("Load last token?(y/n): ")
   if loadtoken == 'y' : 
     tokenfile1 = open("token")
     TOKEN_1 = tokenfile1.read()
 else : loadtoken = 'n'
 if loadtoken == 'n' :
  TOKENlink = input('Access token link:')
  TOKEN1 = TOKENlink.rsplit('access_token=')
  TOKEN2 = TOKEN1[1]
  TOKEN3 = TOKEN2.rsplit('&expires_in')
  TOKEN_1 = TOKEN3[0]
  savetoken = input('Save token?(y/n): ')
 else :
  print("Access token is:" + str(TOKEN_1))
elif multitoken1 != 1 and multitoken1 <= 20 :
 en1 = True
 if type == 1 and os.path.isfile("C:/multitoken.txt") : 
  if multitoken1 == len(re.findall(r"[\n']+", open('C:/multitoken.txt').read())):
   loadmultitoken = input("Load last multitoken?(y/n): ")
   if loadmultitoken == 'y' : 
     multitokenfile1 = open("C:/multitoken.txt")
     for n in range(0,multitoken1):
      tokenl1 = multitokenfile1.readline()
      tokenl2 = tokenl1.rsplit("\n")
      tokenlist[n] = tokenl2[0]
 elif type == 2 and os.path.isfile('multitoken'): 
  if multitoken1 == len(re.findall(r"[\n']+", open('multitoken.txt').read())):
   loadmultitoken = input("Load last token?(y/n): ")
   if loadmultitoken == 'y' : 
     multitokenfile1 = open("multitoken")
     for n in range(0,multitoken1):
      tokenl1 = multitokenfile1.readline()
      tokenl2 = tokenl1.rsplit("\n")
      tokenlist[n] = tokenl2[0]
 else : 
  loadmultitoken = 'n'
 if loadmultitoken == 'n':
   for n in range(0,multitoken1) :
    TOKENlinks = input("Token "+ str(n+1) + " is:")
    TOKEN1s = TOKENlinks.rsplit('access_token=')
    TOKEN2s = TOKEN1s[1]
    TOKEN3s = TOKEN2s.rsplit('&expires_in')
    tokenlist[n] = TOKEN3s[0]
    n += 1
   savemultitoken = input("Save multitoken?:")
   if loadmultitoken == 'n':
    if type == 1 and savemultitoken == 'y' :
     multitokenfile = open('C:/multitoken.txt', 'w')
     for n in range(0,multitoken1+1):
      multitokenfile.write(str(tokenlist[n])+"\n")
     multitokenfile.close()
    elif type == 2 and savemultitoken == 'y' :
     multitokenfile = open('multitoken', 'w')
     for n in range(0,multitoken1+1):
      multitokenfile.write(str(tokenlist[n])+"\n")
     multitokenfile.close()
 
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
 print('ERROR[Code:1]')
 
if typem == 3 : 
  print("Select number of comms in wave")
  print("Write number between 3 and 7:")
  typem = int(input())
  if typem < 3 and typem > 7 :
   print("ERROR[Code:1]")
 
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
if multitoken == False:
 session = vk.Session(access_token=TOKEN_1)
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

rangeclamp = typem + 1
mcounter = 0

print(tokenlist)
 
while counter != -1:
   if multitoken == True :
    for n in range(0,multitoken1):
      session = vk.Session(access_token=tokenlist[n])
      api = vk.API(session ,v='5.92', lang='ru')
      if linktype == 1 :
       (api.wall.createComment(owner_id=post_coment,post_id=postID,from_group=fromgroupmess,message=mess))
       mcounter += 1
      elif linktype == 2 :
       (api.photos.createComment(owner_id=post_coment,photo_id=postID,from_group=fromgroupmess,message=mess))
       mcounter += 1
    if type == 1 : os.system("cls")
    elif type == 2: os.system("clear")
    print("       •Comment++•")
    print("       •Multitoken•")
    print("Already sent:" + str(mcounter))
    print("Message:" + str(mess))
    print("Mess in wave:" + str(typem))
    print("Tokens:"+str(multitoken1))
    print("Powered by Termux-Lab")
    print("by aFro(vk.com/sorrybutiloveanother)")
   else:
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
    print("")
    print("Powered by Termux-Lab")
    print("by aFro(vk.com/sorrybutiloveanother)")
    
    time.sleep(int(coldown))
