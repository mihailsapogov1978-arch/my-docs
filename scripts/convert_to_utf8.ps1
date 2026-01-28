# convert_to_utf8.ps1
Get-ChildItem "docs" -Recurse -Filter "*.md" | ForEach-Object {
    $filePath = $_.FullName
    Write-Host "Конвертируем: $filePath"
    
    # Читаем в CP1251 и записываем в UTF-8
    $content = Get-Content $filePath -Encoding Default
    Set-Content $filePath -Value $content -Encoding UTF8
}