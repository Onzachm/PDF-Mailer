# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

import csv
import smtplib
import tkinter as tk
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import base64
from pdf2image import convert_from_path
from io import BytesIO

a = Analysis(
    ['emailer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['base64', 'csv', 'smtplib', 'tkinter', 'email.mime.multipart', 'email.mime.image', 'email.mime.text', 'pdf2image', 'io'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='emailer2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='emailer2',
)
