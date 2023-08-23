# Install Dependencies
pip install -r requirements.txt 


# Run Migrations
python manage.py migrate


# Run Collect Static
echo yes | python manage.py collectstatic
