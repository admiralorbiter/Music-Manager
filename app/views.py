from flask import render_template, request
from app import app, db
import pandas as pd
from app.models import Artist

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artists_overview', methods=['GET'])
def artists_overview():
    artists = Artist.query.all()
    search = request.args.get('search', '')
    if search:
        # Filter artists by name using the search term
        artists = Artist.query.filter(Artist.artist_name.ilike(f'%{search}%')).all()
    else:
        # Show all artists if no search term is provided
        artists = Artist.query.all()
    return render_template('artists_overview.html', artists=artists)

@app.route('/update_artist', methods=['POST'])
def update_artist():
    artist_name = request.form.get('artist_name')
    need_to_explore = request.form.get('need_to_explore') == 'on'
    looked_at = request.form.get('looked_at') == 'on'
    artist_playlist = request.form.get('artist_playlist') == 'on'

    artist = Artist.query.filter_by(artist_name=artist_name).first()
    if artist:
        artist.need_to_explore = need_to_explore
        artist.looked_at = looked_at
        artist.artist_playlist = artist_playlist
        db.session.commit()
    
    return '', 204

def load_data():
    file_path = 'artists.csv'
    data = pd.read_csv(file_path)
    
    for _, row in data.iterrows():
        artist = Artist(
            artist_name=row['Artist Name(s)'],
            need_to_explore=row['Need to Explore'],
            looked_at=row['Looked At'],
            artist_playlist=row['Artist Playlist'],
            one_of_each=row.get('One of Each', ''),
            notes=row.get('Notes', '')
        )
        db.session.add(artist)
    db.session.commit()