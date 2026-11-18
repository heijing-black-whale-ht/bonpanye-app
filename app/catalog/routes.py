from flask import Blueprint, render_template, request, redirect, url_for, flash

catalog = Blueprint('catalog', __name__)