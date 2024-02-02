import requests
from tqdm import tqdm
from pytube import YouTube

def download_video(url, resolution='720p', save_path='C:\\Users\\ASUS\\Desktop\\yourdownload'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the stream with the specified resolution
        video_stream = yt.streams.filter(res=f'{resolution}').first()

        # Create the save path if it doesn't exist
        import os
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Download the video with tqdm progress bar
        print(f'Downloading: {yt.title} ({resolution})')
        response = requests.get(video_stream.url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        with open(os.path.join(save_path, 'temp_video.mp4'), 'wb') as file, tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as bar:
            for data in response.iter_content(block_size):
                bar.update(len(data))
                file.write(data)
        print('\nDownload complete!')

    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    video_url = input("Enter Your Link: ")
    desired_resolution = input("Enter Your Resolution (e.g., 480, 720, 1080, 1440): ")
    xdesired_resolution = desired_resolution + "p"
    download_video(video_url, resolution=xdesired_resolution)
