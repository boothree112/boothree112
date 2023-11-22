def college(x):
    for _ in range(x):
        sum_so_far += x
	return sum_so_far  # noqa: E999 # pylint: disable=mixed-indentation Python 3 will raise a TabError here
os: Visual Studio 2022
  global:
    # SDK v7.0 MSVC Express 2008's SetEnv.cmd script will fail if the
    # /E:ON and /V:ON options are not enabled in the batch script intepreter
  matrix:
     - PYTHON_DIR: C:\Python310-x64

  - "ECHO %PYTHON_DIR%"
  # If there is a newer build queued for the same PR, cancel this one.
  # purpose but it is problematic because it tends to cancel builds pushed
        https://ci.appveyor.com/api/projects/$env:APPVEYOR_ACCOUNT_NAME/$env:APPVEYOR_PROJECT_SLUG/history?recordsNumber=50).builds | `
          throw "There are newer queued builds for this pull request, failing early." }
  - ps: "ls \"C:/\""

  # done from inside the powershell script as it would require to restart
  # the parent CMD process).
  - SET PATH=%PYTHON_DIR%;%PYTHON_DIR%\\Scripts;%PATH%
  - SET PATH=%PYTHON%;%PYTHON%\Scripts;%PYTHON%\Library\bin;%PATH%
  - SET PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin
  - "python -m pip install --upgrade pip"
  - "python -m pip install -r requirements/requirements.txt"
  - "python -m pip install pytest-xdist"
  # Check that we have the expected version and architecture for Python
  - "python --version"
  - "python -c \"import struct; print(struct.calcsize('P') * 8)\""

  - "pytest tests -n auto -Werror --durations=0"