print ("hola este programa es para crear listas para un archivo bat encargado de renombrar una lista de archivos")
archivo_origen =input("proporcione el nombre del archivo origen ejemplo '2478'")
tipoarchivoorigen=input("indique el tipo de archivo ejempleo 'MP4' en caso de no tener tipo poner '*'")
numerodarchivos =int (input("ingrese el numero de archivos totales"))
archivo_destino =input("proporcione el nombre de la serie, poniendo _ en vez de espacios ejemplo 'Zero_No_Tsuakaima'")
fansuborigen=input("proporcione el nombre del fansub o pagina de origen, ejemplo ANIMEFLV o NANIKANO")
nombreren=input("por ultimo que nombre deseas que tenga el archivo convertidor? recuerde poner .bat")
numerodarchivos=numerodarchivos+1

f =open (nombreren, 'w')
i=1
for i in range (numerodarchivos):
    ##print (archivo_origen,"_",i)
    numerochar=str(i)

    if i<10 and i > 0:
        f.write('ren'+'  '+archivo_origen+'_'+numerochar+'.'+tipoarchivoorigen+'   '+'['+fansuborigen+']'+archivo_destino+'_'+'0'+numerochar+'.mp4''\n')
    elif i>=10 and i > 0:
        f.write('ren'+'  '+archivo_origen+'_'+numerochar+'.'+tipoarchivoorigen+'   '+'['+fansuborigen+']'+archivo_destino+'_'+numerochar+'.mp4''\n')


f.close()

input(">>>>>>>>>>>>")
