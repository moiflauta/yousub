import youtube_dl

from modulos.imprime_cosas import imprime_cosas


lavidamodernaYoutube = "https://www.youtube.com/watch?v=tEhaJ4r15zA"
etherum = 'https://www.youtube.com/watch?v=jp46KmeexxI'
nuevaEsperanza = 'https://www.youtube.com/watch?v=BFXsnuJg2nQ'
listaVideos = [lavidamodernaYoutube, etherum, nuevaEsperanza]
video_input = listaVideos[1]


class objetoYouTube():

    def __init__(self, video_in):  # Un buen sitio para meter el idioma
        self.video_in = video_in
        self.datosVideo = self.datosVideo()
        self.direccionVideo = self.direccionVideo()

        # Aquí podríamos añadir un if para el caso en que no existan subtítulos, llamar al subtítulo automático


    def datosVideo(self):
        """Obtiene la info del vídeo"""

        ydl = youtube_dl.YoutubeDL()
        with ydl:
            resultado = ydl.extract_info(
                self.video_in,
                download=False  # We just want to extract the info
            )
        return resultado


    def direccionVideo(self):
        """Esta función retorna la dirección real del vídeo de mayor calidad.
        Necesaria para usar ffmpeg."""

        direccionVideoFfmpeg = sorted(self.datosVideo['formats'], key=lambda k: int(k['format_id']), reverse=True)[0]['url']
        return direccionVideoFfmpeg


    def subtituloAutomatico(self):

        # Podríamos cargarnos el contenido de la carpeta temp
        # %(title)s-%(id)s.%(ext)s  ->  título-id.ext  -> ¿Qué es el Ethereum y como invertir en el-jp46KmeexxI.es.ttml

        ydl_opciones = ['--ignore-config', '--sub-format=ttml', '--convert-subs=vtt', '--sub-lang=es',  '--write-auto-sub', '--convert-subs=srt', '--skip-download', self.video_in, '-otemp/%(title)s-%(id)s.%(ext)s']
        youtube_dl.main(ydl_opciones)


ytobjeto = objetoYouTube(video_input)

