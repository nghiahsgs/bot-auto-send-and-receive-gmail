# bot-auto-send-gmail
bot auto send gmail


There are several step, you neeed follow to ensure everything will work correctly

+ Step 1: install python 3 (if you already have python 3, you can skip this step)
+ Step 2: install library smtplib (if you already have one, you can skip this step)
+ Step 3: with every gmail you need send as a deliver, you need login this gmail and goto "https://myaccount.google.com/lesssecureapps?pli=1" and turn on to allow "less secure app" can send gmail (my python code is a less secure app)
+ Step 4: Open file data.txt: Every line in this file has template "username|password|gmail_receive|title|content"
+ Final step: Open cmd and type "python index.py", my python code will read file data.txt line by line and send email as u wished

Tks for reading

