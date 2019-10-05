# バイナリデータを読み込む場合の一時ファイル用
from tempfile import NamedTemporaryFile

from pydub import AudioSegment
import simpleaudio

class SoundPlayer:
    """SoundPlayer module."""

    @classmethod
    def play(cls, filename, audio_format="mp3", wait=False, stop=False):
        """Play audio file."""

        if stop:
            simpleaudio.stop_all()

        seg = AudioSegment.from_file(filename, audio_format)
        playback = simpleaudio.play_buffer(
            seg.raw_data,
            num_channels=seg.channels,
            bytes_per_sample=seg.sample_width,
            sample_rate=seg.frame_rate
        )

        if wait:
            playback.wait_done()

    @classmethod
    def play_from_buffer(cls, audio_content, audio_format="mp3", wait=False, stop=False):
        """Play from buffer."""
        with NamedTemporaryFile() as fd:
            fd.write(audio_content)
            # Revert head of file. It is neccesary to play audio.
            fd.seek(0)
            cls.play(fd.name, audio_format=audio_format, wait=wait, stop=stop)
