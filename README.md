# Down_Ytube
Downloads de arquivos do YouTube, unitário ou em quantidade, nos formatos .mp4 e .webm usando pytube
e a última atualização agora permite download de playlists publicas inteiras.

Modo de uso

-> após baixar o arquivo .py

Abrir o arquivo pelo bloco de notas e colocar o caminho para downloads logo no inicio.

->pode executar ele pela prompt de comando do windowns

Primeiramente copia o caminho que está o arquivo baixado e executar na prompt

>>cd c:\pasta1\pasta2\pasta3

em seguida para executar o arquivo

>>python down_ytube.py

Quem for fazer download por playlist precisa só fornecer link de uma playlist publica e um nome para a pasta que vai conter os videos baixados
Se sua internet falhar durante o processo, o programa para de funcionar

Quem for fazer download de alguns videos pode fornecer somente:
-> o link
-> a resoluçao que desejar 720p será a melhor resoluçao disponivel
360p sera a segunda melhor resolucao disponivel.


Dia 15/06 - Atualização

--Código para baixar playlist está funcionando
--Agora não é mais necessario dizer resolução para cada video escolhido para baixar
entre com valor para resolução apenas uma vez e ele se aplicará a todos os videos
--Após muitos teste, recomendo que trabalhe com playlists de 50 videos ou menos
valores maiores tende a falha muito mais fácil.

Dia 16/05 - Atualização
--Você agora pode dizer por qual video da playlist o download vai começar
sabendo que o primeiro video tem o indice 0.
--Se o download de playlist falhar após fazer downloads de vários videos,
você pode pegar o último indice que aparecer e usar
para continuar o download de onde parou. (continue adicionando o mesmo nome da pasta, 
assim eles continuaram tendo o mesmo destino).
