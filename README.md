# JoinCSV-repo
Program for joining csv files using a specified column

## Tests

1. UTF-8 encoding was used to ensure proper output format for all characters in the text.
2. Removing BOM
   Some files, especially generated in Microsoft Office, contain BOM - according to Microsoft Docs 
https://docs.microsoft.com/en-us/globalization/encoding/byte-order-mark :


| Encoding             | Bom         | Python encoding kwarg |
|----------------------|-------------|-----------------------|
| UTF-8                | EF BB BF    | 'utf-8'               |
| UTF-16 big-endian    | FE FF       | 'utf-16-be'           |
| UTF-16 little-endian | FF FE       | 'utf-16-le'           |
| UTF-32 big-endian    | 00 00 FE FF | 'utf-32-be'           |
| UTF-32 little-endian | FF FE 00 00 | 'utf-32-le'           |

There is a need to upload files without BOM for now. 

3. Program was tested using relative and absolute paths.
