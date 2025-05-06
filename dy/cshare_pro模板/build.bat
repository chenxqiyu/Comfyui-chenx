@echo off

REM 编译C#文件
dotnet build "demo.csproj" -o "bin\Debug\net6.0"

if %ERRORLEVEL% equ 0 (
    echo 编译成功，生成文件: demo.exe
) else (
    echo 编译失败
)

pause