o
    ÚÅc
  ã                   @   sd   d dl Z d dlZd dlZd dlZe d¡d Zd dlmZ e  ¡ Z	e
d dd Zdd	 Ze  dS )
é    Né   é   )Úgenerate_user_agentu  
      __      _ 
     / _|    | |    By WHOAMI-XD
    | |_ __ _| | _____
    |  _/ _` | |/ / _ \ âââââ¬âââââ¬â¬
    | || (_| |   <  __/ ââ¤ ââââââ¤ââ
    |_| \__,_|_|\_\___| ââââ´ â´â´ â´â´â´â
          Create fake emailc                  C   s`  	 d} dt  d t }zt d¡ t |¡}| ¡ d |  d }| d¡dkr0td	 td
 nZd|j	v r`| ¡ d |  d }| ¡ d |  d }td|  td|  td|  td n*d|v r| ¡ d |  d }td|  td|  td ntd t
d t  W n# ty   td t
d t  Y n ty®   td t  Y nw q)NTr   z3https://10minutemail.net/address.api.php?sessionid=z&_=é   Z	mail_listÚsubjectzHi, Welcome to 10 Minute Mailz[!] No messages yet u@    âââââââââââââââââââââz"from"ÚfromÚdatetimezFrom email: zdata time: zNew messages : u[    ââââââââââââââââââââââââââââââz
"datetime"z[*] Email expired ..ú Zsorry)ÚsisnÚtimÚtimeÚsleepÚrÚgetÚjsonÚfindÚprintÚtextÚinputÚexitÚ	TypeErrorÚAttributeError)ZERRZurlCODZsend2ÚmsgZemlZTM© r   ú/sdcard/fakemail/FAKE-EMAIL.pyÚCODE   sF   







þâr   c                  C   s   d} dt t ddddddd	d

}tj| |d}t| ¡ d }t| ¡ d at| ¡ d atd td| d  td t	 
d¡ t  d S )Nz)https://10minutemail.net/address.api.php?z10minutemail.netzapplication/json,zen-US,en;q=0.5zgzip,ZXMLHttpRequestz#https://10minutemail.net/m/?lang=arZtrailersÚclose)
ZHostZCookiez
User-AgentZAcceptzAccept-LanguagezAccept-EncodingzX-Requested-WithZRefererZTeZ
Connection)ÚheadersZmail_get_mailZ
session_idZmail_get_timeu\     ââââââââââââââââââââââââââââââz   [$] Email: Ú u]     ââââââââââââââââââââââââââââââ
é   )ÚCoker   r   r   Ústrr   r
   r   r   r   r   r   )Zvv1ckr   ÚsendZemailr   r   r   ÚEmAIl0   s*   ö

r#   )ZrequestsZsecretsr   r   Z	token_hexr    Z
user_agentr   Zsessionr   r   r   r#   r   r   r   r   Ú<module>   s     #
