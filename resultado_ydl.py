import ffmpeg

in_filename = 'https://r2---sn-h5q7rn7s.googlevideo.com/videoplayback?expire=1571643312&ei=UAutXfWjIoGa1wa32pmgBg&ip=176.83.47.244&id=o-AOCxozfy6EJye28sYI6bA9Kn8OXc_obd7Y1EXkQXiS_J&itag=251&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-h5q7rn7s%2Csn-h5q7knee&ms=au%2Crdu&mv=m&mvi=1&pl=16&initcwndbps=1045000&mime=audio%2Fwebm&gir=yes&clen=2884856&dur=209.341&lmt=1571578498613850&mt=1571621679&fvip=2&keepalive=yes&fexp=23842630&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRgIhAPD1xzFYPEKPwgASGHE0qLLzbuXYM4R--qPz2CkR3Y8TAiEAtohV9XS_-Dasqo1-y51hyAcQt35ex4LL7VhqmrmbaTY%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRgIhANFXXEDMrb2lA0XLwi9BPxaNQJ_mDqWwlIaVKqlw28yeAiEA_Ti6OM2AUecmTokDMZpw1DaCt7eE36dhAM7tsozkiek%3D&ratebypass=yes'

#datos = ffmpeg.probe(in_filename)

datos = {'streams': [{'index': 0, 'codec_name': 'opus', 'codec_long_name': 'Opus (Opus Interactive Audio Codec)', 'codec_type': 'audio', 'codec_time_base': '1/48000', 'codec_tag_string': '[0][0][0][0]', 'codec_tag': '0x0000', 'sample_fmt': 'fltp', 'sample_rate': '48000', 'channels': 2, 'channel_layout': 'stereo', 'bits_per_sample': 0, 'r_frame_rate': '0/0', 'avg_frame_rate': '0/0', 'time_base': '1/1000', 'start_pts': -7, 'start_time': '-0.007000', 'disposition': {'default': 1, 'dub': 0, 'original': 0, 'comment': 0, 'lyrics': 0, 'karaoke': 0, 'forced': 0, 'hearing_impaired': 0, 'visual_impaired': 0, 'clean_effects': 0, 'attached_pic': 0, 'timed_thumbnails': 0}, 'tags': {'language': 'eng'}}], 'format': {'filename': 'https://r2---sn-h5q7rn7s.googlevideo.com/videoplayback?expire=1571643312&ei=UAutXfWjIoGa1wa32pmgBg&ip=176.83.47.244&id=o-AOCxozfy6EJye28sYI6bA9Kn8OXc_obd7Y1EXkQXiS_J&itag=251&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-h5q7rn7s%2Csn-h5q7knee&ms=au%2Crdu&mv=m&mvi=1&pl=16&initcwndbps=1045000&mime=audio%2Fwebm&gir=yes&clen=2884856&dur=209.341&lmt=1571578498613850&mt=1571621679&fvip=2&keepalive=yes&fexp=23842630&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRgIhAPD1xzFYPEKPwgASGHE0qLLzbuXYM4R--qPz2CkR3Y8TAiEAtohV9XS_-Dasqo1-y51hyAcQt35ex4LL7VhqmrmbaTY%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRgIhANFXXEDMrb2lA0XLwi9BPxaNQJ_mDqWwlIaVKqlw28yeAiEA_Ti6OM2AUecmTokDMZpw1DaCt7eE36dhAM7tsozkiek%3D&ratebypass=yes', 'nb_streams': 1, 'nb_programs': 0, 'format_name': 'matroska,webm', 'format_long_name': 'Matroska / WebM', 'start_time': '-0.007000', 'duration': '209.341000', 'size': '2884856', 'bit_rate': '110245', 'probe_score': 100, 'tags': {'encoder': 'google/video-file'}}}

tiempoMinutos = (float(datos['format']['duration'])/60)
print(tiempoMinutos)


input = ffmpeg.input(in_filename)

salida = ffmpeg.output(input, )


outinfo = "ffmpeg -i video.webm -ss 00:00:07.000 -vframes 1 thumb.jpg"
