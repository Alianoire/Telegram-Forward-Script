# Introduction
A simple script to automatically forward messages on Telegram, filtered according to their content. Developed in Python using the Telethon library.

# Requirements
The requirements for using the script are as follows:
* Python installed on your system;
* Telethon library;
* ID and Hash to work with Telehram's API.

Once Python is installed, use the following commands to install or upgrade library and pip to the latest version:
```shell
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade telethon
```

To verify that the library is installed correctly, run the following command:
```shell
python3 -c "import telethon; print(telethon.__version__)"
```
The version number of the library should show in the output.

Before working with Telegram’s API, you need to get your own API ID and hash:
1. [Login to your Telegram account](https://my.telegram.org/) with the phone number of the developer account to use.
2. Click under API Development tools.
3. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
4. Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!

# Links
* [Telethon Github](https://github.com/LonamiWebs/Telethon)
* [Telethon Documentation](https://docs.telethon.dev/en/stable/)
* [Python](https://www.python.org/)
