import pickle
def load_data(file):
    try:
        with open(file, 'rb') as f:
            a=pickle.loads(f.read())
    except FileNotFoundError:
        print('Not Found')
    else:
        return a

def query(prof_name):
    depart=[]
    data = load_data("dept-prof.pydata")
    for key,val in data.items():
        if prof_name in data[key]:
            depart.append(key)
    return depart
#query('David')

def update():
    data = load_data("dept-prof.pydata")
    ai = data['Artificial Intelligence']
    del data['Artificial Intelligence']
    data['Computer Science'] += ai
    data['Metaverse']=['Mark','Neo','Trinity']
    with open('dept-prof-updated.pydata', 'wb') as f:
        pickle.dump(data, f)
#update()

def get_depts_size( ):
    data = load_data('dept-prof-updated.pydata')
    dicta={}
    for key,val in data.items():
        dicta[key] = len(val)
    return dicta
#get_depts_size( )