# In this file you can put your own information

def config():

    dictionary = {}

    names = ('Wilson Fino; '+ 
             'Javier Bedoya; '+
             'Miguel Sánchez; '+
             'Jhon Aldana; '+
             'Ramón Castaño;'+
             'Lennys Caré')

    ids = '91250331; 71795542; 1098763422; 14138841; 1053790312; 1045141535'

    email_scrum_master = 'monchouam@gmail.com'

    name_of_the_team =  'Quantum'

    dictionary['names'] = names
    dictionary['ids'] = ids
    dictionary['email'] = email_scrum_master
    dictionary['team_name'] = name_of_the_team

    print('Config OK')
    return dictionary
