param(
    [string]$Name
)

if (-not $Name) {
    Write-Host "Использование: .\fix_images.ps1 <имя_папки>"
    exit 1
}

$IndexPath = "docs\$Name\index.md"

Write-Host "🔧 Исправляем пути к изображениям для: $Name"

if (-not (Test-Path $IndexPath)) {
    Write-Host "❌ Файл не найден: $IndexPath"
    exit 1
}

# Заменяем docs/ИмяПапки/media/ → media/
(Get-Content $IndexPath) -replace 'docs/' + $Name + '/media/', 'media/' | Set-Content $IndexPath

Write-Host "✅ Пути исправлены: $IndexPath"