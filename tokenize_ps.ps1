param([string]$InputFilePath)

$errors = $null
$code = Get-Content -Path $InputFilePath -Raw -Encoding Default
$tokens = [Management.Automation.PSParser]::Tokenize($code, [ref]$errors)

if ($errors.Count -gt 0)
{
  ConvertTo-Json -InputObject $errors
  $LASTEXITCODE = 1
}
else
{
  ConvertTo-Json -InputObject $tokens
  $LASTEXITCODE = 0
}