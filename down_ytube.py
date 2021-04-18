from pytube import YouTube as YT
from pytube import Playlist
import os

vid = os.chdir('C:\\Users\\pc\\Desktop\\Downs')

opc = int(input("1 = playlist\n2 = videos soltos\n->"))


#BAIXAR PLAYLIST

if(opc==1):
	enter = input("\nLink da playlist:\n->")
	playl = Playlist(enter)
	print("\nNúmero de videos presente: %s" %len(playl.videos_uls))
	playl.download_all()
	os.system("start C:/users/pc/Rush_yyz_hq.mp3")



#BAIXAR-ESCOLHER VIDEO OU AUDIO
#DEFINIR QUANTIDADE

if(opc==2):

	url = []; yt = []; res = [];

	print("\nDURAÇÃO ACIMA DE 4H NÃO SERÃO BAIXADOS")
	print("\nTRANSMISSÕES AO VIVO NÃO SERÃO BAIXADOS\n")

	rep = int(input("\tNumero de links para usar? "))

	rep += 1
	url += rep*[0]
	yt += rep*[0]
	res += rep*[0]


	format = int(input("\t1 = Retorno em .mp4, 2 = Retorno em .mp3?\n->"))

#RECEBE LINKS DO YOUTUBE E EXIBIR INFORMAÇÕES

	i=1
	while i<rep:
		print("\n-----------------------------------------\n")
		url[i] = str(input("  Entre com URL_%d_: " %(i)))

		yt[i] = YT(url[i])
		print("")
		print(yt[i].streams.filter(mime_type="video/mp4"))
		print("")
		print("  Titulo: %s"%(yt[i].title))

		res[i] = int(input("  \t 1 = Retorno em 720p\n2 = Retorno em 360p\n"))

		temp = yt[i].length
		h = temp/3600
		min = temp/60
		s = temp
		print("  Duração: %d h =~ %d min =~ %d segs" %(h,min,s))

#RETIRAR LIVE E AO VIVO	

		if(s==0):
			yt.pop(yt[i])

#RETIRAR MAIORES QUE 4H

		if(s>3600*4):
			yt.pop(yt[i])
		i+=1

#DOWNLOAD EM VIDEO

	i=1
	while i<rep:
		if(format==1):
			print("")
			if(res[i]==1):
				movie = yt[i].streams\
				.filter(mime_type="video/mp4")\
				.filter(res="720p")\
				.first()\
				.download(vid)

			if(res[i]==2):
				movie = yt[i].streams\
				.filter(mime_type="video/mp4")\
				.filter(res="360p")\
				.first()\
				.download(vid)

			print("Movie %d Salve" %(i))
#DOWNLOAD EM AUDIO

		if(format==2):
			print("")
			audio = yt[i].streams.get_audio_only()
			audio.download(vid)
	
			print("Audio %d Salve" %(i))
		i+=1
	
	print("\t\t%d DOWNLOADS CONCLUIDOS" %(rep-1))



#https://www.youtube.com/watch?v=Wfi8jY_Dm8k