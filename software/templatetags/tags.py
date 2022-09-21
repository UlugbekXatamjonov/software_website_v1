from django import template
from ..models import *
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('tags/lastest_games.html') # eng so'ngi o'yinlar
def lastest_games(count=5):
	lastest_games = Game.active.all()[:count]
	return {'lastest_games': lastest_games} 


@register.inclusion_tag('tags/lastest_softwares.html') # eng so'ngi proglar
def lastest_softwares(count=5):
	lastest_softwares = Software.active.all()[:count]
	return {'lastest_softwares': lastest_softwares} 


# @register.inclusion_tag('tags/lastest_softwares.html') # eng so'ngi proglar
# def lastest_softwares(count=5):
# 	lastest_softwares = Software.active.all()[:count]
# 	return {'lastest_softwares': lastest_softwares} 

