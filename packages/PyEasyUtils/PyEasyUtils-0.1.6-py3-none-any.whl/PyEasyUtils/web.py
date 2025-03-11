import os
import platform
import hashlib
import urllib
import requests
import json
from tqdm import tqdm
from packaging import version
from github import Github
from pathlib import Path
from enum import Enum
from typing import Union, Optional, Tuple

from .utils import toIterable
from .path import normPath
from .cmd import runCMD

#############################################################################################################

def isConnected(
    host: str,
    port: int,
):
    """
    Check connection
    """
    try:
        response = requests.get(
            url = f"http://{host}:{port}/"
        )
        return True
    except Exception as e:
        print(e)
        return False


class requestManager(Enum):
    """
    Manage request
    """
    Post = 0
    Get = 1

    def createResponse(self,
        host: str,
        port: str,
        pathParams: Union[str, list[str], None] = None,
        queryParams: Union[str, list[str], None] = None,
        headers: Optional[dict] = None,
        data: Union[dict, json.JSONEncoder, None] = None,
    ):
        if self == self.Post:
            reqMethod = requests.post
        if self == self.Get:
            reqMethod = requests.get
        pathParams = "/".join(toIterable(pathParams) if pathParams else [])
        queryParams = "&".join(toIterable(queryParams) if queryParams else [])
        self.response = reqMethod(
            url = f"http://{host}:{port}"
            + (f"/{pathParams}" if len(pathParams) > 0 else "")
            + (f"?{queryParams}" if len(queryParams) > 0 else ""),
            headers = headers,
            data = data if isinstance(data, json.JSONDecoder) else (json.dumps(data) if data is not None else None)
        )
        return self.response


def simpleRequest(
    reqMethod: requestManager,
    host: str,
    port: str,
    pathParams: Union[str, list[str], None] = None,
    queryParams: Union[str, list[str], None] = None,
    headers: Optional[dict] = None,
    data: Union[dict, json.JSONEncoder, None] = None,
    *keys
):
    if not isConnected(host, port):
        return

    response = reqMethod.createResponse(host, port, pathParams, queryParams, headers, data)
    if response.status_code == 200:
        encodedResponse = response.json()
        result = (encodedResponse.get(key, {}) for key in keys) if keys else encodedResponse
        return result

#############################################################################################################

def _download(
    downloadURL: str,
    downloadPath: str,
):
    with urllib.request.urlopen(downloadURL) as source, open(downloadPath, mode = "wb") as output:
        totalLength = int(source.info().get("content-Length"))
        while True:
            buffer = source.read(8192)
            if not buffer:
                break
            output.write(buffer)
            yield len(buffer), totalLength


def _download_aria(
    downloadURL: str,
    downloadPath: str,
    createNewConsole: bool = False
):
    runCMD(
        args = [
            'aria2c',
            f'''
            {('cmd.exe /c start ' if platform.system() == 'Windows' else 'x-terminal-emulator -e ') if createNewConsole else ''}
            aria2c "{downloadURL}" --dir="{Path(downloadPath).parent.as_posix()}" --out="{Path(downloadPath).name}" -x6 -s6 --file-allocation=none --force-save=false
            '''
        ]
    )


def downloadFile(
    downloadURL: str,
    downloadDir: str,
    fileName: str,
    fileFormat: str,
    sha: Optional[str],
    createNewConsole: bool = False
) -> Tuple[Union[bytes, str], str]:
    """
    Downloads a file from a given URL and saves it to a specified directory
    """
    fileBytes = None
    isDownloadNeeded = True

    downloadName = fileName + (fileFormat if '.' in fileFormat else f'.{fileFormat}')
    downloadPath = normPath(Path(downloadDir).joinpath(downloadName).absolute())

    if Path(downloadPath).exists():
        if Path(downloadPath).is_file() and sha is not None:
            with open(downloadPath, mode = "rb") as f:
                fileBytes = f.read()
            if len(sha) == 40:
                SHA_Current = hashlib.sha1(fileBytes).hexdigest()
            if len(sha) == 64:
                SHA_Current = hashlib.sha256(fileBytes).hexdigest()
            isDownloadNeeded = True if SHA_Current != sha else False
        else:
            os.remove(downloadPath)
            os.makedirs(downloadDir, exist_ok = True)

    if isDownloadNeeded:
        try:
            _download_aria(downloadURL, downloadPath, createNewConsole)
        except:
            iter(_download(downloadURL, downloadPath))
        finally:
            fileBytes = open(downloadPath, mode = "rb").read() if Path(downloadPath).exists() else None

    if fileBytes is None:
        raise Exception('Download Failed!')

    return fileBytes, downloadPath

#############################################################################################################

def checkUpdateFromGithub(
    repoOwner: str = ...,
    repoName: str = ...,
    fileName: str = ...,
    fileFormat: str = ...,
    currentVersion: str = ...,
    accessToken: Optional[str] = None,
):
    """
    Check if there is an update available on Github
    """
    try:
        PersonalGit = Github(accessToken)
        Repo = PersonalGit.get_repo(f"{repoOwner}/{repoName}")
        latestVersion = Repo.get_tags()[0].name
        latestRelease = Repo.get_latest_release() #latestRelease = Repo.get_release(latestVersion)
        for Index, Asset in enumerate(latestRelease.assets):
            if Asset.name == f"{fileName}.{fileFormat}":
                IsUpdateNeeded = True if version.parse(currentVersion) < version.parse(latestVersion) else False
                downloadURL = Asset.browser_download_url #downloadURL = f"https://github.com/{repoOwner}/{repoName}/releases/download/{latestVersion}/{fileName}.{fileFormat}"
                VersionInfo = latestRelease.body
                return IsUpdateNeeded, downloadURL, VersionInfo
            elif Index + 1 == len(latestRelease.assets):
                raise Exception(f"No file found with name {fileName}.{fileFormat} in the latest release")

    except Exception as e:
        print(f"Error occurred while checking for updates: \n{e}")

#############################################################################################################