function Show-Menu 
{ 
     param ([string]$Titulo = 'Opciones del Menu') 
     cls 
     Write-Host "================ $Titulo================" 
     Write-Host "1) Imprimir la cadena" 
     Write-Host "2) Contar los elementos de la cadena" 
     Write-Host "3) Convertir la cadena en mayúsculas" 
     Write-Host "4) Convertir la cadena en minúsculas"
     Write-Host "5) Sustituir frases de la cadena"
     Write-Host "Salir) Presiona '0' para salir" 
}cls

function Print-String 
{ 
     Write-Host "$string"
     
}cls

function Length-String 
{ 
     Write-Host $string.Length
     
}cls

function Upper-String 
{ 
     Write-Host $string.ToUpper()
     
}cls

function Lower-String 
{ 
     Write-Host $string.ToLower()
     
}cls

function Replace-String 
{ 
     $word1 = Read-Host "Por favor ingresa la palabra a cambiar en tu cadena"
     $word2 = Read-Host "Por favor ingresa la palabra que vas a cambiar en tu cadena"
     Write-Host $string.Replace("$word1", "$word2")
     
}cls


$string = Read-Host "Por favor ingresa una cadena de texto"

do
{    
    Show-Menu 
    $input = Read-Host "Elegir una Opción " 
    switch ($input) 
    {
        '1' { 
            cls
            Print-String
            
        } '2' { 
            cls
            Length-String 

        } '3' { 
            cls
            Upper-String        
        } '4' {
            cls
            Lower-String
        } '5' {
            cls
            Replace-String
        } '0' { 
            return 
        }  
    } 
    pause 
}
until ($input -eq '0')