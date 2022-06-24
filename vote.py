import json,samino,threading,time,sys





def Animation(text):
	for letter in text + '\n':
	    sys.stdout.write(letter)
	    sys.stdout.flush()
	    time.sleep(9/1000)
	    
	    
	    
	    
Animation("""{}
.,  
                                                 ^
                                                ,.
              ,((')/))).                    (()
             '(.(()( )")),                ((())
           "___/,  "/)))/).'               .))
           '.-.   "(()(()()/^             ( (
           ' _)   /)()())(()'______.---._.' )
             '.   _  (()(()))..            ,'
               (() \  ()) ())(             )
                   ((                .     /_
                   /       \,     .-(     (_ )
                 .'   \/    )___.'   \      )
                /    \-    /        _/'.-'  /
               (,(,.'     ))       (_ /    /
                  (,(,(,_)         (,(,(,_)
                  \n\t\t{}    Instagram : w7x7s\033[37m
      """.format("\033[37m","\033[1;33;40m"))	    
	    
c=samino.Client()
Id=c.get_from_link(input("link >>"))
blogId=Id.objectId
comId=Id.comId
c.login(input("email >>"),input("password >>"))
s=samino.Local(comId=comId)
l=(s.get_blog_info(blogId=blogId).json)


def Extracting_information(blog_json):
	info={}
	for element in blog_json.get("polloptList"):info.update({element.get("polloptId"):element.get("title")})
	return info
	
information=Extracting_information(l)


for num,id in enumerate(information.keys(),1):
	print(f"{num} --  {id}  ==>	{list(information.values())[int(num)-1]}",end="\n•\n")
id=list(information.keys())[int(input(" Type a number:"))-1]
print("Starts... ")
json_file = "accounts.json"
f = open(json_file)
data = json.load(f)
s.vote_poll(optionId=id,blogId=blogId)

def vote_poll(client, email, password):
   try:

        client.login(email, password)
        client.join_community(comId)
        samino.Local(comId).vote_poll(optionId=id,blogId=blogId)
        print("\n{}\ndone with: {}\n{}\n".format("\n[",email,"]\n"))
   except (samino.lib.Except) as arg:
     print( "Error with: {} - {}\n".format(email,arg.args[0]))    


for account in data:
    email = account["email"]
    password = account["password"]
    deviceId = account["device"]
    time.sleep(0.5)
    try:
     t=threading.Thread(target=vote_poll, args=(samino.Client(deviceId), email, password, ))
     t.start()
     
     
    except:pass