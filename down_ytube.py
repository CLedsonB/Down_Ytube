from pytube import YouTube as YT
from pytube import Playlist
import os
import subprocess

# exemplo
# vid = 'c:\pasta1\pasta2\ '
# sim, o espaço é importante

vid = 'caminho_para_download'

opc = int(input("1 = playlist\n2 = videos soltos\n->"))


#BAIXAR PLAYLIST

if(opc==1):
	form = int(input("\t0 = Retorno em video\n\t1 = Retorno em audio\n\t-> "))

	#CRIAR PASTA PARA GUARDAR ARQUIVOS BAIXADOS
	name = input("Nome da pasta (Sem separar caracteres)\n-> ")
	subprocess.call('mkdir %s' %name, shell= True)
	vid += name

	enter = input("\nLink da playlist:\n-> ")
	playl = Playlist(enter)

	#DOWNLOAD EM .MP4
	if(form == 0):
		for video in playl.videos:
			print('\n\tBaixando -> {} -> {} \n'.format(video.title, video.watch_url))
			video.streams.\
			filter(type='video', progressive=True, file_extension='mp4').\
			order_by('resolution').\
			desc().\
			first().\
			download(vid)

	#DOWNLOAD EM .MP4 SOMENTE AUDIO
	if(form == 1):
		for video in playl.videos:
			print('\n\tBaixando -> {} -> {} \n'.format(video.title, video.watch_url))
			audio = video.streams.get_audio_only()
			audio.download(vid)
	if(form>1):
		print("\nERROR\n")


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


	format = int(input("\t1 = Retorno em video, 2 = Retorno em audio?\n->"))

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
	res = int(input("  \t 1 = Retorno em 720p\n2 = Retorno em 360p\n"))

	i=1
	while i<rep:
		if(format==1):
			print("")
			if(res==1):
				movie = yt[i].streams\
				.filter(mime_type="video/mp4")\
				.filter(res="720p")\
				.first()\
				.download(vid)

			if(res==2):
				movie = yt[i].streams\
				.filter(mime_type="video/mp4")\
				.filter(res="360p")\
				.first()\
				.download(vid)
				
			print('\n\tConcluido -> {} -> {} \n'.format(movie.title, movie.watch_url))
#DOWNLOAD EM AUDIO

		if(format==2):
			print("")
			audio = yt[i].streams.get_audio_only()
			audio.download(vid)
			
			print('\n\tConcluido -> {} -> {} \n'.format(audio.title, audio.watch_url))
		i+=1
	
	print("\t\t%d DOWNLOADS CONCLUIDOS" %(rep-1))
