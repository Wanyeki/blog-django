import os



def save_img(files,student_id):
    print('uploading.....')
    path=os.path.join(os.getcwd(),'datasets/'+str(student_id))
    os.makedirs(path)
    

    for count,x in enumerate(files):
        def process(f):
            with open(path+'/image_'+str(count)+'.jpg','wb') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    
    print('training.......')