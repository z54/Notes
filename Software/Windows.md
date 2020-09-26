# Windows

## version

### Windows 10

- Windows 10家庭版（Windows 10 Home）
- Windows 10专业版（Windows 10 Pro）
- Windows 10企业版（Windows 10 Enterprise）
- Windows 10教育版（Windows 10 Education）
- Windows 10移动版（Windows 10 Mobile）
- Windows 10企业移动版（Windows 10 Mobile Enterprise）
- Windows 10 IoT Core（主要针对物联网设备）

---

- vl 
    `cn_windows_10_multi-edition_vl_version_1709_updated_sept_2017_x64_dvd_100090774.iso`

    里面包含三个SKU，分别是教育、企业、专业

    `cn_windows_10_multi-edition_version_1709_updated_sept_2017_x64_dvd_100090804.iso`

    不带vl的，我下载了没有全新安装过
    里面包含5个版本，分别是s、家庭、家庭单语言、教育、专业

- Windows10 1803 iso版本差异

    - Consumer editions包括：家庭版、家庭单语言版、教育版、专业版、专业教育版、专业工作站版（相当于之前的零售版）；
    - Business editions包括：企业版、教育版、专业版（相当于之前的VL版）

[Win10系统有几个版本？Windows10各版本区别详细介绍_windows10_Windows系列_操作系统_脚本之家](https://www.jb51.net/os/win10/325827.html)

## Fatal

### 内存错误，蓝屏

1. start up the software `Windows Memory problem`
2. click the choice `Restart now and check for problems`
3. then PC will restart and enter to scanning mode, wait
4. computer will restart and product a Memory Diagnostics Report
    1. run `eventvwr`
    2. `Event Viewer (local)` - `Windows Logs` - `System`
    3. `filter current log`
    4. `Event Sources`: `MemoryDiagnostics-Results`