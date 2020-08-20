import os
#print(os.getcwd())
os.chdir(path='/home/iamvijay/Desktop/CDK_GLOBAL/Ab-inbev/')
#print(os.listdir()) lists all files and folders in specified path in list format
#print(os.path.exists('/home/')) # verifies a path exists
#os.path.join('abc', 'def')  -> abc/def
#print(os.path.dirname('/home/iamvijay/Desktop')) # it gives DIRNAME as iamvijay
#print(os.path.abspath(path=)# gives absolute path
#print(os.system(command='ls -la'))
#print(os.getpid()) ->provide process id
# os.chdir('../')  # one step back from the cwd
# data=os.getcwd()
# for dirpath, dirname, filename in os.walk(top=data):
#     print("Directory Path: ", dirpath)
#     print('')
#     print('Directory Name: ', dirname)
#     print('')
#     print('Filename: ', filename)
#     print('*'*70)
# os.mkdir('videos')
# os.chdir('videos')
# f = open('abc.txt', 'w')
# f.write('hi')
# f.close()
#os.makedirs('videos/audios/')
print(os.getcwd())
#os.rmdir('videos')
#os.makedirs('videos/audios/travello/')
#os.removedirs('videos/audios/travello/')-->removes all folders recursively..
