from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__)