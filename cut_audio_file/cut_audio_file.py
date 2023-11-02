import moviepy.editor
from pathlib import Path

def cut_audio_file(video_file):
    """Вырезает аудиодорожку из видеофайла."""
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    try:
        audio.write_audiofile(f'{video_file.stem}.mp3')
        print(f'Ваша аудиодорожка - "{video_file.stem}.mp3" готова!')
    except:
        raise TypeError(f'Неверный формат файла - "{video_file}"!!!')
    
if __name__ == '__main__':
    video_file = Path('test_video.mp4')
    cut_audio_file(video_file)
