from flask import Blueprint, render_template, request, redirect, url_for, flash

admin = Blueprint('admin', __name__)