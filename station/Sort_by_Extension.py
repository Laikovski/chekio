"""
 You are given a list of files. You need to sort this list by the file extension. The files with the same extension
 should be sorted by name.

Some possible cases:

    Filename cannot be an empty string;
    Files without the extension should go before the files with one;
    Filename ".config" has an empty extension and a name ".config";
    Filename "config." has an empty extension and a name "config.";
    Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
    Filename ".imp.xls" has an extension "xls" and a name ".imp".

Input: A list of filenames.

Output: A list of filenames.
"""

from typing import List


def ext(file):
    splitted = file.split('.')
    if('' == splitted[0] and len(splitted) == 2):
        splitted = [''.join(splitted[1:]), '']
    return splitted[::-1]

def sort_by_ext(files: List[str]) -> List[str]:
  return sorted(files, key=ext)

# print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']))

print(sort_by_ext(['1.cad', '1.bat', '1.aa'])) # ['1.aa', '1.bat', '1.cad']
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']))
print(sort_by_ext(['.aa.doc', '1.cad', '1.bat', '1.aa'])) # ['1.aa', '1.bat', '1.cad', '.aa.doc']
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat'])) # ['.bat', '1.aa', '1.bat', '1.cad']