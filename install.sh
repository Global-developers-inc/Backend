mkdir /opt/RedGreating
dnf install git -y
git clone https://github.com/Global-developers-inc/Frontend.git
cp ./* /opt/RedGreating/
cd /opt/RedGreating
python -m pip install flask flask_cors
cd Frontend/client
npm install
cd ..
mv RedGreating.service /etc/systemd/systemd/
systemctl daemon-reload
systemctl enable RedGreating.service
