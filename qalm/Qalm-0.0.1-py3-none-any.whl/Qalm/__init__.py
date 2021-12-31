from subprocess import call as shell
import json 

r"""
Qalm is way to handle Files IO in One-Line

> Normal files IO

- Read from a file 
x = pen_head('foo.txt' , "r")

- Get a file lines as an iterator

x = pen_head('foo.txt' , "rl")

- Write to a file 
x = pen_head('foo.txt' , "w" , "boo")

- append to a file 
x = pen_head('foo.txt' , "a" , "boo")

-You also can use kwargs & set a file stat
pen_head(Path = test.txt , Mode = 'w' , Content = 'test', stat = [True , "+h +r +s"]) 

> JSON files IO :

- Read from a JSON file 
json_pen("test.json","r")

- Write to a JSON file 
jd = {"foo" : "boo","foo2":"boo2"}
x = json_pen('foo.json' , "w" , jd)

- append to a file 

tag = {"foo":'boo',
           "boo2": [ "boo", "foo" ],
            "boo3": [ "boo1", "foo2" ]}

json_pen("foo.json", "a" , tag, "foo0")

"""



def pen_head(*args,**kwargs):
	"""
> Normal files IO

- Read from a file 
x = pen_head('foo.txt' , "r")

- Get a file lines as an iterator

x = pen_head('foo.txt' , "rl")

- Write to a file 
x = pen_head('foo.txt' , "w" , "boo")

- append to a file 
x = pen_head('foo.txt' , "a" , "boo")

-You also can use kwargs & set a file stat
pen_head(Path = test.txt , Mode = 'w' , Content = 'test', stat = [True , "+h +r +s"]) """ 

	if not kwargs: 
		try :
			Path,Mode,Content =args
		except:
			try :		
				Path,Mode,Content,stat=args
			except :
				Path,Mode=args

	else :
		try :
			Path,Mode,Content =kwargs['Path'] , kwargs['Mode'], kwargs['Content']
		except :
			try :
				Path,Mode,Content,stat=kwargs['Path'] , kwargs['Mode'] ,kwargs['Content'],kwargs['stat']
			except :
				Path,Mode=kwargs['Path'] , kwargs['Mode']

	with open(Path , Mode) as file :
		
		if file.mode == 'r' or file.mode == "rb" == file.mode == "r+":
			return file.read()
		
		elif file.mode == 'w' or file.mode  == "a" or file.mode  == "wb" or file.mode  == "w+":
			file.write(Content)

		elif file.mode  == "rl":
			return file.readlines()

		try :	
			shell('attrib {} {}'.format(stat ,Path))
		except: pass


def json_pen(*args,**kwargs):

	"""
> JSON files IO :

- Read from a JSON file 
json_pen("test.json","r")

- Write to a JSON file 
jd = {"foo" : "boo","foo2":"boo2"}
x = json_pen('foo.json' , "w" , jd)

- append to a file 

tag = {"foo":'boo',
           "boo2": [ "boo", "foo" ],
            "boo3": [ "boo1", "foo2" ]}

json_pen("foo.json", "a" , tag, "foo0")"""

	if not kwargs: 
		try :
			Path,Mode,Content =args
		except:
			try :		
				Path,Mode,Content,Mother=args
			except :
				Path,Mode=args

	else :
		try :
			Path,Mode,Content =kwargs['Path'] , kwargs['Mode'], kwargs['Content']
		except :
			try :
				Path,Mode,Content,Mother=kwargs['Path'] , kwargs['Mode'] ,kwargs['Content'],kwargs['Mother']
			except :
				Path,Mode=kwargs['Path'] , kwargs['Mode']

	if Mode == "a" : Mode = "r+"

	with open(Path ,Mode) as file :
		
		if file.mode == 'r' or file.mode == "rb":
			return json.load(file)
		
		elif file.mode == 'w' or file.mode  == "wb":			
			json.dump(Content,file, ensure_ascii= False ,indent=None)

		elif file.mode  == "r+" :
			first_insight = json.load(file)
			first_insight[Mother].append(Content)
			file.seek(0)
			json.dump(first_insight, file, indent =3)
