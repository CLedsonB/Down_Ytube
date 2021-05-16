from pytube import YouTube as YT
from pytube import Playlist
import os
import subprocess
import time as t

vid = r"caminho_para_download"
#EXEMPLO
#vid = r"C:\pasta1\pasta2\ "
#SIM, É IMPORTANTISSIMO ESSE ESPAÇO NO FINAL
#CRIAR PASTA NO DESTINO DE DOWNLOAD

os.chdir(vid)
name = input("  Nome da pasta (Sem separar caracteres)\n  -> ")
subprocess.call('mkdir %s' %name, shell= True)

#CONCATENAR PARA SE TORNAR O CAMINHO DE DOWNLOAD
vid += name



opc = int(input("\n  1 = Playlist\n  2 = Videos Aleatórios\n-> "))


#BAIXAR PLAYLIST

if(opc==1):
	form = int(input("\t1 = Retorno de videos com imagem\n\t2 = Retorno de video somente com audio (Ocupa menos espaço de armazenamento)\n\t-> "))

	enter = input("\n\tLink da playlist:\n\t-> ")
	playl = Playlist(enter)

#EM CASO DE FALHA DURANTE DOWNLOAD
#PODE RETORNA O DOWNLOAD DE ONDE PAROU
#POR MEIO DO NUMERO APRESENTADO AO LADO DO TITULO

	names = input("\n  Desejar ver os titulos de todos os videos da playlist? (s = sim / n = não)\n  ->")

	if(names=='s'):
		print("\n----Titulos de todos os videos da playlist----")
		i = 0
		for video in playl.videos:
			print('\n\t({}) {}'.format(i,video.title))
			i += 1

	control = int(input("\tDesejar começar os downloads a partir de qual video?\n\tDigite seu número\n\t->"))


#DOWNLOAD DE PLAYLIST EM FORMATO DE VIDEO

	if(form == 1):
		i = 0
		for video in playl.videos:
			if(i>=control):
				print('\n\t({})  Baixando -> {} -> {}'.format(i,video.title, video.watch_url))
				video.streams.\
				filter(type='video', progressive=True, file_extension='mp4').\
				order_by('resolution').\
				desc().\
				first().\
				download(vid)
				t.sleep(1)
			i += 1

#DOWNLOAD DE PLAYLIST EM FORMATO DE AUDIO

	if(form == 2):
		i = 0
		for video in playl.videos:
			if(i>=control):
				print('\n\t({})  Baixando -> {} -> {} \n'.format(i,video.title, video.watch_url))
				audio = video.streams.\
				get_audio_only()
				audio.download(vid)
			i += 1
				
	if(form>2):
		print("\nERROR\n")

	print("---%d DOWNLOADS CONCLUIDOS---" %(i))

#PARA QUEM ESCOLHEU PLAYLIST, O PROGRAMA ACABA AQUI

#BAIXAR VIDEOS ALEATÓRIOS

if(opc==2):
	
	url = []; yt = []; res = [];

	print("\nDURAÇÃO ACIMA DE 4H NÃO SERÃO BAIXADOS")
	print("\nTRANSMISSÕES AO VIVO NÃO SERÃO BAIXADOS\n")

	rep = int(input("\tNumero de links para usar? "))

	rep += 1
	url += rep*[0]
	yt += rep*[0]

	format = int(input("  1 = Retorno de videos com imagem\n  2 = Retorno de video somente com audio (Ocupa menos espaço de armazenamento)\n  -> "))

#RECEBE LINKS DO YOUTUBE E EXIBIR INFORMAÇÕES
	i = 1
	for i in range(rep-1):
		print("\n-----------------------------------------\n")
		url[i] = str(input("\tEntre com URL_%d_: " %(i)))

		yt[i] = YT(url[i])
		print("")
		print(" (%d) Titulo: %s" %(i,yt[i].title))

		temp = yt[i].length
		h = temp/3600
		min = temp/60
		s = temp
		print("  Duração: %d h =~ %d min =~ %d segs" %(h,min,s))

#RETIRAR LIVE E AO VIVO	

		if(s==0):
			yt.pop(i)

#RETIRAR MAIORES QUE 4H

		if(s>3600*4):
			yt.pop(i)

#DOWNLOAD EM VIDEO

	i = 1
	res = int(input("\n\t1 = Retorno em 720p (melhor qualidade)\n\t2 = Retorno em 360p (qualidade mediana)\n->"))
	for i in range(len(yt)):
		if(format==1):
			print("")

			print("({}) baixando -> {}" .format(i, yt[i].title))
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
#DOWNLOAD EM AUDIO

		if(format==2):
			print("")
			audio = yt[i].streams.get_audio_only()
			audio.download(vid)

	print("---%d DOWNLOADS CONCLUIDOS---" %(rep-1))
