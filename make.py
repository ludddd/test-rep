import os
import sys 
try:
    import _winreg as winreg
except ImportError:
    import winreg as winreg
import zipfile	
    
platform = 'win32'
if len(sys.argv) > 1:
	platform = sys.argv[1]
print('building for platform %s' % platform)	

def getUnityPath():
    regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Unity Technologies\\Installer\\Unity')
    path = winreg.QueryValueEx(regkey, 'Location x64')[0]
    path = os.path.join(path, 'Editor', 'Unity.exe')
    return path.replace('\\', '/')

#unityPath = '"D:/Program Files/Unity/Editor/Unity.exe"'
unityPath = '"%s"' % getUnityPath()
print(unityPath)

targetName = './test_auto'

def getExeName(name):
	return name + '.exe'
	
def getDataFolderName(name):
	return name + '_Data'

projectPath = os.path.abspath('./test')
buildTarget = {'win32' : 'BuildGame.BuildWindows', 'android' : 'BuildGame.BuildAndroid'}
#-buildWindowsPlayer
#cmd = '%s -batchmode -projectPath %s -buildTarget %s %s -quit' % (unityPath, projectPath, buildTarget[platform], getExeName(targetName))
cmd = '%s -batchmode -projectPath %s -executeMethod %s -quit' % (unityPath, projectPath, buildTarget[platform])
print(cmd)
os.system(cmd)

def packResult(name):
	z = zipfile.ZipFile('build_win32.zip', 'w')
	z.write(getExeName(name))
	for root, _, filenames in os.walk(getDataFolderName(name)):
		for name in filenames:
			name = os.path.join(root, name)
			name = os.path.normpath(name)
			z.write(name, name)
	z.close()
	
packResult('test/' + targetName)	