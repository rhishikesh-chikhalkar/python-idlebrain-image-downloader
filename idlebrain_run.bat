@echo off
setlocal

REM Prompt the user to enter root_url
set /p ROOT_URL="Enter the URL link to download images: "

REM Activate the virtual environment
call "D:\UDEMY_Workspace\GITHUB\venv\Scripts\activate"

REM Change the current working directory to "C:\path\to\your\project"
cd /d "D:\UDEMY_Workspace\GITHUB\python-idlebrain-image-downloader"

REM Run the test.py script with the provided root_url parameter
python main.py %ROOT_URL%

REM Deactivate the virtual environment (optional)
call deactivate

endlocal