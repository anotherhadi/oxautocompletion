# 0xAutoCompletion  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">

A Handy Package to add Auto-Completion

# Installation :

From pip :

```bash
pip3 install oxautocompletion
```

From source :

```bash
git clone https://github.com/0x68616469/oxautocompletion/
```

### Requirements :

[oxansi](https://github.com/0x68616469/oxansi/)
(downloaded automatically with pip)

# Example :

```python
from oxautocompletion import complete

wordlist = ["John", "Jarvis", "Patrick", "Kevin", "Angela", "Laura"]

print("Name :")
word = complete(wordlist, case_sensitive=False)
print(f"Hi {word}")
```

result : 

<img src="https://media.giphy.com/media/CMtCwHdkxdY7uaidE0/giphy.gif" />

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/0x68616469)