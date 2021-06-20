mkdir /opt/RedGreating
chmod +777 /opt/RedGreating
dnf install git -y
git clone https://github.com/Global-developers-inc/Frontend.git
cp ./* /opt/RedGreating/ -r
cd /opt/RedGreating
python -m pip install flask flask_cors
cd Frontend/client
npm install
npm audit fix
cd ../..
mv ./RedGreating.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable RedGreating.service
