import os, sys, json

back = False

def dp_error(msg='Error with data pack.\nCheck if it is incomplete or if the wrong directory was given'):
    print(msg)
    sys.exit()
#item entity @s armor.head replace stone
def update_function_dir(fn_path, bck):
    files = os.listdir(fn_path)
    for fn in files:
        if fn.endswith('.mcfunction'):
            with open(fn_path+'\\'+fn,'r+') as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if back:
                        if 'item entity' in lines[i] or 'item block' in lines[i]:
                            slot = lines[i].split('item')[1].split(' ')[3]
                            lines[i] = lines[i].replace(slot+' replace', slot)
                            lines[i] = lines[i].replace('item', 'replaceitem')
                    else:
                        if 'replaceitem' in lines[i]:
                            slot = lines[i].split('replaceitem')[1].split(' ')[3]
                            lines[i] = lines[i].replace(slot, slot+' replace')
                            lines[i] = lines[i].replace('replaceitem', 'item')
                f.seek(0)
                f.write("".join(lines))
                
        else:
            update_function_dir(fn_path+'\\'+fn, bck)

if not sys.argv[1]=='-help':
    if sys.argv[1]=='-back':
        path = sys.argv[2]
        back = True
    else:
        path = sys.argv[1]

    files = os.listdir(path)
    
    #update pack.mcmeta
    if 'pack.mcmeta' in files:
        with open(path+'\\pack.mcmeta','r+') as f:
            try:
                mcmeta = json.load(f)
            except json.decoder.JSONDecodeError:
                dp_error('Error with data pack\'s pack.mcmeta file.\nCheck if it is incomplete or if the wrong directory was given.')
            if back:
                mcmeta['pack']['pack_format']=6
            else:
                mcmeta['pack']['pack_format']=7
            f.seek(0)
            f.write(json.dumps(mcmeta,indent=4))
    else:
        dp_error()
        
    #update functions
    if 'data' in files:
        path += '\\data'
        files = os.listdir(path)
        for s in files: 
            if not s == 'minecraft':
                path += '\\'+s
        funcs_path = path + '\\functions'
        update_function_dir(funcs_path, back)                 
    else:
        dp_error()
else:
    print('Welcome to the data pack 1.17 converter python script.')
    print('\n1. Find your data pack you want to update and unzip it into a folder if it is in a .zip-file')
    print('2. Optimally make a backup of that data pack')
    print('3. Open the folder so that you see the file \"pack.mcmeta\" and the folder \"data\"')
    print('4. Copy the path of the current folder')
    print('5. Open CMD again and execute the command \"python dp_update.py <folder path>\"')