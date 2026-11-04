**Test:** 



def test\_issue\_10():

&#x20;   links = \[

&#x20;       {"url": "https://example.com/docs/", "archived": False},

&#x20;       {"url": "https://old.example.com", "archived": True},

&#x20;   ]

&#x20;   assert is\_unique\_url("HTTPS://EXAMPLE.COM/docs", links) is False

&#x20;   assert is\_unique\_url("https://old.example.com", links) is True



**Results:** 



C:\\Users\\lifes\\OneDrive\\Desktop\\Assignment 5\\LinkVaulterSEF26-JesusM>python -m pytest -v -k test\_issue\_10

================================================= test session starts =================================================

platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0 -- C:\\Python314\\python.exe

cachedir: .pytest\_cache

rootdir: C:\\Users\\lifes\\OneDrive\\Desktop\\Assignment 5\\LinkVaulterSEF26-JesusM

configfile: pyproject.toml

testpaths: tests

collected 33 items / 32 deselected / 1 selected



tests/test\_issues.py::test\_issue\_10 PASSED                                                                       \[100%]



========================================== 1 passed, 32 deselected in 0.28s ===========================================



