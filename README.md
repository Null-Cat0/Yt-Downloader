
# Yt-Downloader

## Description

Yt-Downloader is a command-line tool designed to simplify the process of downloading videos from YouTube. This program utilizes the `yt-dlp` library for handling video downloads and incorporates Flask for a web interface, allowing users to download videos directly through a web browser.

## Dependencies

To ensure the proper functioning of Yt-Downloader, you need to install the following Python dependencies:

- **colorama**: This library is used to enable colored text output in the terminal, enhancing readability and presentation.

    ```bash
    python -m pip install colorama
    ```

- **yt-dlp**: This library is used to manage video downloads from YouTube. `yt-dlp` is a fork of `youtube-dl` that addresses issues related to recent changes in YouTube’s API.

    ```bash
    python -m pip install yt-dlp
    ```

- **Flask**: This micro web framework is used to create a web interface for Yt-Downloader.

    ```bash
    python -m pip install flask
    ```
- **pytubefix**: This library is used for handling YouTube video downloads and is a modified version of `pytube` that fixes issues related to changes in YouTube’s API.

    ```bash
    python -m pip install pytubefix
    ```
