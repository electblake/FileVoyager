#define MyAppName "FileVoyager"
#define MyAppId "FileVoyager.Desktop"
#define MyStageDir "..\build\installer"

[Setup]
AppId={#MyAppId}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
DefaultDirName={localappdata}\Programs\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
ArchitecturesAllowed=x64os
ArchitecturesInstallIn64BitMode=x64os
OutputDir=..\dist\installer
OutputBaseFilename=FileVoyager-Windows-x64-Setup-{#MyAppVersion}
UninstallDisplayIcon={app}\runtime\tools\python.exe
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
CloseApplications=yes
SetupLogging=yes
ArchiveExtraction=full

[Files]
Source: "https://api.nuget.org/v3-flatcontainer/python/3.12.10/python.3.12.10.nupkg"; DestDir: "{app}\runtime"; DestName: "python.zip"; ExternalSize: 39200793; Hash: "0eb85c2dfccccf1b17352de4c397f69194035b7d37149eacc16f1147d93de3b8"; Flags: external download extractarchive ignoreversion recursesubdirs createallsubdirs
Source: "{#MyStageDir}\bootstrap.pyz"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyStageDir}\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyStageDir}\app-wheel.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyStageDir}\filevoyager-{#MyAppVersion}-py3-none-any.whl"; DestDir: "{app}"; Flags: ignoreversion
Source: "OPEN-SOURCE-NOTICES.md"; DestDir: "{app}"; Flags: ignoreversion; AfterInstall: RunBootstrap('install')

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\runtime\tools\python.exe"; Parameters: "-I ""{app}\bootstrap.pyz"" run"; WorkingDir: "{app}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\runtime\tools\python.exe"; Parameters: "-I ""{app}\bootstrap.pyz"" run"; WorkingDir: "{app}"; Tasks: desktopicon

[Run]
Filename: "{app}\runtime\tools\python.exe"; Parameters: "-I ""{app}\bootstrap.pyz"" run"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent; Check: BootstrapSucceeded

[UninstallDelete]
Type: filesandordirs; Name: "{app}\runtime"

[Code]
var
  BootstrapExitCode: Integer;

procedure RunBootstrap(const Action: String);
begin
  if not ExecAndLogOutput(ExpandConstant('{app}\runtime\tools\python.exe'),
    '-I "' + ExpandConstant('{app}\bootstrap.pyz') + '" ' + Action,
    ExpandConstant('{app}'), SW_SHOWNORMAL, ewWaitUntilTerminated, BootstrapExitCode, nil) then
    RaiseException(SysErrorMessage(BootstrapExitCode));
  if BootstrapExitCode <> 0 then
    RaiseException(Format('FileVoyager %s exited with code %d. See the setup log for the original output.', [Action, BootstrapExitCode]));
end;

function BootstrapSucceeded: Boolean;
begin
  Result := BootstrapExitCode = 0;
end;

function GetCustomSetupExitCode: Integer;
begin
  Result := BootstrapExitCode;
end;

procedure CurPageChanged(CurPageID: Integer);
begin
  if (CurPageID = wpFinished) and (BootstrapExitCode <> 0) then
  begin
    WizardForm.FinishedHeadingLabel.Caption := 'FileVoyager installation failed';
    WizardForm.FinishedLabel.Caption := 'The application environment could not be installed. See the setup log for details. You can remove the incomplete installation using the uninstaller.';
  end;
end;

function InitializeUninstall: Boolean;
begin
  RunBootstrap('uninstall');
  Result := True;
end;
