# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\PC\\Documents\\Jobs\\taiwo\\project'],
             binaries=[],
             datas=[('mplwidget.py', '.'), ('window.ui','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pandas', 'PyQt4','tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='taiwo',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='t.ico')
