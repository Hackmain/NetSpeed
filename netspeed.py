import speedtest

def get_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024  # Convert to megabits per second
    upload_speed = st.upload() / 1024 / 1024

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    get_speed()
