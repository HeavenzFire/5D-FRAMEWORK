ot load commands from the current location by default. If you trust this command, instead type: ".\git". See "get-help about_Command_Precedence" for more details.
PS C:\Users\rucke>
PS C:\Users\rucke> # Commit the changes
PS C:\Users\rucke> git commit -m "Initial commit for Spirit Angelus project"
git : The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ git commit -m "Initial commit for Spirit Angelus project"
+ ~~~
    + CategoryInfo          : ObjectNotFound: (git:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command git was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\git". See "get-help about_Command_Precedence" for more details.
PS C:\Users\rucke>
PS C:\Users\rucke> # Connect to GitHub repository
PS C:\Users\rucke> git remote add origin <YOUR_GITHUB_REPO_URL>
At line:1 char:23
+ git remote add origin <YOUR_GITHUB_REPO_URL>
+                       ~
The '<' operator is reserved for future use.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : RedirectionNotSupported

PS C:\Users\rucke>
PS C:\Users\rucke> # Push to GitHub
PS C:\Users\rucke> git push -u origin master
git : The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ git push -u origin master
+ ~~~
    + CategoryInfo          : ObjectNotFound: (git:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command git was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\git". See "get-help about_Command_Precedence" for more details.
PS C:\Users\rucke> Instructions:
Instructions: : The term 'Instructions:' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Instructions:
+ ~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Instructions::String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke> Save the Script:
Save : The term 'Save' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Save the Script:
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (Save:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke>
PS C:\Users\rucke> Save the above code in a file named setup_spirit_angelus.sh.
Save : The term 'Save' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Save the above code in a file named setup_spirit_angelus.sh.
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (Save:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke>
PS C:\Users\rucke> Make the Script Executable:
Make : The term 'Make' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Make the Script Executable:
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (Make:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke>
PS C:\Users\rucke> sh
sh : The term 'sh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ sh
+ ~~
    + CategoryInfo          : ObjectNotFound: (sh:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke>
PS C:\Users\rucke> Copy

cmdlet Copy-Item at command pipeline position 1
Supply values for the following parameters:
Path[0]:
Copy-Item : Cannot bind argument to parameter 'Path' because it is an empty array.
At line:1 char:1
+ Copy
+ ~~~~
    + CategoryInfo          : InvalidData: (:) [Copy-Item], ParameterBindingValidationException
    + FullyQualifiedErrorId : ParameterArgumentValidationErrorEmptyArrayNotAllowed,Microsoft.PowerShell.Commands.CopyI
   temCommand

PS C:\Users\rucke> chmod +x setup_spirit_angelus.sh
chmod : The term 'chmod' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ chmod +x setup_spirit_angelus.sh
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (chmod:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command chmod was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\chmod". See "get-help about_Command_Precedence" for more details.
PS C:\Users\rucke> Run the Script:
Run : The term 'Run' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Run the Script:
+ ~~~
    + CategoryInfo          : ObjectNotFound: (Run:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke>
PS C:\Users\rucke> sh
sh : The term 'sh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ sh
+ ~~
    + CategoryInfo          : ObjectNotFound: (sh:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\rucke>
PS C:\Users\rucke> Copy

cmdlet Copy-Item at command pipeline position 1
Supply values for the following parameters:
Path[0]:
