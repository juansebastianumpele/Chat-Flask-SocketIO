# Chat-Flask-SocketIO
Websocket adalah protokol komunikasi, yang menyediakan komunikasi dua arah melalui koneksi TCP tunggal.
Untuk memahami Websockets, kita harus memiliki pemahaman yang jelas tentang protokol HTTP karena keduanya selalu berjalan bersamaan.

HTTP adalah protokol yang memungkinkan pengambilan sumber daya, seperti dokumen HTML. 
Ini adalah dasar dari setiap pertukaran data di Web dan merupakan protokol klien-server, yang berarti permintaan diprakarsai oleh penerima, biasanya browser Web.
HTTP adalah protokol tingkat aplikasi tanpa kewarganegaraan di mana biasanya klien meminta informasi dengan header
menggunakan tindakan seperti GET, POST, PUT… dan server mengirimkan respons kembali ke klien dan koneksi ditutup.
Untuk setiap komunikasi, protokol HTTP akan membuka koneksi, pertukaran data kemudian koneksi ditutup.

Websocket juga merupakan protokol lapisan aplikasi dan merupakan peningkatan HTTP yang menggunakan koneksi TCP yang sama melalui ws://
Secara sederhana klien meminta server itu, dapatkah kita membuat koneksi WebSocket dan di server balasan..

<h3>Untuk Mempelajari Socket-IO lebih lanjut silahkan kunjungi link :</h3>
<ul>
  <li>https://pythonprogramminglanguage.com/python-flask-websocket/</li>
  <li>https://ichi.pro/id/menggunakan-websockets-dengan-python-74315371198182</li>
</ul>

========================================================
<p>jika terjadi masalah pada python socketIO silahkan install/upgrade :</p>

<li>pip install --upgrade python-socketio==4.6.0</li>
<li>pip install --upgrade python-engineio==3.13.2</li>
<li>pip install --upgrade Flask-SocketIO==4.3.1</li>
========================================================
