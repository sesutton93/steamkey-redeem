# steamkey-redeem

Linux/Unix

1. add keys from email into keys.txt    
2. type 'source venv/bin/activate'
3. run 'python steamkey-redeem.py'
4. should read all keys in back to you
5. login and enter steam email key
6. congrats all your keys should be redeemed!

Windows - venv
 
 1. add keys from email into keys.txt 
 2. Install python3.9 from microsoft store (if you don't have it already)
 3. (admin powershell)  Set-ExecutionPolicy RemoteSigned
 4. Change the path in venv_windows\pyvenv.cfg to point to your installed python
 5. (powershell) 'venv_windows/Scripts/Activate.ps1'
 6. within the venv, run 'python steamkey-redeem.py'
 7. should read all keys in back to you
 8. login and enter steam email key
 9. congrats all your keys should be redeemed!

Windows - without venv
 
 1. add keys from email into keys.txt 
 2. Install python3.9 from microsoft store (if you don't have it already)
 3. ~~(powershell) python -m venv~~
 4. ~~(powershell) 'venv/bin/Activate.ps1'~~
 5. python -m pip install -r requirements.txt
 6. python -m pip install steam google
 7. within the venv, run 'python steamkey-redeem.py'
 8. should read all keys in back to you
 9. login and enter steam email key
 10. congrats all your keys should be redeemed!