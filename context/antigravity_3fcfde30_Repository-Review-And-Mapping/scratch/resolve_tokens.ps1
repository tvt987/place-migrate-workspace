Add-Type -AssemblyName System.Reflection
$bytes = [System.IO.File]::ReadAllBytes('e:\Work\Place_Migrate\cci-store-location-web\01_origin\DLL.Web\Core.MVC.dll')
$asm = [System.Reflection.Assembly]::Load($bytes)
$mod = $asm.GetModules()[0]

$mPost = $asm.GetType('Core.MVC.APIClient').GetMethod('Post')
$mPostObj = $asm.GetType('Core.MVC.APIClient').GetMethod('PostObject')

# Token at offset 10 in Post is 0x2B000001 (MethodSpec)
# Let's resolve tokens
Write-Host "Post called method: $($mod.ResolveMethod(0x2B000001, $mPost.DeclaringType.GetGenericArguments(), $mPost.GetGenericArguments()).Name) in $($mod.ResolveMethod(0x2B000001, $mPost.DeclaringType.GetGenericArguments(), $mPost.GetGenericArguments()).DeclaringType.FullName)"
Write-Host "PostObject called method: $($mod.ResolveMethod(0x2B000002, $mPostObj.DeclaringType.GetGenericArguments(), $mPostObj.GetGenericArguments()).Name) in $($mod.ResolveMethod(0x2B000002, $mPostObj.DeclaringType.GetGenericArguments(), $mPostObj.GetGenericArguments()).DeclaringType.FullName)"

# And token at offset 15 is 0x0A000020
Write-Host "Token 0x0A000020: $($mod.ResolveMember(0x0A000020).Name) in $($mod.ResolveMember(0x0A000020).DeclaringType.FullName)"
