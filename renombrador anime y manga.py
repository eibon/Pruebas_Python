print("Renamer Anime & Manga\n Ver.0.0.0.1 Alfa\n\n\n\n")
print ("hola este programa es para crear listas para un archivo *.bat encargado de\n renombrar una lista de archivos")
print ("funciono para renombrar un nomero grande de archivos segun una plantilla")
print("tambien para cambiarles la terminacion o tipo de archivo")
print ("como cuando cambia de un archivo *.rar o *.zip a *.cbr o *.cbz ")
##vcf=""
j=1
while j!=0:

    print("primero tendras que especificar que tipo de archivo convertiras")
    print("sera anime o manga?")
    print ("1.- Anime \n2.-Manga \n3.-Salir")
    anime_o_manga=int(input("~$"))
    if anime_o_manga==1:
        print ("seleccionaste el renombrar anime")
        archivo_origen =input("proporcione el nombre del archivo origen ejemplo '2478'~$  ")
        print(archivo_origen)
        tipoarchivoorigen=input("indique el tipo de archivo ejempleo 'MP4' en caso de no tener tipo poner '*'~$  ")
        print(archivo_origen,".",tipoarchivoorigen)
        numerodarchivos =int (input("ingrese el numero de archivos totales~$  "))
        print(archivo_origen,"_",numerodarchivos,".",tipoarchivoorigen)
        archivo_destino =input("proporcione el nombre de la serie, poniendo _ en vez de espacios ejemplo 'Zero_No_Tsuakaima'~$  ")
        print(archivo_origen,"_",numerodarchivos,".",tipoarchivoorigen,"  ",archivo_destino,"_",numerodarchivos,".",tipoarchivoorigen)

        tipoarchivof=input("por favor proporciona el tipo de archivo final ejemplo 'mp4, avi, mkv' ~$  ")
        print ("deseas que aparesca el nombre de fansub, pagina o alguna informacion que desees antes del nombre de la serie ?")
        respuesta=input("S/N~$  ")
        ##respuesta=respuesta.lower()

        if respuesta == 's':
            fansuborigen=input("proporcione el nombre del fansub o pagina de origen, ejemplo ANIMEFLV o NANIKANO ~$  ")
            print(archivo_origen,"_",numerodarchivos,".",tipoarchivoorigen,"  ","[",fansuborigen,"]",archivo_destino,"_",numerodarchivos,".",tipoarchivoorigen)
            print("ejemplo de la cadena que se generara:")
            print("ren ",archivo_origen,numerodarchivos,".",tipoarchivoorigen,"  ","[",fansuborigen,"]",archivo_destino,numerodarchivos,".",tipoarchivoorigen)
            nombreren=input("por ultimo que nombre deseas que tenga el archivo convertidor? recuerde poner .bat ~$  ")

            numerodarchivos=numerodarchivos+1

            f = open (nombreren, 'w')
            i=1
            for i in range (numerodarchivos):
                ##print (archivo_origen,"_",i)
                numerochar=str(i)

                if i<10 and i > 0:
                    f.write('ren'+'  '+archivo_origen+'_'+numerochar+'.'+tipoarchivoorigen+'   '+'['+fansuborigen+']'+archivo_destino+'_'+'0'+numerochar+'.mp4''\n')
                elif i>=10 and i > 0:
                    f.write('ren'+'  '+archivo_origen+'_'+numerochar+'.'+tipoarchivoorigen+'   '+'['+fansuborigen+']'+archivo_destino+'_'+numerochar+'.mp4''\n')


            f.close()
        elif respuesta=='n':

            ##print(archivo_origen,"_",numerodarchivos,".",tipoarchivoorigen,"  ","[",fansuborigen,"]",archivo_destino,"_",numerodarchivos,".",tipoarchivoorigen)
            print("ejemplo de la cadena que se generara:")
            print("ren ",archivo_origen,numerodarchivos,".",tipoarchivoorigen,"  ",archivo_destino,numerodarchivos,".",tipoarchivoorigen)
            nombreren=input("por ultimo que nombre deseas que tenga el archivo convertidor? recuerde poner .bat ~$  ")

            numerodarchivos=numerodarchivos+1

            f = open (nombreren, 'w')
            i=1
            for i in range (numerodarchivos):
                ##print (archivo_origen,"_",i)
                numerochar=str(i)

                if i<10 and i > 0:
                    f.write('ren'+'  '+archivo_origen+'_'+numerochar+'.'+tipoarchivoorigen+'   '+archivo_destino+'_'+'0'+numerochar+'.mp4''\n')
                elif i>=10 and i > 0:
                    f.write('ren'+'  '+archivo_origen+'_'+numerochar+'.'+tipoarchivoorigen+'   '+archivo_destino+'_'+numerochar+'.mp4''\n')


            f.close()


    elif anime_o_manga==2:
        print("seleccionaste renombrar manga")
        print("esta opcion sirve para renombrar archivos *.rar o *.zip y nombrarlos como archivos de comic electronico cbr")
        print("NOTA VERIFICA QUE EL ARCHIVO NO ESTE PROTEGIDO POR CONTRASEÑA!!!!!!")
        print ("Deseas canbiar el nombre completo o solo la extencion?")
        print ("1.- Nombre completo \n2.-Cambiar extencion")

        opcion=int(input("~$  "))
        if opcion ==1:
            mangaor=input("proporciona el nombre del archivo comprimido ~$  ")
            tipo=int(input("que tipo de archivo es? \n1.-Zip\n2.-Rar ~$  "))
            if tipo==1:
                tipof=".zip"
            elif tipo==2:
                tipof=".rar"

            voci=int(input("son volumenes o capitulos?\n1.-volumenes\n2.-capitulos\n~$  "))
            if voci ==1:
                vcf = "vol"

            elif voci==2:
                vcf = "cap"

            print ("fin if ",vcf)
            print ("ejemplo de la cadena resultante: ", mangaor,vcf, "00" ,tipof )## lina para pruebas
            nmangf=input("que nombre final del manga ~$  ")
            nombremanga=input("nombre del bat ~$  ")
            print ("la numeracion de origrn es \n1.-1, 2, 3  \n2.-01, 02, 03")
            numer = int (input(" ~$"))
            if numer == 1:
                print("cual es el numero de archivos? ")
                numcv=int(input("~$  "))
                numcv=numcv+1
                f = open (nombremanga, 'w')
                i=1
                for i in range (numcv):
                    ##print (archivo_origen,"_",i)
                    numerochar=str(i)

                    if i<10 and i > 0:
                        f.write('ren'+'  '+mangaor+'_'+vcf+'_'+numerochar+tipof+'   '+nmangf+'_'+vcf+'_00'+numerochar+'.cbr''\n')
                    elif i>=10 and i < 100:
                        f.write('ren'+'  '+mangaor+'_'+vcf+'_'+numerochar+tipof+'   '+nmangf+'_'+vcf+'_0'+numerochar+'.cbr''\n')
                    elif i>=100 and i>0:
                        f.write('ren'+'  '+mangaor+'_'+vcf+'_'+numerochar+tipof+'   '+nmangf+'_'+vcf+'_'+numerochar+'.cbr''\n')


                f.close()
            elif numer == 2:
                print("cual es el numero de archivos? ")
                numcv=int(input("~$  "))
                numcv=numcv+1
                f = open (nombremanga, 'w')
                i=1
                for i in range (numcv):
                    ##print (archivo_origen,"_",i)
                    numerochar=str(i)

                    if i<10 and i > 0:
                        f.write('ren'+'  '+mangaor+'_'+vcf+'_00'+numerochar+tipof+'   '+nmangf+'_'+vcf+'_00'+numerochar+'.cbr''\n')
                    elif i>=10 and i < 100:
                        f.write('ren'+'  '+mangaor+'_'+vcf+'_0'+numerochar+tipof+'   '+nmangf+'_'+vcf+'_0'+numerochar+'.cbr''\n')
                    elif i>=100 and i>0:
                        f.write('ren'+'  '+mangaor+'_'+vcf+'_'+numerochar+tipof+'   '+nmangf+'_'+vcf+'_'+numerochar+'.cbr''\n')

                f.close()

        elif opcion == 2:
            f = open ('Manga.bat', 'w')
            f.write('ren *.rar *.cbr\n ren *.zip *.cbr')
            f.close()

    elif anime_o_manga==3:
        j=0
    elif anime_o_manga==4:
        print("Developed By EibonMc\n ")


input("<<<<<fin del programa, precione cualquier tecla>>>>>")
