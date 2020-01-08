def proba_is_negative(com):
    assert type(com) is str, "Vous devez rentrez un commentaire sous la forme d'une chaine de caractères"
    p = terme2 = 0
    com = com.lower()
    
    if "délai" in com:
        terme2 = 0.6
    else:
        terme2 = (1-0.6)

    if "prix" in com:
        terme2 = terme2*0.8
    else:
        terme2 = terme2*(1-0.8)
        
    if "vendeur" in com:
        terme2 = terme2*0.4
    else:
        terme2 = terme2*(1-0.4)
        
    if "responsable" in com:
        terme2 = terme2*0.2
    else:
        terme2 = terme2*(1-0.2)
        
    p = ((0.5*terme2)/0.12)
    print(p*100)

proba_is_negative("Délai d’attente trop important et mauvais rapport qualité prix ")