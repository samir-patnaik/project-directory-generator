import os
from string import Template

projectname = raw_input('Enter project name : ')
	# let's say the project name is 'pabitra_lenka' 
projectpath = Template ('K:\Work\${project}')
path = projectpath.substitute ( project = projectname)
	# path is now K:\Work\Pabitra_Lenka
flag = os.system('mkdir' + ' ' + path)

subfolders = [ ['SoundFX', 'VO', 'Music'], [], [], [], [], [], [], [], [], 
			   [], [] ]

folders = [ 'Audio',  'Conform',  
			   'Document', 'Footage',  'Graded',  'Graphics', 
			   'Offline',  'Project', 'Sent_to_Client', 
			   'Transfer',  'VFX', subfolders ]


subfolderpath=[]
for x in range( 0, len(folders)-1):

	subfolderpath.append(path + '\\' + str(folders[x]))
	os.system ('mkdir' + ' ' +  subfolderpath[x])

subsubfolderpath = []
for x in range(0,len(subfolders)):
	for y in range (0, len(subfolders[x])):
		subsubfolderpath.append(subfolderpath[x] +'\\'+str(subfolders[x][y]))
for x in range(0,len(subsubfolderpath) ):
	os.system('mkdir' + ' ' + str(subsubfolderpath[x]))

if flag == 0:
	print 'project ' + projectname + ' sucessfully created at '+ path 
else: 
	print 'Unsuccessful'
