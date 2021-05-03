from django.shortcuts import render
import requests
from django.conf import settings
import datetime
import pytz
import tweepy
from management.models import MLBGameLine, MLBGame, TeamName
from django.db.models import Avg, Count, Min, Sum

def matchups(request):
    """ a view to show MLB game matchups """
    # Get the date for the SportspageFeeds API params
    todays_date = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
    yesterdays_date = todays_date + datetime.timedelta(days=-1)
    yesterday = yesterdays_date.strftime('%Y-%m-%d')

    # Get all objects in MLBGameLine model
    game_lines = MLBGameLine.objects.all()

    # Get game id from submitted form to show specific game info
    # Get city from form for weather API
    # Get league from form to render correct Matchup template

    if request.method == "GET":
        game_id = request.GET.get('gameId')
        city = request.GET.get('city')
        league = request.GET.get('league')

    # Convert game_id from to an int to match game.game_id on matchup template

    gameID = int(game_id)

    # Get currently selected game for template
    current = MLBGameLine.objects.get(gameID=gameID)

    # OpenWeatherMap API
    country = ",us"
    cityWeather = city + country
    params = {"q": cityWeather, "units": "imperial"}

    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    headers = {
        'x-rapidapi-key': settings.RAPID_API_KEY,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    results = requests.request("GET", url,
                               headers=headers, params=params).json()
    weather_data = results['list']

    for weather in weather_data:
        current_tz = pytz.timezone("UTC")
        new_tz = pytz.timezone("US/Eastern")
        weather_date = weather['dt_txt']
        weatherDatetime = datetime.datetime.strptime(
                                                 weather_date,
                                                 '%Y-%m-%d %H:%M:%S')
        localized_time = current_tz.localize(weatherDatetime)
        gameDayWeather = localized_time.astimezone(new_tz)
        weather['gameDate'] = gameDayWeather.strftime("%B %d, %Y")
        weather['gameTime'] = gameDayWeather.strftime("%-I%p")
        weather['gameTemp'] = round(weather['main']['temp'])
        weather['gameWeather'] = weather['weather'][0]['main']

    # Twitter/Tweepy API
    auth = tweepy.OAuthHandler(
        settings.TWITTER_API_KEY, settings.TWITTER_SECRET_KEY)
    auth.set_access_token(
        settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_SECRET_ACCESS_TOKEN)

    # Get current teams Twitter handles from db
    home_object = TeamName.objects.get(name=current.home_team)
    home_twitter = home_object.twitter_id

    away_object = TeamName.objects.get(name=current.away_team)
    away_twitter = away_object.twitter_id

    api = tweepy.API(auth)
    home_tweets = tweepy.Cursor(
        api.user_timeline, id=home_twitter, exclude_replies=True,
        include_rts=False).items(20)
    away_tweets = tweepy.Cursor(
        api.user_timeline, id=away_twitter, exclude_replies=True,
        include_rts=False).items(20)

    # Get all objects in MLBGame model for current game home team
    home_games = MLBGame.objects.filter(name__name=current.home_team)
    home_nickname = home_games[0].nickname
    wins_home = home_games.aggregate(Sum('win_home'))['win_home__sum']
    loss_home = home_games.aggregate(Sum('loss_home'))['loss_home__sum']
    home_total_wins = home_games.aggregate(
        total=Sum('win_home') + Sum('win_away'))['total']
    home_total_loss = home_games.aggregate(
        total=Sum('loss_home') + Sum('loss_away'))['total']

    # Get all objects in MLBGame model for current game away team
    away_games = MLBGame.objects.filter(name__name=current.away_team)
    away_nickname = away_games[0].nickname
    wins_away = away_games.aggregate(Sum('win_away'))['win_away__sum']
    loss_away = away_games.aggregate(Sum('loss_away'))['loss_away__sum']
    away_total_wins = away_games.aggregate(
        total=Sum('win_home') + Sum('win_away'))['total']
    away_total_loss = away_games.aggregate(
        total=Sum('loss_home') + Sum('loss_away'))['total']

    context = {
        'weather_data': weather_data,
        'game_lines': game_lines,
        'league': league,
        'current': current,
        'home_tweets': home_tweets,
        'away_tweets': away_tweets,
        'home_twitter': home_twitter,
        'away_twitter': away_twitter,
        'home_nickname': home_nickname,
        'away_nickname': away_nickname,
        'wins_home': wins_home,
        'loss_home': loss_home,
        'home_total_wins': home_total_wins,
        'home_total_loss': home_total_loss,
        'wins_away': wins_away,
        'loss_away': loss_away,
        'away_total_wins': away_total_wins,
        'away_total_loss': away_total_loss,
    }

    return render(request, 'matchups/matchups.html', context)
