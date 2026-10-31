<!--
source: https://github.com/enthought/comtypes/blob/main/pyproject.toml
retrieved: 2026-10-31T21:19:14.936595+00:00
final_url: https://github.com/enthought/comtypes/blob/main/pyproject.toml
content_type: text/html
-->

# comtypes/pyproject.toml at main · enthought/comtypes · GitHub

[Skip to content](https://github.com/enthought/comtypes/blob/main/pyproject.toml#start-of-content)

## Navigation Menu

[https://github.com/](https://github.com/)

[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fenthought%2Fcomtypes%2Fblob%2Fmain%2Fpyproject.toml)

Search /

[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fenthought%2Fcomtypes%2Fblob%2Fmain%2Fpyproject.toml)

[Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&source=header-repo&source_repo=enthought%2Fcomtypes)

Appearance settings

You signed in with another tab or window. Reload  to refresh your session. You signed out in another tab or window. Reload  to refresh your session. You switched accounts on another tab or window. Reload  to refresh your session. Dismiss alert

{{ message }}

## Repository navigation

[https://github.com/enthought/comtypes](https://github.com/enthought/comtypes)

## Files Expand file tree

main

/

# pyproject.toml

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/enthought/comtypes/commits/main/pyproject.toml)

[https://github.com/enthought/comtypes/commits/main/pyproject.toml](https://github.com/enthought/comtypes/commits/main/pyproject.toml) History

106 lines (96 loc) · 3.13 KB

main

/

# pyproject.toml

Copy path

Top

## File metadata and controls

- 

Code

- 

Blame

106 lines (96 loc) · 3.13 KB

[Raw](https://github.com/enthought/comtypes/raw/refs/heads/main/pyproject.toml)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

[project ]

name  = " comtypes "

description  = " Pure Python COM package "

readme  = " README.md "

requires-python  = " >=3.9 "

license  = " MIT "

license-files  = [" LICENSE.txt " ]

authors  = [

 { name  = " Thomas Heller " , email  = " theller@python.net "  },

]

classifiers  = [

" Development Status :: 5 - Production/Stable " ,

" Intended Audience :: Developers " ,

" Operating System :: Microsoft :: Windows " ,

" Programming Language :: Python " ,

" Programming Language :: Python :: 3 " ,

" Topic :: Software Development :: Libraries :: Python Modules " ,

]

dynamic  = [" version " ]

[project . scripts ]

clear_comtypes_cache  = " comtypes.clear_cache:main "

[project . urls ]

Source  = " https://github.com/enthought/comtypes "

Download  = " https://github.com/enthought/comtypes/releases "

Issues  = " https://github.com/enthought/comtypes/issues "

[build-system ]

requires  = [" setuptools>=77.0.0 " ]

build-backend  = " setuptools.build_meta "

[tool . setuptools ]

packages  = [

" comtypes " ,

" comtypes._post_coinit " ,

" comtypes.client " ,

" comtypes.server " ,

" comtypes.tools " ,

" comtypes.tools.codegenerator " ,

" comtypes.test " ,

]

[tool . setuptools . dynamic ]

version  = { attr  = " comtypes.__version__ "  }

[tool . setuptools . package-data ]

"comtypes.test"  = [

" TestComServer.idl " ,

" TestComServer.tlb " ,

" TestDispServer.idl " ,

" TestDispServer.tlb " ,

" mytypelib.idl " ,

" mylib.idl " ,

" mylib.tlb " ,

" urlhist.tlb " ,

" test_jscript.js " ,

]

"comtypes"  = [" hints.pyi " , " py.typed " ]

[tool . ruff . lint ]

extend-select  = [" I " ]

ignore  = [" E402 " ]

[tool . ruff . lint . per-file-ignores ]

#  production

"comtypes/_npsupport.py"  = [" F401 " ]

"comtypes/_vtbl.py"  = [" E722 " ]

"comtypes/automation.py"  = [" F401 " , " F403 " , " F405 " ]

"comtypes/viewobject.py"  = [" F403 " , " F405 " ]

"comtypes/client/_constants.py"  = [" F401 " ]

"comtypes/server/automation.py"  = [" F403 " , " F405 " ]

"comtypes/server/connectionpoints.py"  = [" F401 " , " F403 " , " F405 " ]

"comtypes/server/inprocserver.py"  = [" E722 " ]

"comtypes/server/register.py"  = [" E713 " ]

"comtypes/tools/codegenerator/packing.py"  = [" F821 " , " F841 " ]

#  gen directory

"comtypes/gen/*"  = [" E " , " F " , " I " ]

#  stub

"comtypes/hints.pyi"  = [" I " ]

#  tests

"comtypes/test/TestDispServer.py"  = [" E401 " ]

"comtypes/test/find_memleak.py"  = [" E401 " , " F401 " , " F403 " , " F405 " ]

"comtypes/test/setup.py"  = [" F401 " ]

"comtypes/test/test_agilent.py"  = [" F401 " , " F841 " ]

"comtypes/test/test_client.py"  = [" F401 " ]

"comtypes/test/test_dict.py"  = [" F841 " ]

"comtypes/test/test_eventinterface.py"  = [" F841 " ]

"comtypes/test/test_outparam.py"  = [" F841 " ]

"comtypes/test/test_sapi.py"  = [" E401 " ]

"comtypes/test/test_server.py"  = [" F401 " , " F841 " ]

"comtypes/test/test_subinterface.py"  = [" E401 " , " F401 " , " F403 " , " F405 " ]

"comtypes/test/test_urlhistory.py"  = [" E401 " , " F401 " , " F403 " , " F405 " , " F841 " ]

"comtypes/test/test_variant.py"  = [" F401 " , " F821 " , " F841 " ]

[tool . coverage . run ]

#  Specify the source directory to avoid tracking temporary files created by "test_client_regenerate_modules.py".

#  Without this, coverage track these temporary files, leading to error when trying to generate a report.

source  = [" comtypes " ]

omit  = [" comtypes/gen/* " ]

[tool . coverage . report ]

exclude_also  = [

" if __name__ == .__main__.: " ,

" if TYPE_CHECKING: " ,

]

 You can’t perform that action at this time.
