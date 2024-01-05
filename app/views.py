import csv
import io
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Track

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            stream = io.StringIO(uploaded_file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream)
            next(csv_input, None)  # Skip the header row
            for row in csv_input:
                track = Track(
                    track_uri=row[0], track_name=row[1], artist_uri=row[2], 
                    artist_name=row[3], album_uri=row[4], album_name=row[5],
                    album_artist_uri=row[6], album_artist_name=row[7], 
                    album_release_date=row[8], album_image_url=row[9], 
                    disc_number=int(row[10]), track_number=int(row[11]), 
                    track_duration_ms=int(row[12]), track_preview_url=row[13],
                    explicit=row[14] == 'true', popularity=int(row[15]), 
                    isrc=row[16], added_by=row[17], added_at=row[18]
                )
                db.session.add(track)
            print('Committing...')
            db.session.commit()
        return redirect(url_for('index'))
    else:
        # Display the upload form and table
        tracks = Track.query.all()
        print(tracks)
        return render_template('index.html', tracks=tracks)