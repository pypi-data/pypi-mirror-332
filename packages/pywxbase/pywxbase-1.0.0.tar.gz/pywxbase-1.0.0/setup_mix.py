import os
import glob
import platform
import re
import py_compile
import shutil
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

root_dir = os.path.abspath(os.path.dirname(__file__))
package_dir = os.path.join(root_dir, "pywxbase")

def remove_existing_files(root_dir):
    """删除已有的 .pyc, .pyi 文件，防止编译出错"""
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith((".pyc", ".pyi")):
                os.remove(os.path.join(root, file))
                print(f"Removed: {file}")

remove_existing_files(package_dir)

py_files = [
    f for f in glob.glob("pywxbase/**/*.py", recursive=True)
    if f not in {"pywxbase/__init__.py"}
]

def extract_stub_info(py_file):
    """自动生成 .pyi 类型提示"""
    with open(py_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.readlines()

    stub = "# Stub file for type hints\n\n"
    imports, class_methods, constants, functions = [], {}, [], {}
    current_class = None

    for line in content:
        stripped = line.strip()

        if stripped.startswith(("import ", "from ")):
            imports.append(stripped)

        class_match = re.match(r"^class (\w+)", stripped)
        if class_match:
            current_class = class_match.group(1)
            class_methods[current_class] = []
            continue

        # 识别方法定义（确保是类内部的）
        # if current_class and re.match(r"^def (\w+)", stripped):
        #     method_name = re.match(r"^def (\w+)", stripped).group(1)
        #     class_methods[current_class].append(method_name)
        #     continue
        if current_class and stripped.startswith("def "):
            # 通过检查前一行是否为 @staticmethod 装饰器来标记静态方法
            is_static_method = False
            if len(content) > content.index(line) - 1 and "@staticmethod" in content[content.index(line) - 1]:
                is_static_method = True

            method_name = re.match(r"^def (\w+)", stripped).group(1)

            if is_static_method:
                # 静态方法：加上 @staticmethod 并移除 self 或 cls 参数
                method_signature = f"    @staticmethod\n    def {method_name}(*args, **kwargs): ..."
            else:
                # 普通方法：包含 self 参数
                method_signature = f"    def {method_name}(self, *args, **kwargs): ..."

            class_methods[current_class].append(method_signature)
            continue

        func_match = re.match(r"^def (\w+)\((.*?)\)\s*(->\s*\w+)?\:", stripped)
        if func_match:
            func_name, func_signature, return_type = func_match.groups()
            functions[func_name] = f"({func_signature}){return_type or ''}"

        variable_match = re.match(r"^(\w+):\s*(\w+)\s*=\s*(.*)", stripped)
        if variable_match:
            constant_name, constant_type = variable_match.groups()[:2]
            constants.append(f"{constant_name}: {constant_type}")

    if imports:
        stub += "\n".join(imports) + "\n\n"

    for constant in constants:
        stub += f"{constant}: ...\n"

    for func_name, func_signature in functions.items():
        stub += f"def {func_name}{func_signature}: ...\n"

    # for class_name, methods in class_methods.items():
    #     stub += f"class {class_name}:\n"
    #     for method in methods:
    #         stub += f"    def {method}(self, *args, **kwargs): ...\n"
    #     stub += "\n"

    for class_name, methods in class_methods.items():
        stub += f"class {class_name}:\n"
        for method in methods:
            stub += f"{method}\n"
        stub += "\n"

    return stub

def create_stub_files():
    """为所有模块创建 .pyi 文件"""
    for py_file in py_files:
        stub_file = py_file.replace(".py", ".pyi")
        stub_dir = os.path.dirname(stub_file)
        if not os.path.exists(stub_dir):
            os.makedirs(stub_dir)
        print(f"Creating stub: {stub_file}")
        with open(stub_file, "w", encoding="utf-8") as f:
            f.write(extract_stub_info(py_file))

create_stub_files()

def compile_all_py_to_pyc(root_dir):
    """编译 .py 文件为 .pyc"""
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                py_path = os.path.join(root, file)
                pyc_path = py_path + "c"
                py_compile.compile(py_path, cfile=pyc_path)
                print(f"Compiled: {py_path} -> {pyc_path}")

compile_all_py_to_pyc(package_dir)

class CustomBuild(build_py):
    """只打包 .pyc 和 .pyi，不打包 .py"""
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for pkg, mod, file in modules:
            if file.endswith(".py"):
                pyc_file = f"{file}c"
                if os.path.exists(os.path.join(package_dir, pyc_file)):
                    filtered_modules.append((pkg, mod, pyc_file))
        return filtered_modules

system_name = platform.system().lower()
package_name = "pywxbase"
version = "1.0.0"
dist_name = f"{package_name}-{version}-{system_name}"

setup(
    name=package_name,
    version=version,
    author="wx",
    description="pywxbase",
    long_description="pywxbase",
    packages=find_packages(),
    cmdclass={"build_py": CustomBuild},
    zip_safe=False,
    include_package_data=True,
    package_data={
        "pywxbase": ["**/*.pyc", "**/*.pyi"],
    },
    exclude_package_data={"pywxbase": ["*.py"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities",
    ],
)

remove_existing_files(package_dir)

#classifiers
# 1. 开发状态 (Development Status)
# 这些分类器描述项目的开发阶段，帮助用户了解项目的成熟度。
# Development Status :: 1 - Planning
# 项目处于规划阶段，尚未开始开发。
# Development Status :: 2 - Pre-Alpha
# 项目处于早期开发阶段，功能不完整，可能不稳定。
# Development Status :: 3 - Alpha
# 项目处于 Alpha 阶段，功能基本实现，但可能存在较多 Bug。
# Development Status :: 4 - Beta
# 项目处于 Beta 阶段，功能基本稳定，但仍需测试和优化。
# Development Status :: 5 - Production/Stable
# 项目已经稳定，适合生产环境使用。
# Development Status :: 6 - Mature
# 项目非常成熟，已经经过长时间的生产环境考验。
# Development Status :: 7 - Inactive
# 项目不再维护或开发。

# 2. 目标受众 (Intended Audience)
# 这些分类器描述项目的目标用户群体。
# Intended Audience :: Developers
# 项目面向开发人员。
# Intended Audience :: End Users/Desktop
# 项目面向普通用户或桌面应用程序用户。
# Intended Audience :: Science/Research
# 项目面向科学研究人员。
# Intended Audience :: System Administrators
# 项目面向系统管理员。
# Intended Audience :: Education
# 项目面向教育领域。

# 3. 许可证 (License)
# 这些分类器描述项目的许可证类型。
# License :: OSI Approved :: MIT License
# 项目使用 MIT 许可证。
# License :: OSI Approved :: Apache Software License
# 项目使用 Apache 2.0 许可证。
# License :: OSI Approved :: GNU General Public License v3 (GPLv3)
# 项目使用 GPLv3 许可证。
# License :: OSI Approved :: BSD License
# 项目使用 BSD 许可证。
# License :: Public Domain
# 项目属于公共领域。

# 1. 常见许可证类型
# 1.1 MIT 许可证
# 特点：
# 非常宽松的许可证。
# 允许他人自由使用、修改、分发代码，甚至可以用于商业用途。
# 唯一的要求是保留原始许可证声明和版权声明。
# 风险：
# 代码可能被他人用于闭源项目，且你无法控制其后续分发。
# 如果代码被滥用，你可能无法追究责任。
# 适用场景：
# 适合希望代码被广泛使用的开源项目。
#
# 1.2 Apache 2.0 许可证
# 特点：
# 允许他人自由使用、修改、分发代码，包括商业用途。
# 要求保留原始许可证声明和版权声明。
# 提供专利授权，保护用户免受专利诉讼。
# 如果修改代码，必须明确说明修改内容。
# 风险：
# 比 MIT 许可证更复杂，需要遵守更多的条款。
# 适用场景：
# 适合涉及专利保护的开源项目。
#
# 1.3 GNU General Public License (GPL)
# 特点：
# 强 Copyleft 许可证。
# 允许他人自由使用、修改、分发代码。
# 如果他人分发基于 GPL 代码的衍生作品，也必须以 GPL 许可证开源。
# 风险：
# 限制了代码的闭源使用，可能影响商业应用。
# 如果项目中包含 GPL 代码，整个项目可能都需要以 GPL 开源。
# 适用场景：
# 适合希望强制开源的社区项目。
#
# 1.4 GNU Lesser General Public License (LGPL)
# 特点：
# 弱 Copyleft 许可证。
# 允许他人自由使用、修改、分发代码。
# 如果他人仅使用 LGPL 代码作为库，而不修改它，可以闭源。
# 如果修改 LGPL 代码，则必须以 LGPL 开源。
# 风险：
# 比 GPL 更灵活，但仍有一定的限制。
# 适用场景：
# 适合希望作为库被广泛使用的开源项目。
#
# 1.5 BSD 许可证
# 特点：
# 类似于 MIT 许可证，非常宽松。
# 允许他人自由使用、修改、分发代码，包括商业用途。
# 要求保留原始许可证声明和版权声明。
# 风险：
# 代码可能被他人用于闭源项目。
# 适用场景：
# 适合希望代码被广泛使用的开源项目。
#
# 1.6 Mozilla Public License 2.0 (MPL 2.0)
# 特点：
# 介于宽松许可证和 Copyleft 许可证之间。
# 允许他人自由使用、修改、分发代码。
# 如果修改 MPL 代码，则必须以 MPL 开源。
# 允许将 MPL 代码与闭源代码结合。
# 风险：
# 比 MIT 和 Apache 2.0 更复杂。
# 适用场景：
# 适合希望部分开源的商业项目。
#
# 1.7 Creative Commons (CC)
# 特点：
# 主要用于非代码内容（如文档、图像、音乐等）。
# 有多种变体，如 CC BY（署名）、CC BY-SA（署名-相同方式共享）等。
# 风险：
# 不适用于软件代码。
# 适用场景：
# 适合非代码内容的开源项目。


# 4. 编程语言 (Programming Language)
# 这些分类器描述项目使用的编程语言及其版本。
# Programming Language :: Python
# 项目使用 Python 编写。
# Programming Language :: Python :: 3
# 项目兼容 Python 3。
# Programming Language :: Python :: 3.7
# 项目兼容 Python 3.7。
# Programming Language :: Python :: 3.8
# 项目兼容 Python 3.8。
# Programming Language :: Python :: 3.9
# 项目兼容 Python 3.9。
# Programming Language :: Python :: 3.10
# 项目兼容 Python 3.10。
# Programming Language :: Python :: 3.11
# 项目兼容 Python 3.11。


# 5. 操作系统 (Operating System)
# 这些分类器描述项目支持的操作系统。
# Operating System :: OS Independent
# 项目与操作系统无关，可以在任何操作系统上运行。
# Operating System :: Microsoft :: Windows
# 项目支持 Windows 操作系统。
# Operating System :: POSIX :: Linux
# 项目支持 Linux 操作系统。
# Operating System :: MacOS :: MacOS X
# 项目支持 macOS 操作系统。
# Operating System :: Unix
# 项目支持 Unix 操作系统。


# 6. 框架 (Framework)
# 这些分类器描述项目使用的框架或库。
# Framework :: Django
# 项目基于 Django 框架。
# Framework :: Flask
# 项目基于 Flask 框架。
# Framework :: Pytest
# 项目与 Pytest 测试框架相关。
# Framework :: Jupyter
# 项目与 Jupyter 相关。


# 7. 主题 (Topic)
# 这些分类器描述项目的主题或用途。
# Topic :: Software Development
# 项目与软件开发相关。
# Topic :: Scientific/Engineering
# 项目与科学或工程相关。
# Topic :: Internet :: WWW/HTTP
# 项目与 Web 开发相关。
# Topic :: Utilities
# 项目是一个实用工具。
# Topic :: Education
# 项目与教育相关。

# 8. 其他分类器
# Environment :: Console
# 项目是一个命令行工具。
# Environment :: Web Environment
# 项目是一个 Web 应用程序。
# Natural Language :: English
# 项目的文档或代码使用英语。
# Typing :: Typed
# 项目包含类型注解（Type Hints）。

