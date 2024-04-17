def naamcontrole(naam):  
 #   if naam(1, len(naam)) in ("a","b","c","d","e","f","g",h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
  #  A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z):
    for letter in naam: 
        if letter in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
        "t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
        "R","S","T","U","V","W","X","Y","Z"]:
            return letter 

    else: 
        return ("dit is geen geldige naam")