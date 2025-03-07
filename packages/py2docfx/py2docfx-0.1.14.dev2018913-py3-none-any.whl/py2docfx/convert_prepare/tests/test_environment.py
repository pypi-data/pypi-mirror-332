import os
import shutil
import pytest

from py2docfx.convert_prepare.environment import create_environment, install_required_packages
from py2docfx.convert_prepare.environment import remove_environment
from py2docfx.convert_prepare.environment import get_venv_path
from py2docfx.convert_prepare.environment import get_venv_exe
from py2docfx.convert_prepare.environment import install_venv_requirements
from py2docfx.convert_prepare.environment import VENV_REQUIREMENT_MODULES
from py2docfx.convert_prepare.environment import prepare_base_venv
from py2docfx.convert_prepare.environment import get_base_venv_exe
from py2docfx.convert_prepare.environment import get_base_venv_path
from py2docfx.convert_prepare.package_info import PackageInfo

@pytest.mark.asyncio
async def test_venv_creation_package_install_remove():
    # Test creating a venv
    venv_path = get_venv_path(0)
    await create_environment(venv_path)
    interpreter = get_venv_exe(0)
    assert os.path.exists(interpreter)

    # Test installing requirements
    await install_venv_requirements(0)
    # check if the requirements are installed in the venv
    for module in VENV_REQUIREMENT_MODULES:
        assert os.system(f"{interpreter} -m pip show {module}") == 0

    # Test removing the venv
    await remove_environment(0)
    assert not os.path.exists(interpreter)

@pytest.mark.asyncio
async def test_prepare_base_venv():
    await prepare_base_venv([], "", "")
    interpreter = get_base_venv_exe()
    assert os.path.exists(interpreter)
    # check if the requirements are installed in the venv
    requrirements = ["setuptools", "sphinx", "pyyaml", "jinja2", "wheel"]
    for module in requrirements:
        assert os.system(f"{interpreter} -m pip show {module}") == 0

    # remove base venv
    base_venv_path = get_base_venv_path()
    shutil.rmtree(base_venv_path)

@pytest.mark.asyncio
async def test_install_required_packages_pypi():
    required_package_info = PackageInfo()
    required_package_info.install_type = PackageInfo.InstallType.PYPI
    required_package_info.name = "azure-core"

    await prepare_base_venv([], "", "")
    interpreter = get_base_venv_exe()
    await install_required_packages(interpreter, [required_package_info], None, None)
    
    assert os.system(f"{interpreter} -m pip show {required_package_info.name}") == 0

@pytest.mark.asyncio
async def test_install_required_packages_source_code():
    required_package_info = PackageInfo()
    required_package_info.install_type = PackageInfo.InstallType.SOURCE_CODE
    required_package_info.name = "botbuilder-schema"
    required_package_info.url = "https://github.com/microsoft/botbuilder-python"
    required_package_info.branch = "releases/4.14"
    required_package_info.folder = "./libraries/botbuilder-schema"

    await prepare_base_venv([], "", "")
    interpreter = get_base_venv_exe()
    await install_required_packages(interpreter, [required_package_info], None, None)
    
    assert os.system(f"{interpreter} -m pip show {required_package_info.name}") == 0

@pytest.mark.asyncio
async def test_install_required_packages_dist_file():
    required_package_info = PackageInfo()
    required_package_info.install_type = PackageInfo.InstallType.DIST_FILE
    required_package_info.name = "py4j"
    required_package_info.location = "https://files.pythonhosted.org/packages/e3/53/c737818eb9a7dc32a7cd4f1396e787bd94200c3997c72c1dbe028587bd76/py4j-0.10.7-py2.py3-none-any.whl"

    await prepare_base_venv([], "", "")
    interpreter = get_base_venv_exe()
    await install_required_packages(interpreter, [required_package_info], None, None)
    
    assert os.system(f"{interpreter} -m pip show {required_package_info.name}") == 0