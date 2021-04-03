def move_string(x,y):
    '''
    Transforme un coup en un format lisible
    '''
    outstr='Possible moves:'
    outstr= chr(ord('@')+y+1)+str(x+1)
    return outstr