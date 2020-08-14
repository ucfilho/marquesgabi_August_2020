import numpy as np
import mahotas
def Mahotas_PSD(Size,Foto,Sub_Size,Escolha):    
    
    Prop_Escolhida=[]
    p_foto=Foto
    GLCM=[]
    glcm_haralick=[]
    x_ref=[]
    Count=Sub_Size
    p=np.zeros((Sub_Size,Sub_Size))
    j_ref=0
    Cada_foto=[]
    Posicao_X=[]
    Posicao_Y=[]
    for k in range(Size):
      if((k+Sub_Size-1)<Size):
        for i in range(Sub_Size):
          Posicao_X.append(Crop+i)
          for j in range(Sub_Size):
            p[i,j]=p_foto[Crop+i,j+k]
            Posicao_Y.append(j+k)

        WW=np.copy(p) 
        Cada_foto.append(WW.ravel())
        x_ref.append(Count-Sub_Size)
        Count=Count+1
      
        Mahotas =pd.DataFrame(mahotas.features.haralick(p.astype(int)), columns =Escolha)
        Prop_Escolhida.append(Mahotas[Prop].mean())

    Todas_Fotos.append(Prop_Escolhida)

    df_mahotas=pd.DataFrame(Todas_Fotos)
    
    return(df_mahotas)
